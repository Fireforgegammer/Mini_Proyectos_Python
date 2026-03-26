"""
tests/unit/test_acciones.py
Pruebas unitarias para src.ui.acciones (con mocks de I/O y storage)
"""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock, call

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from ui.acciones import (
    mostrar_passwords,
    ver_passwords,
    anadir_sitio,
    eliminar_password,
    buscar_password,
    pedir_opcion,
    pedir_numero,
    pedir_configuracion_password,
    generar_y_guardar_passwords,
)

PASSWORDS_FIXTURE = [
    {"sitio": "github.com", "password": "Abc123!@#xyz"},
    {"sitio": None,         "password": "Xyz789@abcde"},
]


# ─────────────────────────────────────────
# mostrar_passwords
# ─────────────────────────────────────────

class TestMostrarPasswords:

    def test_imprime_cada_entrada(self, capsys):
        mostrar_passwords(PASSWORDS_FIXTURE)
        out = capsys.readouterr().out
        assert "github.com" in out
        assert "Abc123!@#xyz" in out

    def test_sin_sitio_muestra_sin_asignar(self, capsys):
        mostrar_passwords(PASSWORDS_FIXTURE)
        out = capsys.readouterr().out
        assert "Sin asignar" in out

    def test_numeracion_desde_1(self, capsys):
        mostrar_passwords(PASSWORDS_FIXTURE)
        out = capsys.readouterr().out
        assert "1." in out
        assert "2." in out

    def test_lista_vacia_no_imprime_nada(self, capsys):
        mostrar_passwords([])
        out = capsys.readouterr().out
        assert out == ""


# ─────────────────────────────────────────
# ver_passwords
# ─────────────────────────────────────────

class TestVerPasswords:

    @patch("ui.acciones.cargar_passwords", return_value=PASSWORDS_FIXTURE)
    @patch("ui.acciones.evaluar_password", return_value="✅ Fuerte")
    def test_muestra_passwords_con_nivel(self, mock_eval, mock_cargar, capsys):
        ver_passwords()
        out = capsys.readouterr().out
        assert "github.com" in out
        assert "✅ Fuerte" in out

    @patch("ui.acciones.cargar_passwords", return_value=[])
    def test_lista_vacia_muestra_mensaje(self, mock_cargar, capsys):
        ver_passwords()
        out = capsys.readouterr().out
        assert "No hay contraseñas" in out

    @patch("ui.acciones.cargar_passwords", return_value=PASSWORDS_FIXTURE)
    @patch("ui.acciones.evaluar_password", return_value="⚠️ Media")
    def test_llama_evaluar_por_cada_password(self, mock_eval, mock_cargar):
        ver_passwords()
        assert mock_eval.call_count == len(PASSWORDS_FIXTURE)


# ─────────────────────────────────────────
# anadir_sitio
# ─────────────────────────────────────────

class TestAnadirSitio:

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": None, "password": "Abc123!"}
    ])
    @patch("builtins.input", side_effect=["1", "github.com"])
    def test_asigna_sitio_correctamente(self, mock_input, mock_cargar, mock_guardar):
        anadir_sitio()
        guardado = mock_guardar.call_args[0][0]
        assert guardado[0]["sitio"] == "github.com"

    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "ya_tiene.com", "password": "Abc123!"}
    ])
    def test_sin_sin_sitio_muestra_mensaje(self, mock_cargar, capsys):
        anadir_sitio()
        out = capsys.readouterr().out
        assert "No hay contraseñas sin asignar" in out

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": None, "password": "Abc123!"}
    ])
    @patch("builtins.input", side_effect=["abc", "github.com"])
    def test_seleccion_invalida_muestra_mensaje(self, mock_input, mock_cargar, mock_guardar, capsys):
        anadir_sitio()
        out = capsys.readouterr().out
        assert "inválida" in out
        mock_guardar.assert_not_called()

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": None, "password": "Abc123!"}
    ])
    @patch("builtins.input", side_effect=["99", "github.com"])
    def test_indice_fuera_de_rango_muestra_mensaje(self, mock_input, mock_cargar, mock_guardar, capsys):
        anadir_sitio()
        out = capsys.readouterr().out
        assert "inválida" in out


