# 🖥️ src.ui.menu

Módulo de interfaz de menú principal para el paquete `src.ui`.

---

## 📋 Descripción

`menu.py` es responsable de renderizar el menú principal de la aplicación en consola. Es el punto de entrada visual del gestor de contraseñas, presentando al usuario las opciones disponibles de forma clara y estructurada.

---

## 📁 Ubicación

```
src/
└── ui/
    └── menu.py
```

---

## 📦 Dependencias

**Ninguna.** El módulo no importa ningún paquete externo ni interno — solo utiliza `print` de la biblioteca estándar de Python.

---

## ⚙️ API

### `mostrar_menu() -> None`

Imprime por consola el menú principal del gestor de contraseñas con todas las opciones disponibles.

**Parámetros:** Ninguno.

**Retorno:** `None`.

**Salida en consola:**

```
🔥 Elegir Opcion 🔥

🔐 GESTOR DE CONTRASEÑAS
1. Generar contraseñas
2. Ver contraseñas
3. Añadir sitio
4. Eliminar contraseña
5. Buscar contraseña
6. Salir
```

---

## 🗺️ Mapa de Opciones

| Opción | Descripción              | Función asociada (`src.ui.acciones`)    |
|:------:|--------------------------|-----------------------------------------|
| `1`    | Generar contraseñas      | `generar_y_guardar_passwords()`         |
| `2`    | Ver contraseñas          | `ver_passwords()`                       |
| `3`    | Añadir sitio             | `anadir_sitio()`                        |
| `4`    | Eliminar contraseña      | `eliminar_password()`                   |
| `5`    | Buscar contraseña        | `buscar_password()`                     |
| `6`    | Salir                    | Termina el bucle principal en `main.py` |

---

## 🚀 Ejemplo de Uso

```python
from src.ui.menu import mostrar_menu

mostrar_menu()
```

En la práctica, es llamada desde el bucle principal de `main.py` al inicio de cada iteración:

```python
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    # ...
```

---

## 📝 Notas

- La función es **puramente de presentación**: no recoge input ni ejecuta lógica. La gestión de la opción elegida es responsabilidad de `main.py`.
- Para añadir nuevas opciones al menú, basta con añadir un `print` adicional aquí y registrar el caso correspondiente en el bloque de control de `main.py`.

---

## 🗂️ Módulo

| Atributo              | Valor       |
|-----------------------|-------------|
| Archivo               | `menu.py`   |
| Paquete               | `src.ui`    |
| Lenguaje              | Python 3.x  |
| Dependencias externas | Ninguna     |