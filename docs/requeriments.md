 # Solo hay dos dependencias porque todo lo demás es biblioteca estándar de Python:
 ### Módulo_Origen_Necesita instalación
 -  stringstdlib❌
 - secretsstdlib❌
 - jsonstdlib❌
 - sys / osstdlib❌
 - pytestexterno✅
 - pytest-mockexterno✅ (para los mocks de tests)
 ### pytest-mock
  lo añadí porque los tests que generamos lo usan indirectamente, aunque en este caso usamos unittest.mock directamente — si prefieres dejarlo solo con pytest también es válido. 🚀