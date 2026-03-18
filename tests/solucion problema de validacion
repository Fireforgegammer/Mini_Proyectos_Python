❌ ¿Qué pasa si el usuario escribe esto?
hola

Python intenta hacer:

int("hola")

💥 ERROR → el programa se rompe con algo como:

ValueError: invalid literal for int()
✅ ¿Qué significa “validar”?

👉 Significa comprobar que el usuario escribe algo correcto antes de usarlo

🛠️ Solución: usar try/except

Esto evita que el programa se rompa.

💻 Código con validación
while True:
    try:
        longitud = int(input("Longitud de la contraseña (3-12): "))

        if 3 <= longitud <= 12:
            break
        else:
            print("❌ Debe ser un número entre 3 y 12")

    except ValueError:
        print("❌ Debes introducir un número válido")
🧠 ¿Cómo funciona?

try → intenta ejecutar el código

except → si hay error, lo controla y muestra mensaje

🔁 Ejemplo real

Usuario escribe:

hola

👉 Resultado:

❌ Debes introducir un número válido

Usuario escribe:

20

👉 Resultado:

❌ Debe ser un número entre 3 y 12

Usuario escribe:

8

👉 ✅ válido → el programa sigue

🚀 Resultado

✔ Tu programa ya no se rompe
✔ Es más profesional
✔ Mejor experiencia de usuario