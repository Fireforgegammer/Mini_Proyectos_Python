"""
tests/conftest.py
Fixtures compartidas para todos los tests del proyecto.
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


@pytest.fixture
def passwords_fixture():
    """Lista de contraseñas de prueba con y sin sitio asignado."""
    return [
        {"sitio": "github.com",  "password": "Abc123!@#xyz"},
        {"sitio": "gitlab.com",  "password": "Xyz789@abcde"},
        {"sitio": None,          "password": "Def456!qwert"},
    ]


@pytest.fixture
def config_completa():
    """Configuración con todos los tipos de caracteres activos."""
    return {"mayus": True, "minus": True, "numeros": True, "simbolos": True}


@pytest.fixture
def config_basica():
    """Configuración mínima: solo minúsculas y números."""
    return {"mayus": False, "minus": True, "numeros": True, "simbolos": False}


@pytest.fixture
def archivo_passwords(tmp_path):
    """Ruta a un archivo temporal de passwords.json para tests con I/O real."""
    return str(tmp_path / "passwords.json")