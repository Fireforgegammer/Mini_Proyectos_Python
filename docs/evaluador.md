# 🔐 src.core.evaluador

Módulo de evaluación de seguridad de contraseñas para el paquete `src.core`.

---

## 📋 Descripción

`evaluador.py` expone una única función pública que analiza una contraseña y devuelve un nivel de seguridad basado en un sistema de puntuación acumulativa. Evalúa composición de caracteres y longitud de forma independiente.

---

## 📁 Ubicación

```
src/
└── core/
    └── evaluador.py
```

---

## 📦 Dependencias

Solo utiliza la biblioteca estándar de Python — **sin dependencias externas**.

| Módulo   | Uso                                                   |
|----------|-------------------------------------------------------|
| `string` | Constantes de caracteres: mayúsculas, minúsculas, dígitos y puntuación |

---

## ⚙️ API

### `evaluar_password(password: str) -> str`

Evalúa la fortaleza de una contraseña y retorna una etiqueta con indicador visual.

**Parámetros**

| Nombre     | Tipo  | Descripción              |
|------------|-------|--------------------------|
| `password` | `str` | La contraseña a evaluar. |

**Retorno**

| Tipo  | Valores posibles                                          |
|-------|-----------------------------------------------------------|
| `str` | `"❌ Débil"`, `"⚠️ Media"`, `"✅ Fuerte"`, `"🔥 Muy fuerte"` |

---

## 🧮 Sistema de Puntuación

| Criterio                          | Puntos |
|-----------------------------------|:------:|
| Contiene letras mayúsculas        | +1     |
| Contiene letras minúsculas        | +1     |
| Contiene dígitos numéricos        | +1     |
| Contiene caracteres especiales    | +1     |
| Longitud ≥ 12 caracteres          | +2     |
| Longitud ≥ 8 y < 12 caracteres    | +1     |

> ⚠️ Los criterios de longitud son mutuamente excluyentes: solo se aplica el de mayor puntuación.

---

## 🎯 Niveles de Resultado

| Resultado       | Puntuación | Descripción                                    |
|-----------------|:----------:|------------------------------------------------|
| ❌ Débil        | ≤ 2        | Contraseña fácilmente vulnerable.              |
| ⚠️ Media        | = 3        | Cumple criterios básicos, mejorable.           |
| ✅ Fuerte       | = 4        | Contraseña segura para uso general.            |
| 🔥 Muy fuerte   | ≥ 5        | Cumple todos los criterios de seguridad.       |

---

## 🚀 Ejemplos de Uso

```python
from src.core.evaluador import evaluar_password

print(evaluar_password("abc"))           # ❌ Débil
print(evaluar_password("Abc12345"))      # ⚠️ Media
print(evaluar_password("Abc1234!"))      # ✅ Fuerte
print(evaluar_password("Abc123456!@#"))  # 🔥 Muy fuerte
```

---

## 📝 Notas

- La función **no valida el tipo de entrada**; se recomienda verificar que `password` sea `str` en capas superiores.
- No realiza comprobación contra diccionarios de contraseñas comunes (*dictionary attack check*).
- La función es **pura** (sin efectos secundarios), apta para uso en contextos multihilo.

---

## 🗂️ Módulo

| Atributo    | Valor             |
|-------------|-------------------|
| Archivo     | `evaluador.py`    |
| Paquete     | `src.core`        |
| Lenguaje    | Python 3.x        |
| Dependencias externas | Ninguna |