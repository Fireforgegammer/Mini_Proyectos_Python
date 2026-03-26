"""
tests/unit/test_evaluador.py
Pruebas unitarias para src.core.evaluador
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from core.evaluador import evaluar_password


# ─────────────────────────────────────────
# Casos felices — niveles esperados
# ─────────────────────────────────────────

class TestEvaluarPasswordNiveles:

    def test_password_muy_fuerte(self):
        """Mayus + minus + numeros + simbolos + longitud>=12 → Muy fuerte"""
        assert evaluar_password("Abc123456!@#") == "🔥 Muy fuerte"

    def test_password_fuerte(self):
        """Mayus + minus + numeros + simbolos, longitud < 8 → Fuerte"""
        assert evaluar_password("Aa1!") == "✅ Fuerte"

    def test_password_media(self):
        """Mayus + minus + numeros, sin simbolos, longitud < 8 → Media"""
        assert evaluar_password("Abc123") == "⚠️ Media"

    def test_password_debil(self):
        """Solo minusculas → Débil"""
        assert evaluar_password("abc") == "❌ Débil"

    def test_password_debil_solo_numeros(self):
        """Solo números → Débil"""
        assert evaluar_password("12345") == "❌ Débil"


# ─────────────────────────────────────────
# Sistema de puntuación — criterios individuales
# ─────────────────────────────────────────

class TestEvaluarPasswordPuntuacion:

    def test_solo_mayusculas_es_debil(self):
        assert evaluar_password("ABCDEF") == "❌ Débil"

    def test_solo_simbolos_es_debil(self):
        assert evaluar_password("!@#$") == "❌ Débil"

    def test_mayus_mas_minus_es_media(self):
        """Mayus + minus = 2 puntos → Débil (<=2), no llega a Media"""
        assert evaluar_password("AbCd") == "❌ Débil"

    def test_mayus_minus_numeros_es_media(self):
        assert evaluar_password("Abc1") == "⚠️ Media"

    def test_longitud_8_suma_punto(self):
        """8 caracteres suman +1, empujando de Débil a Media con otros criterios"""
        # minus(1) + numeros(1) + longitud>=8(1) = 3 → Media
        assert evaluar_password("abcd1234") == "⚠️ Media"

    def test_longitud_12_suma_dos_puntos(self):
        """12+ caracteres suman +2"""
        # minus(1) + numeros(1) + longitud>=12(2) = 4 → Fuerte
        assert evaluar_password("abcd12345678") == "✅ Fuerte"

    def test_longitud_exacta_8_no_es_12(self):
        """Exactamente 8 caracteres suma +1, no +2"""
        result = evaluar_password("Abcd123!")
        # mayus+minus+num+sim+len>=8 = 5 → Muy fuerte
        assert result == "🔥 Muy fuerte"


# ─────────────────────────────────────────
# Casos borde
# ─────────────────────────────────────────

class TestEvaluarPasswordBorde:

    def test_password_vacia(self):
        """Cadena vacía: sin criterios cumplidos → Débil"""
        assert evaluar_password("") == "❌ Débil"

    def test_password_un_caracter_minuscula(self):
        assert evaluar_password("a") == "❌ Débil"

    def test_password_un_caracter_simbolo(self):
        assert evaluar_password("!") == "❌ Débil"

    def test_longitud_exacta_12(self):
        """Exactamente 12 caracteres suma +2"""
        assert evaluar_password("Abcdefghij1!") == "🔥 Muy fuerte"

    def test_longitud_11_no_suma_2(self):
        """11 caracteres suma +1, no +2"""
        # minus+mayus+num+sim+len>=8 = 5 → Muy fuerte igualmente
        result = evaluar_password("Abcdefghi1!")
        assert result == "🔥 Muy fuerte"

    def test_password_muy_larga(self):
        """Contraseña muy larga sigue siendo Muy fuerte"""
        assert evaluar_password("Abc123!@#" * 10) == "🔥 Muy fuerte"

    def test_retorno_es_string(self):
        """La función siempre retorna str"""
        assert isinstance(evaluar_password("cualquier"), str)