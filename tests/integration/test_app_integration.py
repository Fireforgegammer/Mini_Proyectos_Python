"""
tests/integration/test_app_integration.py
Pruebas de integración de la aplicación completa (UI + core)
"""
import pytest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from ui.acciones import (
    ver_passwords,
    anadir_sitio,
    eliminar_password,
    buscar_password,
    generar_y_guardar_passwords,
)
from core.storage import cargar_passwords, guardar_passwords
from core.generador import generar_passwords
from core.evaluador import evaluar_password


# ─────────────────────────────────────────
# Flujo: generar → ver
# ─────────────────────────────────────────

class TestFlujioGenerarVer:

    @patch("ui.acciones.cargar_passwords")
    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.generar_passwords")
    @patch("builtins.input", side_effect=["s", "s", "s", "n", "12", "3"])
    def test_generar_y_luego_ver(self, mock_input, mock_gen, mock_guardar, mock_cargar, capsys):
        """Generar contraseñas y luego verlas muestra el nivel de cada una"""
        passwords_generadas = [
            {"sitio": None, "password": "Abc123!@#xyz"},
            {"sitio": None, "password": "Xyz789@abcde"},
            {"sitio": None, "password": "Def456!qwert"},
        ]
        mock_gen.return_value = passwords_generadas
        mock_cargar.side_effect = [[], passwords_generadas]

        generar_y_guardar_passwords()
        ver_passwords()

        out = capsys.readouterr().out
        assert "Abc123!@#xyz" in out
        assert "Sin asignar" in out


# ─────────────────────────────────────────
# Flujo: generar → añadir sitio → ver
# ─────────────────────────────────────────

class TestFlujioGenerarAnadirVer:

    def test_generar_asignar_sitio_persistir(self, tmp_path):
        """Genera, asigna sitio y verifica que persiste correctamente"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        # Generar y guardar
        passwords = generar_passwords(config, longitud=12, cantidad=2)
        guardar_passwords(passwords, archivo)

        # Simular anadir_sitio sobre archivo real
        with patch("ui.acciones.cargar_passwords", return_value=cargar_passwords(archivo)), \
             patch("ui.acciones.guardar_passwords", side_effect=lambda p, *a: guardar_passwords(p, archivo)), \
             patch("builtins.input", side_effect=["1", "github.com"]):
            anadir_sitio()

        final = cargar_passwords(archivo)
        assert final[0]["sitio"] == "github.com"
        assert final[1]["sitio"] is None

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords")
    @patch("builtins.input", side_effect=["1", "gitlab.com"])
    def test_anadir_sitio_llama_guardar(self, mock_input, mock_cargar, mock_guardar):
        mock_cargar.return_value = [{"sitio": None, "password": "Abc123!"}]
        anadir_sitio()
        mock_guardar.assert_called_once()


# ─────────────────────────────────────────
# Flujo: generar → eliminar → verificar
# ─────────────────────────────────────────

class TestFlujioGenerarEliminar:

    def test_eliminar_reduce_lista(self, tmp_path):
        """Tras eliminar una entrada, el archivo tiene una menos"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        passwords = generar_passwords(config, longitud=10, cantidad=3)
        guardar_passwords(passwords, archivo)

        with patch("ui.acciones.cargar_passwords", return_value=cargar_passwords(archivo)), \
             patch("ui.acciones.guardar_passwords", side_effect=lambda p, *a: guardar_passwords(p, archivo)), \
             patch("builtins.input", return_value="1"):
            eliminar_password()

        final = cargar_passwords(archivo)
        assert len(final) == 2

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "a.com", "password": "Aaa111!xxx"},
        {"sitio": "b.com", "password": "Bbb222!yyy"},
    ])
    @patch("builtins.input", return_value="2")
    def test_elimina_el_elemento_correcto(self, mock_input, mock_cargar, mock_guardar):
        eliminar_password()
        guardado = mock_guardar.call_args[0][0]
        assert len(guardado) == 1
        assert guardado[0]["sitio"] == "a.com"


# ─────────────────────────────────────────
# Flujo: generar → buscar
# ─────────────────────────────────────────

class TestFlujioGenerarBuscar:

    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "github.com",  "password": "Abc123!@#xyz"},
        {"sitio": "gitlab.com",  "password": "Xyz789@abcde"},
        {"sitio": None,          "password": "Def456!qwert"},
    ])
    @patch("builtins.input", return_value="git")
    def test_buscar_devuelve_coincidencias(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "github.com" in out
        assert "gitlab.com" in out

    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "github.com", "password": "Abc123!@#xyz"},
        {"sitio": None,         "password": "Xyz789@abcde"},
    ])
    @patch("builtins.input", return_value="git")
    def test_buscar_excluye_sin_sitio(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "Xyz789@abcde" not in out


# ─────────────────────────────────────────
# Flujo completo de aplicación (end-to-end con tmp_path)
# ─────────────────────────────────────────

class TestFlujoEndToEnd:

    def test_ciclo_completo(self, tmp_path):
        """
        E2E: generar → persistir → cargar → asignar sitio → evaluar → eliminar
        """
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}

        # 1. Generar y guardar
        passwords = generar_passwords(config, longitud=12, cantidad=3)
        guardar_passwords(passwords, archivo)

        # 2. Cargar y verificar
        cargadas = cargar_passwords(archivo)
        assert len(cargadas) == 3

        # 3. Asignar sitio al primero
        cargadas[0]["sitio"] = "github.com"
        guardar_passwords(cargadas, archivo)

        # 4. Evaluar todos
        recargadas = cargar_passwords(archivo)
        for p in recargadas:
            nivel = evaluar_password(p["password"])
            assert nivel in {"✅ Fuerte", "🔥 Muy fuerte"}

        # 5. Eliminar el primero
        recargadas.pop(0)
        guardar_passwords(recargadas, archivo)

        # 6. Verificar estado final
        final = cargar_passwords(archivo)
        assert len(final) == 2
        assert all(p["sitio"] is None for p in final)

    def test_persistencia_entre_operaciones(self, tmp_path):
        """Los datos no se corrompen tras múltiples operaciones de lectura/escritura"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        for _ in range(5):
            existentes = cargar_passwords(archivo)
            nuevas = generar_passwords(config, longitud=10, cantidad=2)
            existentes.extend(nuevas)
            guardar_passwords(existentes, archivo)

        total = cargar_passwords(archivo)
        assert len(total) == 10
        for p in total:
            assert isinstance(p["password"], str)
            assert len(p["password"]) == 10