# ─────────────────────────────────────────
# eliminar_password
# ─────────────────────────────────────────

class TestEliminarPassword:

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "github.com", "password": "Abc123!"},
        {"sitio": "gitlab.com", "password": "Xyz789@"},
    ])
    @patch("builtins.input", return_value="1")
    def test_elimina_entrada_correcta(self, mock_input, mock_cargar, mock_guardar):
        eliminar_password()
        guardado = mock_guardar.call_args[0][0]
        assert len(guardado) == 1
        assert guardado[0]["sitio"] == "gitlab.com"

    @patch("ui.acciones.cargar_passwords", return_value=[])
    def test_lista_vacia_muestra_mensaje(self, mock_cargar, capsys):
        eliminar_password()
        out = capsys.readouterr().out
        assert "No hay contraseñas" in out

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "github.com", "password": "Abc123!"}
    ])
    @patch("builtins.input", return_value="abc")
    def test_input_no_numerico_muestra_mensaje(self, mock_input, mock_cargar, mock_guardar, capsys):
        eliminar_password()
        out = capsys.readouterr().out
        assert "número" in out
        mock_guardar.assert_not_called()

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "github.com", "password": "Abc123!"}
    ])
    @patch("builtins.input", return_value="99")
    def test_indice_fuera_de_rango(self, mock_input, mock_cargar, mock_guardar, capsys):
        eliminar_password()
        out = capsys.readouterr().out
        assert "rango" in out
        mock_guardar.assert_not_called()


# ─────────────────────────────────────────
# buscar_password
# ─────────────────────────────────────────

