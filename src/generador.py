import string
import secrets

def generar_password(usuario, longitud):
    if longitud < 3 or longitud > 12:
        raise ValueError("La longitud debe estar entre 3 y 12 caracteres")

    while True:
        # 1. Caracteres obligatorios
        mayuscula = secrets.choice(string.ascii_uppercase)
        minuscula = secrets.choice(string.ascii_lowercase)
        numero = secrets.choice(string.digits)
        simbolo = secrets.choice(string.punctuation)

        # 2. Todos los caracteres posibles
        todos = string.ascii_letters + string.digits + string.punctuation

        # 3. Rellenar
        restantes = [secrets.choice(todos) for _ in range(longitud - 4)]

        # 4. Mezclar
        contrasena_lista = [mayuscula, minuscula, numero, simbolo] + restantes
        secrets.SystemRandom().shuffle(contrasena_lista)

        contrasena = ''.join(contrasena_lista)

        # 5. Validar que no sea igual al usuario
        if usuario.lower() not in contrasena.lower():
            return contrasena


# 🔹 Uso
import string

def validar_password(usuario, password):
    if len(password) < 4 or len(password) > 12:
        return "❌ La contraseña debe tener entre 4 y 12 caracteres"

    if usuario.lower() in password.lower():
        return "❌ La contraseña no puede contener el usuario"

    if not any(c in string.ascii_uppercase for c in password):
        return "❌ Falta una letra mayúscula"

    if not any(c in string.ascii_lowercase for c in password):
        return "❌ Falta una letra minúscula"

    if not any(c in string.digits for c in password):
        return "❌ Falta un número"

    if not any(c in string.punctuation for c in password):
        return "❌ Falta un símbolo"

    return "✅ Contraseña válida"


# 🔹 NUEVO USO
usuario = input("Introduce tu usuario: ")

while True:
    password = input("Introduce tu contraseña: ")
    resultado = validar_password(usuario, password)

    print(resultado)

    if "✅" in resultado:
        break