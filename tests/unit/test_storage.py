"""
tests/unit/test_storage.py
Pruebas unitarias para src.core.storage
"""
import pytest
import json
import sys
import os
from unittest.mock import patch, mock_open, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from core.storage import cargar_passwords, guardar_passwords


# ─────────────────────────────────────────
# cargar_passwords
# ─────────────────────────────────────────

class TestCargarPasswords:

    def test_carga_lista_correctamente(self):
        datos = [{"sitio": "github.com", "password": "Abc123!"}]
        m = mock_open(read_data=json.dumps(datos))
        with patch("builtins.open", m):
            result = cargar_passwords()
        assert result == datos

    def test_retorna_lista_vacia_si_no_existe_archivo(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = cargar_passwords()
        assert result == []

    def test_retorna_lista_vacia_si_json_invalido(self):
        m = mock_open(read_data="esto no es json {{{")
        with patch("builtins.open", m):
            result = cargar_passwords()
        assert result == []

    def test_retorna_lista_vacia_si_archivo_vacio(self):
        m = mock_open(read_data="")
        with patch("builtins.open", m):
            result = cargar_passwords()
        assert result == []

    def test_usa_archivo_por_defecto(self):
        m = mock_open(read_data="[]")
        with patch("builtins.open", m) as mock_file:
            cargar_passwords()
        mock_file.assert_called_once_with("passwords.json", "r")

    def test_usa_archivo_personalizado(self):
        m = mock_open(read_data="[]")
        with patch("builtins.open", m) as mock_file:
            cargar_passwords("mis_passwords.json")
        mock_file.assert_called_once_with("mis_passwords.json", "r")

    def test_retorna_lista(self):
        m = mock_open(read_data="[]")
        with patch("builtins.open", m):
            result = cargar_passwords()
        assert isinstance(result, list)

    def test_carga_multiples_entradas(self):
        datos = [
            {"sitio": "github.com", "password": "Abc123!"},
            {"sitio": None, "password": "Xyz789@"},
        ]
        m = mock_open(read_data=json.dumps(datos))
        with patch("builtins.open", m):
            result = cargar_passwords()
        assert len(result) == 2


# ─────────────────────────────────────────
# guardar_passwords
# ─────────────────────────────────────────

class TestGuardarPasswords:

    def test_escribe_en_archivo(self):
        passwords = [{"sitio": "github.com", "password": "Abc123!"}]
        m = mock_open()
        with patch("builtins.open", m):
            guardar_passwords(passwords)
        m.assert_called_once_with("passwords.json", "w")

    def test_escribe_json_valido(self):
        passwords = [{"sitio": "test.com", "password": "Pass1!"}]
        written = []
        m = mock_open()
        with patch("builtins.open", m):
            with patch("json.dump") as mock_dump:
                guardar_passwords(passwords)
                mock_dump.assert_called_once()
                args = mock_dump.call_args
                assert args[0][0] == passwords
                assert args[1]["indent"] == 4

    def test_usa_archivo_por_defecto(self):
        m = mock_open()
        with patch("builtins.open", m) as mock_file:
            guardar_passwords([])
        mock_file.assert_called_once_with("passwords.json", "w")

    def test_usa_archivo_personalizado(self):
        m = mock_open()
        with patch("builtins.open", m) as mock_file:
            guardar_passwords([], "mis_passwords.json")
        mock_file.assert_called_once_with("mis_passwords.json", "w")

    def test_guarda_lista_vacia(self):
        m = mock_open()
        with patch("builtins.open", m):
            with patch("json.dump") as mock_dump:
                guardar_passwords([])
                mock_dump.assert_called_once()

    def test_retorna_none(self):
        m = mock_open()
        with patch("builtins.open", m):
            result = guardar_passwords([])
        assert result is None


# ─────────────────────────────────────────
# Casos borde
# ─────────────────────────────────────────

class TestStorageBorde:

    def test_cargar_json_con_sitio_none(self):
        datos = [{"sitio": None, "password": "Abc123!"}]
        m = mock_open(read_data=json.dumps(datos))
        with patch("builtins.open", m):
            result = cargar_passwords()
        assert result[0]["sitio"] is None

    def test_guardar_y_cargar_ciclo_completo(self, tmp_path):
        """Test de ciclo real usando archivo temporal"""
        archivo = str(tmp_path / "test_passwords.json")
        passwords = [{"sitio": "test.com", "password": "Abc123!"}]

        guardar_passwords(passwords, archivo)
        result = cargar_passwords(archivo)

        assert result == passwords

    def test_guardar_sobreescribe_contenido(self, tmp_path):
        """Guardar dos veces deja solo los últimos datos"""
        archivo = str(tmp_path / "test_passwords.json")
        primera = [{"sitio": "a.com", "password": "Aaa111!"}]
        segunda = [{"sitio": "b.com", "password": "Bbb222!"}]

        guardar_passwords(primera, archivo)
        guardar_passwords(segunda, archivo)
        result = cargar_passwords(archivo)

        assert result == segunda
        assert len(result) == 1