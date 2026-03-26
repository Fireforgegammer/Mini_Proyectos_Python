"""
tests/unit/test_generador.py
Pruebas unitarias para src.core.generador
"""
import pytest
import string
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from core.generador import construir_pantalla, generar_password, generar_passwords


# ─────────────────────────────────────────
# construir_pantalla
# ─────────────────────────────────────────

class TestConstruirPantalla:

    def test_config_todas_activas(self):
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}
        pool, required = construir_pantalla(config)
        assert string.ascii_uppercase in pool
        assert string.ascii_lowercase in pool
        assert string.digits in pool
        assert string.punctuation in pool

    def test_required_chars_longitud_correcta(self):
        """Un required_char por cada tipo activo"""
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}
        _, required = construir_pantalla(config)
        assert len(required) == 3

    def test_required_chars_pertenecen_a_su_conjunto(self):
        config = {"mayus": True, "minus": False, "numeros": True, "simbolos": False}
        _, required = construir_pantalla(config)
        all_chars = string.ascii_uppercase + string.digits
        for c in required:
            assert c in all_chars

    def test_config_solo_minus(self):
        config = {"mayus": False, "minus": True, "numeros": False, "simbolos": False}
        pool, required = construir_pantalla(config)
        assert pool == string.ascii_lowercase
        assert len(required) == 1

    def test_config_ninguna_activa_lanza_error(self):
        config = {"mayus": False, "minus": False, "numeros": False, "simbolos": False}
        with pytest.raises(ValueError, match="al menos un tipo"):
            construir_pantalla(config)

    def test_pool_no_contiene_chars_de_tipo_inactivo(self):
        config = {"mayus": False, "minus": True, "numeros": False, "simbolos": False}
        pool, _ = construir_pantalla(config)
        for c in string.ascii_uppercase:
            assert c not in pool
        for c in string.digits:
            assert c not in pool


# ─────────────────────────────────────────
# generar_password
# ─────────────────────────────────────────

class TestGenerarPassword:

    def test_longitud_correcta(self):
        pool = string.ascii_lowercase + string.digits
        required = ["a", "1"]
        result = generar_password(10, pool, required)
        assert len(result) == 10

    def test_retorna_string(self):
        pool = string.ascii_lowercase
        result = generar_password(5, pool, ["a"])
        assert isinstance(result, str)

    def test_contiene_required_chars(self):
        """Los required_chars deben aparecer en la contraseña generada"""
        pool = string.ascii_lowercase + string.digits
        required = ["a", "1"]
        # Con longitud == len(required) solo hay required_chars
        result = generar_password(2, pool, required)
        assert sorted(result) == sorted(required)

    def test_longitud_igual_a_required(self):
        """Longitud exactamente igual al número de required_chars"""
        pool = string.ascii_lowercase
        required = ["a", "b", "c"]
        result = generar_password(3, pool, required)
        assert len(result) == 3

    def test_longitud_menor_a_required_lanza_error(self):
        pool = string.ascii_lowercase
        required = ["a", "b", "c"]
        with pytest.raises(ValueError):
            generar_password(2, pool, required)

    def test_todos_los_chars_en_pool(self):
        pool = string.ascii_lowercase
        required = ["a"]
        result = generar_password(8, pool, required)
        for c in result:
            assert c in pool

    def test_aleatoriedad_entre_llamadas(self):
        """Dos llamadas no deben producir la misma contraseña (altamente improbable)"""
        pool = string.ascii_letters + string.digits
        required = ["A"]
        results = {generar_password(16, pool, ["A"]) for _ in range(10)}
        assert len(results) > 1


# ─────────────────────────────────────────
# generar_passwords
# ─────────────────────────────────────────

class TestGenerarPasswords:

    def setup_method(self):
        self.config = {
            "mayus": True, "minus": True,
            "numeros": True, "simbolos": False
        }

    def test_cantidad_correcta(self):
        result = generar_passwords(self.config, longitud=12, cantidad=5)
        assert len(result) == 5

    def test_estructura_de_cada_item(self):
        result = generar_passwords(self.config, longitud=10, cantidad=2)
        for item in result:
            assert "sitio" in item
            assert "password" in item

    def test_sitio_es_none(self):
        result = generar_passwords(self.config, longitud=10, cantidad=3)
        for item in result:
            assert item["sitio"] is None

    def test_longitud_de_cada_password(self):
        result = generar_passwords(self.config, longitud=14, cantidad=3)
        for item in result:
            assert len(item["password"]) == 14

    def test_cantidad_uno(self):
        result = generar_passwords(self.config, longitud=8, cantidad=1)
        assert len(result) == 1

    def test_config_invalida_propaga_error(self):
        config_vacia = {"mayus": False, "minus": False, "numeros": False, "simbolos": False}
        with pytest.raises(ValueError):
            generar_passwords(config_vacia, longitud=8, cantidad=1)

    def test_passwords_son_distintas(self):
        """Alta probabilidad de que las contraseñas generadas sean distintas"""
        result = generar_passwords(self.config, longitud=16, cantidad=10)
        passwords = [r["password"] for r in result]
        assert len(set(passwords)) > 1


# ─────────────────────────────────────────
# Casos borde
# ─────────────────────────────────────────

class TestGeneradorBorde:

    def test_longitud_minima_igual_a_tipos_activos(self):
        """Con 2 tipos activos, longitud mínima válida es 2"""
        config = {"mayus": True, "minus": True, "numeros": False, "simbolos": False}
        result = generar_passwords(config, longitud=2, cantidad=1)
        assert len(result[0]["password"]) == 2

    def test_solo_un_tipo_activo(self):
        config = {"mayus": False, "minus": True, "numeros": False, "simbolos": False}
        result = generar_passwords(config, longitud=8, cantidad=1)
        pw = result[0]["password"]
        assert all(c in string.ascii_lowercase for c in pw)

    def test_cantidad_grande(self):
        config = {"mayus": True, "minus": True, "numeros": True, "simbolos": True}
        result = generar_passwords(config, longitud=12, cantidad=100)
        assert len(result) == 100