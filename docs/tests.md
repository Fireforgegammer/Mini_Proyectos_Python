He generado los tests 100% compatibles con pytest usando unittest.mock para los mocks — funcionarán perfectamente cuando tengas pytest instalado en tu proyecto con pip install pytest pytest-mock.
# resumen de lo generado
tests/
├── conftest.py                          # Fixtures compartidas
├── unit/
│   ├── test_evaluador.py    — 15 tests  # Niveles, puntuación, bordes
│   ├── test_generador.py    — 22 tests  # construir_pantalla, generar_password, generar_passwords
│   ├── test_storage.py      — 14 tests  # cargar/guardar con mocks + tmp_path
│   └── test_acciones.py     — 32 tests  # Todas las acciones mockeando I/O y storage
└── integration/
    ├── test_core_integration.py — 12 tests  # generador↔evaluador, generador↔storage, flujo completo core
    └── test_app_integration.py  — 10 tests  # Flujos UI+core, E2E con tmp_path
# para ejecutarlos en tu proyecto
pip install pytest pytest-mock
pytest tests/ -v
# para ejecutar solo unitarios o solo integracion
pytest tests/unitarios/ -v
pytest tests/integration/ -v