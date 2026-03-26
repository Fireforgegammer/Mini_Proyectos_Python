# 💾 src.core.storage

Módulo de persistencia de contraseñas para el paquete `src.core`.

---

## 📋 Descripción

`storage.py` gestiona la lectura y escritura de contraseñas en un archivo JSON local. Actúa como capa de persistencia del proyecto, proporcionando una interfaz simple y tolerante a fallos para cargar y guardar el listado de contraseñas.

---

## 📁 Ubicación

```
src/
└── core/
    └── storage.py
```

---

## 📦 Dependencias

Solo utiliza la biblioteca estándar de Python — **sin dependencias externas**.

| Módulo | Uso                                      |
|--------|------------------------------------------|
| `json` | Serialización y deserialización de datos |

---

## ⚙️ API

### `cargar_passwords(archivo: str = "passwords.json") -> list`

Lee el archivo JSON indicado y retorna la lista de contraseñas almacenadas. Si el archivo no existe o está corrupto, retorna una lista vacía sin lanzar excepción.

**Parámetros**

| Nombre    | Tipo  | Valor por defecto   | Descripción                           |
|-----------|-------|---------------------|---------------------------------------|
| `archivo` | `str` | `"passwords.json"`  | Ruta al archivo JSON de persistencia. |

**Retorno**

| Tipo   | Descripción                                                                    |
|--------|--------------------------------------------------------------------------------|
| `list` | Lista de diccionarios con las contraseñas almacenadas, o `[]` si no hay datos. |

**Comportamiento ante errores**

| Excepción capturada    | Comportamiento                      |
|------------------------|-------------------------------------|
| `FileNotFoundError`    | Retorna `[]` sin propagar el error. |
| `json.JSONDecodeError` | Retorna `[]` sin propagar el error. |

---

### `guardar_passwords(passwords: list, archivo: str = "passwords.json") -> None`

Serializa y escribe la lista de contraseñas en el archivo JSON indicado, sobreescribiendo el contenido existente.

**Parámetros**

| Nombre      | Tipo   | Valor por defecto  | Descripción                        |
|-------------|--------|--------------------|------------------------------------|
| `passwords` | `list` | —                  | Lista de diccionarios a persistir. |
| `archivo`   | `str`  | `"passwords.json"` | Ruta al archivo JSON de destino.   |

**Retorno**

| Tipo   | Descripción           |
|--------|-----------------------|
| `None` | Sin valor de retorno. |

> ⚠️ Si el archivo no existe, se crea automáticamente. Si ya existe, su contenido es **sobreescrito completamente**.

---

## 📄 Formato del Archivo JSON

El archivo generado sigue la estructura producida por `src.core.generador`:

```json
[
    {
        "sitio": "github.com",
        "password": "aB3kL9mZqR1w"
    },
    {
        "sitio": null,
        "password": "X7nPc2tWjY4s"
    }
]
```

---

## 🚀 Ejemplos de Uso

```python
from src.core.storage import cargar_passwords, guardar_passwords

# Cargar contraseñas existentes
passwords = cargar_passwords()                       # usa "passwords.json" por defecto
passwords = cargar_passwords("mis_passwords.json")   # archivo personalizado

# Añadir una nueva entrada y guardar
passwords.append({"sitio": "github.com", "password": "aB3kL9mZqR1w"})
guardar_passwords(passwords)

# Flujo típico combinado con generador
from src.core.generador import generar_passwords

config = {"mayus": True, "minus": True, "numeros": True, "simbolos": False}
nuevas = generar_passwords(config, longitud=12, cantidad=2)

existentes = cargar_passwords()
existentes.extend(nuevas)
guardar_passwords(existentes)
```

---

## 📝 Notas

- `cargar_passwords` es **tolerante a fallos**: nunca lanza excepción en condiciones normales de uso, facilitando un arranque limpio en primera ejecución.
- `guardar_passwords` **sobreescribe** el archivo completo en cada llamada; no hace escritura incremental. Se recomienda cargar, modificar y volver a guardar la lista completa.
- El archivo JSON se guarda con `indent=4` para facilitar la legibilidad en texto plano.
- La ruta del archivo es relativa al directorio de ejecución del proceso; se recomienda ejecutar desde la raíz del proyecto.

---

## 🗂️ Módulo

| Atributo              | Valor        |
|-----------------------|--------------|
| Archivo               | `storage.py` |
| Paquete               | `src.core`   |
| Lenguaje              | Python 3.x   |
| Dependencias externas | Ninguna      |