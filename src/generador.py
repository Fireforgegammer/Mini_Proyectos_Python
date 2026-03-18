import string

def validar_password(usuario, password):
    if len(password) < 8 or len(password) > 128:
        return "❌ La contraseña debe tener entre 8 y 128 caracteres"

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


# 🔹 USO
usuario = input("Introduce tu usuario: ")

while True:
    password = input("Introduce tu contraseña (ENTER = usar una por defecto): ")

    # 👉 valor por defecto si no escribe nada
    if password == "":
        password = "Aa1!" * 4  # 16 caracteres seguros
        print("⚠️ Usando contraseña por defecto:", password)

    resultado = validar_password(usuario, password)
    print(resultado)

    if "✅" in resultado:
        break