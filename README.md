# 🐍 Mini Proyectos Python

> **Repositorio de proyectos prácticos en Python, pensados para aprender de forma clara y progresiva.**
> 🎯 Para cualquier edad, cualquier nivel, cualquier actitud. ¡Lo importante es querer aprender!

---

## 📋 Tabla de Contenidos

* [🧭 Sobre este repositorio](#-sobre-este-repositorio)
* [📦 Proyectos disponibles](#-proyectos-disponibles)

  * [🔐 Generador de Contraseñas](#-generador-de-contraseñas)
* [🚀 Cómo usar este repositorio](#-cómo-usar-este-repositorio)
* [🛠️ Requisitos](#️-requisitos)
* [📜 Licencia](#-licencia)
* [👤 Autor](#-autor)

---

## 🧭 Sobre este repositorio

Este repositorio reúne **mini proyectos en Python** construidos paso a paso.

* ✅ Nivel: Principiante → Intermedio
* 🎓 Objetivo: Aprender creando proyectos reales
* 🔨 Enfoque: Evolución progresiva + buenas prácticas

---

## 📦 Proyectos disponibles

---

## 🔐 Generador de Contraseñas

> 📁 `/generador_contraseñas`

Generador de contraseñas seguras usando `secrets`, con validación avanzada y arquitectura modular.

---

### 🚀 Características

| Característica         | Detalle               |
| ---------------------- | --------------------- |
| 🔡 Letras mayúsculas   | Opcional              |
| 🔠 Letras minúsculas   | Opcional              |
| 🔢 Números             | Garantizado           |
| ⚡ Símbolos             | Garantizado           |
| 📏 Longitud            | 8–128 (def. 16)       |
| 🧍 Seguridad           | Evita usar el usuario |
| 💪 Fortaleza           | Débil → Muy fuerte    |
| 🔁 Generación múltiple | 1–10                  |

---

### 🧱 Arquitectura del proyecto

```
generador_contraseñas/
├── main.py
├── core/
│   ├── generador.py
│   ├── evaluador.py
│   └── storage.py
├── ui/
│   ├── menu.py
│   └── acciones.py
```

Separación clara:

* `core` → lógica
* `ui` → interacción
* `main` → ejecución

---

## 🗺️ Diagramas de flujo

---

### 🔄 Flujo general del programa

```
┌────────────────────────────┐
│        INICIO              │
└────────────┬───────────────┘
             │
             ▼
     Pedir usuario
             │
             ▼
   ¿Cantidad (1-10)?
   Validar entrada
             │
             ▼
   Configurar parámetros
             │
             ▼
        ┌───────────┐
        │   BUCLE   │
        └────┬──────┘
             │
             ▼
   Generar contraseña
             │
             ▼
   Evaluar fortaleza
             │
             ▼
   Mostrar resultado
             │
     ¿Quedan más?
        │       │
       Sí      No
        │       │
        └───►  FIN
```

---

### 🔐 Generación de contraseña

```
┌────────────────────────────┐
│ generar_password()         │
└────────────┬───────────────┘
             │
             ▼
 Forzar caracteres obligatorios
             │
             ▼
 Rellenar con aleatorios
             │
             ▼
 Mezclar (shuffle)
             │
             ▼
 ¿Contiene usuario?
        │       │
       Sí      No
        │       │
   Regenerar   ▼
        │   Devolver pwd
```

---

### 💪 Evaluador de fortaleza

```
Inicializar puntuación = 0

Longitud:
≥8  → +1
≥12 → +1
≥16 → +1

Tipos:
Mayúsculas → +1
Minúsculas → +1
Números    → +1
Símbolos   → +1

Resultado:
0-2  → Débil
3-4  → Media
5-6  → Fuerte
7+   → Muy fuerte
```

---

### 🧠 ¿Por qué `secrets`?

```
random  → predecible ❌
secrets → seguro ✔️
```

---

### 📝 Evolución del proyecto

| Paso   | Mejora                |
| ------ | --------------------- |
| 1️⃣    | Generación básica     |
| 2️⃣    | Longitud configurable |
| 3️⃣    | Tipos obligatorios    |
| 4️⃣    | Validaciones          |
| 5️⃣    | Seguridad usuario     |
| 6️⃣    | Validación robusta    |
| 7️⃣    | Longitud 8–128        |
| 8️⃣    | Configuración         |
| 9️⃣    | Evaluador             |
| 🔟     | Generación múltiple   |
| 1️⃣1️⃣ | Modularización        |

---

### 💻 Ejemplo

```bash
$ python main.py

Usuario: fireforgegammer
Cantidad: 3

1. K!9vQr#mXwLp3T@n → Muy fuerte
2. aZ$4nWqL!2yBpR%v → Muy fuerte
3. Jm@8XkQr!nTv#2Yw → Muy fuerte
```

---

## 🚀 Uso

```
git clone https://github.com/Fireforgegammer/Mini_Proyectos_Python.git
```
```
cd Mini_Proyectos_Python/generador_contraseñas
```
```
python main.py
```

---

## 🛠️ Requisitos

* Python 3.6+
* Sin librerías externas

---

## 📜 Licencia

MIT

---

## 👤 Autor

**Fireforgegammer**
https://github.com/Fireforgegammer

---

<div align="center">

⭐ Dale estrella si te ayuda ⭐

</div>
