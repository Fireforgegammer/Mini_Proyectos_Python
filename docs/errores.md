# 💥 ERROR
ImportError: cannot import name 'eliminar_password' from 'ui.acciones'

# 🎯 QUÉ SIGNIFICA

👉 En tu main.py haces esto:

from ui.acciones import eliminar_password

👉 Pero en acciones.py:

# ❌ NO existe una función llamada exactamente eliminar_password

🔍 CONFIRMA ESTO

Abre src/ui/acciones.py y busca:

def eliminar_password():
🧨 CASOS POSIBLES
# ❌ Caso 1: No existe

👉 Entonces por eso falla

# ❌ Caso 2: Tiene otro nombre

Ejemplo:

def eliminar_contrasena():

👉 Entonces tienes que importar ese nombre:

from ui.acciones import eliminar_contrasena
# ❌ Caso 3: Está mal escrito

Ejemplo:

def eliminar_pasword():  # falta una "s"

👉 Python es literal → no coincide

# ✅ SOLUCIONES
## ✔ Opción A (rápida)

Crea la función en acciones.py:

def eliminar_password():
    print("🗑️ Eliminar password (pendiente implementar)")
## ✔ Opción B (mejor)

Ajusta el import en main.py al nombre real

# 🔥 CONSEJO PRO

Para evitar estos errores:

👉 En VS Code:

Ctrl + click sobre eliminar_password
Si no te lleva a la función → no existe
🚀 RESUMEN

💥 El error no es de ejecución
💥 Es de nombre de función

### 👇 Siguiente paso

Pásame el contenido completo de acciones.py
y te digo exactamente qué nombres debes usar sin fallar 🔥

ahi lo tienes y da este error

Perfecto, ahora sí: este es el problema real de verdad 👇

#### 💥 ERROR
ModuleNotFoundError: No module named 'core'
#### 🎯 QUÉ SIGNIFICA

👉 Python no encuentra la carpeta core como módulo

Y esto pasa porque estás ejecutando:

python src/ui/acciones.py   ❌
# 🔴 IMPORTANTE (esto es la clave)

Tu proyecto está pensado para ejecutarse desde la raíz así:

python src/main.py   ✅
## 💣 Por qué falla

Cuando ejecutas directamente:

python src/ui/acciones.py

👉 Python toma como raíz:

src/ui/

Entonces intenta buscar:

src/ui/core  ❌ (no existe)
# ✅ SOLUCIÓN
✔ SIEMPRE ejecuta desde la raíz del proyecto:
cd C:\Users\IA\Documents\GitHub\Mini_Proyectos_Python
python src/main.py
# 🚀 OPCIÓN PRO (recomendada)

Para evitar estos problemas en el futuro:

🔧 Añade esto al inicio de main.py:
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

👉 Esto fuerza a Python a reconocer src como raíz

## 🔥 ALTERNATIVA LIMPIA (nivel pro)

Usar imports absolutos desde src:

from src.core.storage import cargar_passwords

Pero esto requiere ejecutar como módulo:

python -m src.main
# 🧠 RESUMEN

💥 No es un error de código
💥 Es cómo estás ejecutando el programa

✅ REGLA DE ORO

👉 Nunca ejecutes archivos internos directamente:

python src/ui/acciones.py ❌

👉 Siempre:

python src/main.py ✅