class TestBuscarPassword:

    @patch("ui.acciones.cargar_passwords", return_value=PASSWORDS_FIXTURE)
    @patch("builtins.input", return_value="github")
    def test_encuentra_por_nombre_parcial(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "github.com" in out

    @patch("ui.acciones.cargar_passwords", return_value=PASSWORDS_FIXTURE)
    @patch("builtins.input", return_value="GITHUB")
    def test_busqueda_insensible_a_mayusculas(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "github.com" in out

    @patch("ui.acciones.cargar_passwords", return_value=PASSWORDS_FIXTURE)
    @patch("builtins.input", return_value="xxxxnoexiste")
    def test_sin_resultados_muestra_mensaje(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "No se encontraron" in out

    @patch("ui.acciones.cargar_passwords", return_value=[])
    @patch("builtins.input", return_value="github")
    def test_lista_vacia_muestra_mensaje(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "No hay contraseñas" in out

    @patch("ui.acciones.cargar_passwords", return_value=PASSWORDS_FIXTURE)
    @patch("builtins.input", return_value="github")
    def test_no_muestra_passwords_sin_sitio(self, mock_input, mock_cargar, capsys):
        buscar_password()
        out = capsys.readouterr().out
        assert "Xyz789@abcde" not in out


# ─────────────────────────────────────────
# pedir_opcion
# ─────────────────────────────────────────

class TestPedirOpcion:

    @patch("builtins.input", return_value="s")
    def test_retorna_true_para_s(self, mock_input):
        assert pedir_opcion("¿?") is True

    @patch("builtins.input", return_value="n")
    def test_retorna_false_para_n(self, mock_input):
        assert pedir_opcion("¿?") is False

    @patch("builtins.input", side_effect=["x", "z", "s"])
    def test_reintenta_hasta_entrada_valida(self, mock_input):
        result = pedir_opcion("¿?")
        assert result is True
        assert mock_input.call_count == 3

    @patch("builtins.input", return_value="S")
    def test_mayuscula_invalida(self, mock_input, capsys):
        """'S' en mayúscula no es válido — solo 's' en minúscula"""
        with patch("builtins.input", side_effect=["S", "s"]):
            result = pedir_opcion("¿?")
        assert result is True


# ─────────────────────────────────────────
# pedir_numero
# ─────────────────────────────────────────

class TestPedirNumero:

    @patch("builtins.input", return_value="5")
    def test_retorna_entero(self, mock_input):
        assert pedir_numero("Num: ") == 5

    @patch("builtins.input", side_effect=["abc", "0", "3"])
    def test_reintenta_hasta_valido(self, mock_input):
        result = pedir_numero("Num: ", minimo=1)
        assert result == 3

    @patch("builtins.input", return_value="1")
    def test_minimo_por_defecto_es_1(self, mock_input):
        assert pedir_numero("Num: ") == 1

    @patch("builtins.input", side_effect=["3", "5"])
    def test_respeta_minimo_personalizado(self, mock_input):
        result = pedir_numero("Num: ", minimo=4)
        assert result == 5

    @patch("builtins.input", return_value="-1")
    def test_negativo_no_valido(self, mock_input, capsys):
        with patch("builtins.input", side_effect=["-1", "2"]):
            result = pedir_numero("Num: ", minimo=1)
        assert result == 2


# ─────────────────────────────────────────
# pedir_configuracion_password
# ─────────────────────────────────────────

class TestPedirConfiguracionPassword:

    @patch("builtins.input", side_effect=["s", "s", "s", "s"])
    def test_todas_activas(self, mock_input):
        config = pedir_configuracion_password()
        assert all(config.values())

    @patch("builtins.input", side_effect=["n", "n", "n", "n"])
    def test_todas_inactivas(self, mock_input):
        config = pedir_configuracion_password()
        assert not any(config.values())

    @patch("builtins.input", side_effect=["s", "n", "s", "n"])
    def test_configuracion_mixta(self, mock_input):
        config = pedir_configuracion_password()
        assert config["minus"] is True
        assert config["mayus"] is False
        assert config["numeros"] is True
        assert config["simbolos"] is False

    @patch("builtins.input", side_effect=["s", "n", "s", "n"])
    def test_retorna_claves_correctas(self, mock_input):
        config = pedir_configuracion_password()
        assert set(config.keys()) == {"minus", "mayus", "numeros", "simbolos"}


# ─────────────────────────────────────────
# generar_y_guardar_passwords
# ─────────────────────────────────────────

class TestGenerarYGuardarPasswords:

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[])
    @patch("ui.acciones.generar_passwords", return_value=[
        {"sitio": None, "password": "MockPass1!"},
        {"sitio": None, "password": "MockPass2!"},
    ])
    @patch("builtins.input", side_effect=["s", "s", "s", "n", "12", "2"])
    def test_genera_y_guarda(self, mock_input, mock_gen, mock_cargar, mock_guardar):
        generar_y_guardar_passwords()
        mock_guardar.assert_called_once()
        guardado = mock_guardar.call_args[0][0]
        assert len(guardado) == 2

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[
        {"sitio": "existente.com", "password": "Existente1!"}
    ])
    @patch("ui.acciones.generar_passwords", return_value=[
        {"sitio": None, "password": "Nueva1!"}
    ])
    @patch("builtins.input", side_effect=["s", "n", "n", "n", "8", "1"])
    def test_extiende_passwords_existentes(self, mock_input, mock_gen, mock_cargar, mock_guardar):
        generar_y_guardar_passwords()
        guardado = mock_guardar.call_args[0][0]
        assert len(guardado) == 2
        assert guardado[0]["sitio"] == "existente.com"

    @patch("ui.acciones.guardar_passwords")
    @patch("ui.acciones.cargar_passwords", return_value=[])
    @patch("ui.acciones.generar_passwords", return_value=[
        {"sitio": None, "password": "MockPass!"}
    ])
    @patch("builtins.input", side_effect=["s", "s", "s", "n", "12", "1"])
    def test_imprime_passwords_generadas(self, mock_input, mock_gen, mock_cargar, mock_guardar, capsys):
        generar_y_guardar_passwords()
        out = capsys.readouterr().out
        assert "MockPass!" in out