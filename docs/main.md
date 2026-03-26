# 🚀 main.py

Punto de entrada principal del gestor de contraseñas.

---

## 📋 Descripción

`main.py` es el archivo raíz de la aplicación. Inicializa el bucle principal del programa, renderiza el menú en cada iteración y despacha la ejecución a la función correspondiente de `src.ui.acciones` según la opción elegida por el usuario.

---

## 📁 Ubicación

```
MINI_PROYECTOS_PYTHON/
├── src/
│   ├── core/
│   │   ├── evaluador.py
│   │   ├── generador.py
│   │   └── storage.py
│   └── ui/
│       ├── acciones.py
│       └── menu.py
├── main.py
├── passwords.json
└── requirements.txt
```

---

## 📦 Dependencias

| Módulo           | Importación                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------|
| `ui.menu`        | `mostrar_menu`                                                                                    |
| `ui.acciones`    | `ver_passwords`, `anadir_sitio`, `eliminar_password`, `buscar_password`, `generar_y_guardar_passwords` |
| `sys`            | Diagnóstico del `sys.path` en arranque                                                            |
| `os`             | Diagnóstico del directorio de trabajo en arranque                                                 |

---

## ⚙️ API

### `main() -> None`

Ejecuta el bucle principal de la aplicación. En cada iteración muestra el menú, recoge la opción del usuario y llama a la función correspondiente. El bucle termina cuando el usuario elige la opción `6`.

**Tabla de despacho**

| Opción | Mensaje previo             | Función invocada                  |
|:------:|----------------------------|-----------------------------------|
| `1`    | `"Selecione opciones"`     | `generar_y_guardar_passwords()`   |
| `2`    | `"Mostrando contraseñas"`  | `ver_passwords()`                 |
| `3`    | `"Selecion de nombre"`     | `anadir_sitio()`                  |
| `4`    | `"Selecione opcion"`       | `eliminar_password()`             |
| `5`    | `"Introduzca nombre"`      | `buscar_password()`               |
| `6`    | `"Gracias"`                | `break` — termina el programa     |
| otro   | —                          | Imprime `"❌ Opción inválida"`    |

---

## 🔄 Flujo de Ejecución

```
python main.py
      │
      ├── DEBUG PATH  (sys.path)
      ├── MAIN DESDE  (os.getcwd())
      │
      └── main()
            │
            ▼
        ┌─────────────────────────┐
        │      mostrar_menu()     │  ◄──────────┐
        └────────────┬────────────┘             │
                     │                          │
              input("Elige una opción")         │
                     │                          │
           ┌─────────▼──────────┐               │
           │  Despacho por opción│               │
           └─────────┬──────────┘               │
                     │                          │
        ┌────────────▼────────────┐             │
        │   Ejecutar acción       │─────────────┘
        │   (o break si op.6)     │
        └─────────────────────────┘
```

---

## 🚀 Ejecución

Ejecutar siempre desde la **raíz del proyecto** para que las rutas relativas de `passwords.json` y los imports funcionen correctamente:

```bash
# Desde MINI_PROYECTOS_PYTHON/
python main.py
```

> ⚠️ Ejecutar desde otro directorio puede provocar errores de `ModuleNotFoundError` o que `passwords.json` se cree en una ubicación inesperada.

---

## 📝 Notas

- Las líneas `print("DEBUG PATH:", sys.path)` y `print("MAIN DESDE:", os.getcwd())` son **trazas de diagnóstico**. Se recomienda eliminarlas o sustituirlas por un logger antes de pasar a producción.
- El bloque `if __name__ == "__main__"` garantiza que `main()` solo se ejecuta cuando el archivo es invocado directamente, no cuando es importado como módulo.
- La entrada del usuario se normaliza con `.strip()` para evitar fallos por espacios accidentales, aunque no se convierte a entero, lo que hace el control de flujo robusto frente a entradas no numéricas.

---

## 🗂️ Archivo

| Atributo              | Valor        |
|-----------------------|--------------|
| Archivo               | `main.py`    |
| Nivel                 | Raíz         |
| Lenguaje              | Python 3.x   |
| Dependencias externas | Ninguna      |