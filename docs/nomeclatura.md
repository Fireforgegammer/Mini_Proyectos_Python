# 📖 Nomenclatura del Proyecto

Convenciones de nombres aplicadas en `MINI_PROYECTOS_PYTHON` para variables, funciones, parámetros y archivos.

---

## 🐍 Convenciones Generales

- Se sigue **PEP 8** como estándar base de nomenclatura Python.
- Todos los identificadores están en **español**, a excepción de términos técnicos consolidados (`pool`, `config`, `shuffle`...).
- Se usa **snake_case** para variables, funciones y parámetros.
- Se usa **UPPER_CASE** para constantes (si aplica en el futuro).

---

## 📦 Módulos y Archivos

| Archivo          | Criterio de nombre                                              |
|------------------|-----------------------------------------------------------------|
| `evaluador.py`   | Sustantivo agente — describe qué hace el módulo                |
| `generador.py`   | Sustantivo agente — describe qué hace el módulo                |
| `storage.py`     | Término técnico en inglés — convención estándar de persistencia|
| `acciones.py`    | Sustantivo plural — agrupa todas las acciones de usuario       |
| `menu.py`        | Sustantivo funcional — representa el componente de menú        |
| `main.py`        | Punto de entrada estándar Python                               |
| `passwords.json` | Sustantivo plural en inglés — archivo de datos persistidos     |

---

## 🔤 Variables

| Variable          | Módulo         | Tipo    | Descripción                                              |
|-------------------|----------------|---------|----------------------------------------------------------|
| `password`        | global         | `str`   | Una contraseña individual como cadena de texto           |
| `passwords`       | global         | `list`  | Lista de diccionarios `{sitio, password}`                |
| `puntuacion`      | `evaluador`    | `int`   | Puntuación acumulada para clasificar la contraseña       |
| `pool`            | `generador`    | `str`   | Cadena con todos los caracteres disponibles para generar |
| `required_chars`  | `generador`    | `list`  | Caracteres obligatorios (uno por tipo activo)            |
| `restante`        | `generador`    | `int`   | Caracteres adicionales a rellenar tras los obligatorios  |
| `opciones`        | `generador`    | `dict`  | Mapa de clave de config a su conjunto de caracteres      |
| `config`          | `generador`    | `dict`  | Configuración de tipos de caracteres activos             |
| `sin_sitio`       | `acciones`     | `list`  | Subconjunto de contraseñas sin sitio asignado            |
| `encontrados`     | `acciones`     | `list`  | Resultados filtrados de una búsqueda por sitio           |
| `eleccion`        | `acciones`     | `int`   | Índice numérico elegido por el usuario (base 0)          |
| `seleccionada`    | `acciones`     | `dict`  | Entrada de contraseña seleccionada por el usuario        |
| `eliminada`       | `acciones`     | `dict`  | Entrada de contraseña eliminada de la lista              |
| `busqueda`        | `acciones`     | `str`   | Término de búsqueda introducido por el usuario           |
| `sitio`           | `acciones`     | `str`   | Nombre del sitio asociado a una contraseña               |
| `opcion`          | `main`         | `str`   | Opción de menú introducida por el usuario                |
| `archivo`         | `storage`      | `str`   | Ruta al archivo JSON de persistencia                     |

---

## 🔧 Funciones

Las funciones siguen el patrón **verbo + sustantivo** en español, describiendo la acción que realizan.

| Función                        | Módulo       | Patrón              |
|--------------------------------|--------------|---------------------|
| `evaluar_password`             | `evaluador`  | verbo + sustantivo  |
| `construir_pantalla`           | `generador`  | verbo + sustantivo  |
| `generar_password`             | `generador`  | verbo + sustantivo  |
| `generar_passwords`            | `generador`  | verbo + sustantivo  |
| `cargar_passwords`             | `storage`    | verbo + sustantivo  |
| `guardar_passwords`            | `storage`    | verbo + sustantivo  |
| `mostrar_passwords`            | `acciones`   | verbo + sustantivo  |
| `ver_passwords`                | `acciones`   | verbo + sustantivo  |
| `anadir_sitio`                 | `acciones`   | verbo + sustantivo  |
| `eliminar_password`            | `acciones`   | verbo + sustantivo  |
| `buscar_password`              | `acciones`   | verbo + sustantivo  |
| `pedir_opcion`                 | `acciones`   | verbo + sustantivo  |
| `pedir_numero`                 | `acciones`   | verbo + sustantivo  |
| `pedir_configuracion_password` | `acciones`   | verbo + sustantivo  |
| `generar_y_guardar_passwords`  | `acciones`   | verbo + conj + verbo|
| `mostrar_menu`                 | `menu`       | verbo + sustantivo  |
| `main`                         | `main`       | estándar Python     |

---

## 🗂️ Parámetros

| Parámetro       | Tipo    | Convención                                              |
|-----------------|---------|---------------------------------------------------------|
| `password`      | `str`   | Singular — siempre una sola contraseña                  |
| `passwords`     | `list`  | Plural — siempre una lista de contraseñas               |
| `config`        | `dict`  | Abreviatura técnica — configuración de generación       |
| `longitud`      | `int`   | Sustantivo descriptivo en español                       |
| `cantidad`      | `int`   | Sustantivo descriptivo en español                       |
| `pantalla`      | `str`   | Nombre interno del pool de caracteres disponibles       |
| `archivo`       | `str`   | Ruta al archivo de persistencia; tiene valor por defecto|
| `mensaje`       | `str`   | Texto de prompt para funciones de entrada de datos      |
| `minimo`        | `int`   | Valor mínimo aceptado en `pedir_numero`                 |

---

## 📁 Claves de Diccionarios

### Objeto contraseña (`dict`)

| Clave      | Tipo         | Descripción                                          |
|------------|--------------|------------------------------------------------------|
| `sitio`    | `str / None` | Nombre del sitio asociado. `None` si no está asignado|
| `password` | `str`        | La contraseña generada                               |

### Objeto config (`dict`)

| Clave      | Tipo   | Descripción                              |
|------------|--------|------------------------------------------|
| `mayus`    | `bool` | Incluir letras mayúsculas                |
| `minus`    | `bool` | Incluir letras minúsculas                |
| `numeros`  | `bool` | Incluir dígitos numéricos                |
| `simbolos` | `bool` | Incluir caracteres especiales            |

---

## 🔄 Historial de Cambios

| Versión | Cambio                                      |
|---------|---------------------------------------------|
| v0.1    | `p` renombrado a `item` en bucles de lista  |

---