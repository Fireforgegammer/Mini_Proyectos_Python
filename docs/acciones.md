# 🎬 src.ui.acciones

Módulo de acciones de usuario para el paquete `src.ui`.

---

## 📋 Descripción

`acciones.py` implementa todas las operaciones interactivas de la aplicación. Actúa como capa intermedia entre la interfaz de menú (`src.ui.menu`) y el núcleo del sistema (`src.core`), gestionando la entrada del usuario por consola, la validación de datos y la coordinación entre persistencia, generación y evaluación de contraseñas.

---

## 📁 Ubicación

```
src/
└── ui/
    └── acciones.py
```

---

## 📦 Dependencias

| Módulo                  | Función importada                          |
|-------------------------|--------------------------------------------|
| `core.storage`          | `cargar_passwords`, `guardar_passwords`    |
| `core.evaluador`        | `evaluar_password`                         |
| `core.generador`        | `generar_passwords`                        |

---

## ⚙️ API

### Funciones de visualización

---

#### `mostrar_passwords(passwords: list) -> None`

Imprime por consola la lista de contraseñas numerada, mostrando sitio y contraseña.

| Parámetro   | Tipo   | Descripción                        |
|-------------|--------|------------------------------------|
| `passwords` | `list` | Lista de diccionarios `{sitio, password}`. |

---

#### `ver_passwords() -> None`

Carga las contraseñas desde el archivo de persistencia y las muestra en consola junto con su nivel de seguridad evaluado.

Formato de salida por entrada:
```
1. github.com -> aB3kL9mZqR1w -> ✅ Fuerte
2. Sin asignar -> X7nPc2tWjY4s -> ⚠️ Media
```

---

### Funciones de gestión

---

#### `anadir_sitio() -> None`

Permite asignar un nombre de sitio a una contraseña que aún no tiene uno. Muestra solo las contraseñas con `sitio = None`, solicita al usuario que elija una e introduce el sitio, y guarda los cambios.

**Flujo:**
1. Filtra contraseñas sin sitio asignado.
2. Muestra la lista numerada.
3. Solicita selección e introduce el nombre del sitio.
4. Actualiza el registro original y persiste los cambios.

---

#### `eliminar_password() -> None`

Muestra la lista completa de contraseñas y permite eliminar la entrada seleccionada por número, con confirmación tras la eliminación.

**Flujo:**
1. Carga y muestra la lista con `mostrar_passwords`.
2. Solicita número a eliminar con validación de rango.
3. Elimina la entrada, guarda y confirma.

---

#### `buscar_password() -> None`

Realiza una búsqueda por nombre de sitio (insensible a mayúsculas, búsqueda parcial) e imprime los resultados encontrados.

**Comportamiento:**
- Ignora contraseñas con `sitio = None`.
- La búsqueda es de tipo *contains*, no exacta.
- Imprime un mensaje si no hay resultados.

---

#### `generar_y_guardar_passwords() -> None`

Orquesta el flujo completo de generación y persistencia de nuevas contraseñas: solicita configuración, longitud y cantidad al usuario, genera las contraseñas, las muestra y las añade al archivo existente.

**Flujo:**
1. Llama a `pedir_configuracion_password()` para obtener la config.
2. Llama a `pedir_numero()` para longitud (mínimo 4) y cantidad (mínimo 1).
3. Genera las contraseñas con `generar_passwords()`.
4. Muestra las contraseñas generadas.
5. Carga las existentes, añade las nuevas y guarda.

---

### Funciones de entrada de datos

---

#### `pedir_opcion(mensaje: str) -> bool`

Solicita una respuesta `s/n` al usuario en bucle hasta recibir una entrada válida.

| Parámetro | Tipo  | Descripción                        |
|-----------|-------|------------------------------------|
| `mensaje` | `str` | Texto mostrado como prompt.        |

| Retorno | Descripción                                  |
|---------|----------------------------------------------|
| `bool`  | `True` si el usuario introduce `"s"`, `False` si introduce `"n"`. |

---

#### `pedir_numero(mensaje: str, minimo: int = 1) -> int`

Solicita un número entero al usuario en bucle hasta recibir un valor válido mayor o igual al mínimo indicado.

| Parámetro | Tipo  | Valor por defecto | Descripción                    |
|-----------|-------|-------------------|--------------------------------|
| `mensaje` | `str` | —                 | Texto mostrado como prompt.    |
| `minimo`  | `int` | `1`               | Valor mínimo aceptado.         |

| Retorno | Descripción                    |
|---------|--------------------------------|
| `int`   | Número entero validado.        |

---

#### `pedir_configuracion_password() -> dict`

Solicita al usuario qué tipos de caracteres desea incluir en la generación de contraseñas mediante cuatro preguntas `s/n`.

| Retorno | Descripción                                                                 |
|---------|-----------------------------------------------------------------------------|
| `dict`  | Diccionario con claves `"minus"`, `"mayus"`, `"numeros"`, `"simbolos"` y valores `bool`. |

Ejemplo de retorno:
```python
{
    "minus":    True,
    "mayus":    True,
    "numeros":  True,
    "simbolos": False
}
```

---

## 🔄 Relación entre Funciones

```
generar_y_guardar_passwords()
  ├── pedir_configuracion_password()
  │     └── pedir_opcion()  ×4
  ├── pedir_numero()  ×2
  ├── generar_passwords()       ← src.core.generador
  ├── cargar_passwords()        ← src.core.storage
  └── guardar_passwords()       ← src.core.storage

ver_passwords()
  ├── cargar_passwords()        ← src.core.storage
  └── evaluar_password()        ← src.core.evaluador

anadir_sitio()
  ├── cargar_passwords()
  └── guardar_passwords()

eliminar_password()
  ├── cargar_passwords()
  ├── mostrar_passwords()
  └── guardar_passwords()

buscar_password()
  └── cargar_passwords()
```

---

## 🚀 Ejemplos de Uso

> Las funciones de este módulo son invocadas directamente desde `src.ui.menu` y no están diseñadas para ser usadas de forma aislada. A modo ilustrativo:

```python
from src.ui.acciones import ver_passwords, buscar_password

ver_passwords()
# 1. github.com -> aB3kL9mZqR1w -> ✅ Fuerte
# 2. Sin asignar -> X7nPc2tWjY4s -> ⚠️ Media

buscar_password()
# 🔍 Introduce el sitio a buscar: git
# 1. github.com -> aB3kL9mZqR1w
```

---

## 📝 Notas

- `pedir_opcion` y `pedir_numero` implementan bucles de validación infinitos; la salida solo ocurre con entrada válida.
- `anadir_sitio` actualiza el objeto original en la lista por **referencia de identidad** (`p == seleccionada`), lo que asume unicidad del objeto en memoria.
- `buscar_password` filtra entradas con `sitio = None` para evitar errores al aplicar `.lower()`.
- El import de `core.generador` se realiza al final del archivo, después de las funciones de entrada; esto no afecta al comportamiento pero puede reorganizarse al inicio para mayor claridad.

---

## 🗂️ Módulo

| Atributo              | Valor          |
|-----------------------|----------------|
| Archivo               | `acciones.py`  |
| Paquete               | `src.ui`       |
| Lenguaje              | Python 3.x     |
| Dependencias externas | Ninguna        |