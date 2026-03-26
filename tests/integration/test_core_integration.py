"""
tests/integration/test_core_integration.py
Pruebas de integración entre src.core.evaluador, src.core.generador y src.core.storage
"""
import pytest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from core.generador import generar_passwords
from core.evaluador import evaluar_password
from core.storage import cargar_passwords, guardar_passwords


# ─────────────────────────────────────────
# generador + evaluador
# ─────────────────────────────────────────

class TestGeneradorEvaluador:

    def test_passwords_generadas_no_son_debiles(self):
        """Passwords con todos los tipos activos y longitud>=12 no deben ser Débiles"""
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}
        passwords = generar_passwords(config, longitud=12, cantidad=20)
        for p in passwords:
            nivel = evaluar_password(p["password"])
            assert nivel != "❌ Débil", f"Password débil generada: {p['password']}"

    def test_passwords_largas_son_fuertes_o_muy_fuertes(self):
        """Con todos los tipos y longitud 16, deben ser Fuerte o Muy fuerte"""
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}
        passwords = generar_passwords(config, longitud=16, cantidad=10)
        niveles_validos = {"✅ Fuerte", "🔥 Muy fuerte"}
        for p in passwords:
            nivel = evaluar_password(p["password"])
            assert nivel in niveles_validos

    def test_password_solo_minus_longitud_corta_es_debil(self):
        """Solo minúsculas y longitud 4 → siempre Débil"""
        config = {"mayus": False, "minus": True, "numeros": False, "simbolos": False}
        passwords = generar_passwords(config, longitud=4, cantidad=5)
        for p in passwords:
            nivel = evaluar_password(p["password"])
            assert nivel == "❌ Débil"

    def test_password_completa_longitud_8_al_menos_media(self):
        """Todos los tipos activos y longitud=8 → al menos Media"""
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}
        passwords = generar_passwords(config, longitud=8, cantidad=10)
        niveles_aceptables = {"⚠️ Media", "✅ Fuerte", "🔥 Muy fuerte"}
        for p in passwords:
            nivel = evaluar_password(p["password"])
            assert nivel in niveles_aceptables


# ─────────────────────────────────────────
# generador + storage
# ─────────────────────────────────────────

class TestGeneradorStorage:

    def test_generar_y_persistir_passwords(self, tmp_path):
        """Generar contraseñas y guardarlas, luego cargarlas"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        nuevas = generar_passwords(config, longitud=12, cantidad=3)
        guardar_passwords(nuevas, archivo)
        cargadas = cargar_passwords(archivo)

        assert len(cargadas) == 3
        for p in cargadas:
            assert "password" in p
            assert "sitio" in p

    def test_passwords_persisten_correctamente(self, tmp_path):
        """Los valores de las contraseñas se mantienen tras guardar y cargar"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}

        originales = generar_passwords(config, longitud=14, cantidad=5)
        guardar_passwords(originales, archivo)
        recuperadas = cargar_passwords(archivo)

        passwords_orig = [p["password"] for p in originales]
        passwords_rec = [p["password"] for p in recuperadas]
        assert passwords_orig == passwords_rec

    def test_acumulacion_de_passwords(self, tmp_path):
        """Guardar dos lotes consecutivos acumula todas las entradas"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        lote1 = generar_passwords(config, longitud=10, cantidad=3)
        guardar_passwords(lote1, archivo)

        existentes = cargar_passwords(archivo)
        lote2 = generar_passwords(config, longitud=10, cantidad=2)
        existentes.extend(lote2)
        guardar_passwords(existentes, archivo)

        total = cargar_passwords(archivo)
        assert len(total) == 5

    def test_sitio_none_persiste_como_none(self, tmp_path):
        """El campo sitio=None se preserva tras guardar y cargar"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        passwords = generar_passwords(config, longitud=10, cantidad=2)
        guardar_passwords(passwords, archivo)
        recuperadas = cargar_passwords(archivo)

        for p in recuperadas:
            assert p["sitio"] is None


# ─────────────────────────────────────────
# evaluador + storage
# ─────────────────────────────────────────

class TestEvaluadorStorage:

    def test_evaluar_passwords_cargadas(self, tmp_path):
        """Las contraseñas cargadas desde disco pueden evaluarse correctamente"""
        archivo = str(tmp_path / "passwords.json")
        passwords = [
            {"sitio": "github.com", "password": "Abc123!@#xyz"},
            {"sitio": None,         "password": "abcdefgh"},
        ]
        guardar_passwords(passwords, archivo)
        cargadas = cargar_passwords(archivo)

        niveles = [evaluar_password(p["password"]) for p in cargadas]
        assert niveles[0] == "🔥 Muy fuerte"
        assert niveles[1] in {"❌ Débil", "⚠️ Media"}

    def test_archivo_inexistente_devuelve_lista_evaluable(self):
        """cargar desde archivo inexistente devuelve [] — no hay nada que evaluar"""
        cargadas = cargar_passwords("archivo_que_no_existe_xyz.json")
        assert cargadas == []
        niveles = [evaluar_password(p["password"]) for p in cargadas]
        assert niveles == []


# ─────────────────────────────────────────
# flujo completo: generador + evaluador + storage
# ─────────────────────────────────────────

class TestFlujoCoreCompleto:

    def test_generar_guardar_cargar_evaluar(self, tmp_path):
        """Flujo completo del núcleo sin UI"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}

        # 1. Generar
        nuevas = generar_passwords(config, longitud=12, cantidad=5)

        # 2. Guardar
        guardar_passwords(nuevas, archivo)

        # 3. Cargar
        cargadas = cargar_passwords(archivo)
        assert len(cargadas) == 5

        # 4. Evaluar
        for p in cargadas:
            nivel = evaluar_password(p["password"])
            assert nivel in {"✅ Fuerte", "🔥 Muy fuerte"}

    def test_asignar_sitio_y_persistir(self, tmp_path):
        """Simula el flujo de anadir_sitio sin UI"""
        archivo = str(tmp_path / "passwords.json")
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}

        passwords = generar_passwords(config, longitud=10, cantidad=2)
        guardar_passwords(passwords, archivo)

        # Simular asignación de sitio
        cargadas = cargar_passwords(archivo)
        cargadas[0]["sitio"] = "github.com"
        guardar_passwords(cargadas, archivo)

        final = cargar_passwords(archivo)
        assert final[0]["sitio"] == "github.com"
        assert final[1]["sitio"] is None