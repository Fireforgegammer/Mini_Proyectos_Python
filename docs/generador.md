# ⚙️ src.core.generador

Módulo de generación segura de contraseñas para el paquete `src.core`.

---

## 📋 Descripción

`generador.py` proporciona las funciones necesarias para construir y generar contraseñas criptográficamente seguras. Utiliza el módulo `secrets` de Python para garantizar aleatoriedad de calidad criptográfica, y permite configurar el conjunto de caracteres permitidos así como garantizar la presencia de al menos un carácter de cada tipo activado.

---

## 📁 Ubicación

```
src/
└── core/
    └── generador.py
```

---

## 📦 Dependencias

Solo utiliza la biblioteca estándar de Python — **sin dependencias externas**.

| Módulo    | Uso                                                          |
|-----------|--------------------------------------------------------------|
| `string`  | Constantes de caracteres: mayúsculas, minúsculas, dígitos y puntuación |
| `secrets` | Selección y mezcla aleatoria criptográficamente segura       |

---

## ⚙️ API

### `construir_pantalla(config: dict) -> tuple[str, list]`

Construye el pool de caracteres disponibles y garantiza al menos un carácter obligatorio por cada tipo activado.

**Parámetros**

| Nombre   | Tipo   | Descripción                                                                 |
|----------|--------|-----------------------------------------------------------------------------|
| `config` | `dict` | Diccionario con claves `"mayus"`, `"minus"`, `"numeros"`, `"simbolos"` y valores `bool`. |

**Retorno**

| Tipo              | Descripción                                                                    |
|-------------------|--------------------------------------------------------------------------------|
| `tuple[str, list]`| `(pool, required_chars)` — el pool completo de caracteres y la lista de caracteres obligatorios. |

**Excepciones**

| Excepción      | Condición                                              |
|----------------|--------------------------------------------------------|
| `ValueError`   | Si ninguna clave de `config` está activa (`True`).     |

---

### `generar_password(longitud: int, pantalla: str, required_chars: list) -> str`

Genera una única contraseña aleatoria respetando los caracteres obligatorios y la longitud indicada.

**Parámetros**

| Nombre          | Tipo   | Descripción                                               |
|-----------------|--------|-----------------------------------------------------------|
| `longitud`      | `int`  | Longitud total de la contraseña generada.                 |
| `pantalla`      | `str`  | Pool completo de caracteres disponibles.                  |
| `required_chars`| `list` | Lista de caracteres que deben aparecer en la contraseña.  |

**Retorno**

| Tipo  | Descripción                        |
|-------|------------------------------------|
| `str` | Contraseña generada aleatoriamente. |

**Excepciones**

| Excepción    | Condición                                                          |
|--------------|--------------------------------------------------------------------|
| `ValueError` | Si `longitud` es menor que el número de caracteres obligatorios.   |

---

### `generar_passwords(config: dict, longitud: int, cantidad: int) -> list[dict]`

Genera un lote de contraseñas a partir de una configuración, longitud y cantidad indicadas.

**Parámetros**

| Nombre     | Tipo   | Descripción                                             |
|------------|--------|---------------------------------------------------------|
| `config`   | `dict` | Configuración de tipos de caracteres (ver `construir_pantalla`). |
| `longitud` | `int`  | Longitud de cada contraseña generada.                   |
| `cantidad` | `int`  | Número de contraseñas a generar.                        |

**Retorno**

| Tipo          | Descripción                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `list[dict]`  | Lista de diccionarios con las claves `"sitio"` (`None`) y `"password"` (`str`). |

---

## 🔄 Flujo Interno

```
generar_passwords(config, longitud, cantidad)
        │
        ▼
construir_pantalla(config)
  ├── Construye pool de caracteres
  └── Selecciona required_chars (uno por tipo activo)
        │
        ▼
generar_password(longitud, pantalla, required_chars)  ← se ejecuta `cantidad` veces
  ├── Completa con caracteres aleatorios del pool
  ├── Mezcla con secrets.SystemRandom().shuffle()
  └── Retorna contraseña como str
```

---

## 🚀 Ejemplos de Uso

```python
from src.core.generador import generar_passwords

config = {
    "mayus":    True,
    "minus":    True,
    "numeros":  True,
    "simbolos": False
}

resultados = generar_passwords(config, longitud=12, cantidad=3)

for r in resultados:
    print(r["password"])
# Ejemplo de salida:
# aB3kL9mZqR1w
# X7nPc2tWjY4s
# Qm8vR3eLdK5n
```

---

## 📝 Notas

- Cada contraseña generada **garantiza al menos un carácter** de cada tipo activado en `config`, gracias a `required_chars`.
- El campo `"sitio"` del resultado se devuelve siempre como `None`; se espera que sea asignado por capas superiores (p. ej. `src.core.storage`).
- Se usa `secrets.SystemRandom().shuffle()` en lugar de `random.shuffle()` para asegurar aleatoriedad criptográfica en la mezcla final.
- El pool se reconstruye una sola vez por llamada a `generar_passwords`, reutilizándose para todas las contraseñas del lote.

---

## 🗂️ Módulo

| Atributo               | Valor             |
|------------------------|-------------------|
| Archivo                | `generador.py`    |
| Paquete                | `src.core`        |
| Lenguaje               | Python 3.x        |
| Dependencias externas  | Ninguna           |