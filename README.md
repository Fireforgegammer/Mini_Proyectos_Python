 # 🔐 Generador de Contraseñas en Python

Un pequeño proyecto en Python que genera contraseñas seguras personalizables.

# 🚀 Características

Generación de contraseñas aleatorias

Longitud configurable

Inclusión de:

Letras mayúsculas

Letras minúsculas

Números

Símbolos

# ¿Por qué usar secrets y no random?

👉 Respuesta clara:

random NO es seguro → se puede predecir (está pensado para juegos/simulaciones)

secrets SÍ es seguro → usa generación criptográfica (ideal para contraseñas)

🔐 En resumen:

random → rápido pero predecible

secrets → seguro e impredecible ✔️

# Le eh pedido que me garantice que haya al menos 1 mayuscula, 1 numero y 1 simbolo
La idea es:

Forzar esos caracteres obligatorios

Completar el resto aleatoriamente

Mezclar todo para que no sea predecible
¿Por qué esto funciona?
✔ Primero aseguramos los obligatorios
✔ Luego rellenamos el resto
✔ Finalmente mezclamos → evita patrones como: A3$xxxxxxx

# Le eh pedido que la contraseña tenga una longitud minima de 3 caracteres y maxima de 12 y que no pueda usarse el usuario como password.
# Tambien vamos a evitar que la contraseña contenga el usuario y vamos a añadir una validacion para que el usuario no rompa el programa al meter texto en vez de un numero
# siguiente paso fue evitar que la contraseña contenga partes del usuario