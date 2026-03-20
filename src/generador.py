import string
import secrets
import json

def obtener_configuracion():
    print("\n🔧 CONFIGURA TU CONTRASEÑA")

    config = {
        "mayus": input("¿Incluir mayúsculas? (s/n): ").lower() == "s",
        "minus": input("¿Incluir minúsculas? (s/n): ").lower() == "s",
        "numeros": input("¿Incluir números? (s/n): ").lower() == "s",
        "simbolos": input("¿Incluir símbolos? (s/n): ").lower() == "s"
    }

    return config


def construir_pool(config):
    opciones = {
        "mayus": string.ascii_uppercase,
        "minus": string.ascii_lowercase,
        "numeros": string.digits,
        "simbolos": string.punctuation
    }

    pool = ""              # 👈 ESTA ES LA VARIABLE CORRECTA
    obligatorios = []

    for clave, activo in config.items():
        if activo:
            caracteres = opciones[clave]   # 👈 se define aquí
            pool += caracteres             # 👈 usamos pool, NO caracteres
            obligatorios.append(secrets.choice(caracteres))

    if not pool:
        raise ValueError("❌ Debes seleccionar al menos un tipo de carácter")

    return pool, obligatorios


def generar_password(longitud, pool, obligatorios):
    restante = longitud - len(obligatorios)

    password = obligatorios + [
        secrets.choice(pool) for _ in range(restante)
    ]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


import string

def evaluar_password(password):
    puntuacion = 0

    if any(c in string.ascii_uppercase for c in password):
        puntuacion += 1
    if any(c in string.ascii_lowercase for c in password):
        puntuacion += 1
    if any(c in string.digits for c in password):
        puntuacion += 1
    if any(c in string.punctuation for c in password):
        puntuacion += 1

    if len(password) >= 12:
        puntuacion += 2
    elif len(password) >= 8:
        puntuacion += 1

    if puntuacion <= 2:
        return "❌ Débil"
    elif puntuacion == 3:
        return "⚠️ Media"
    elif puntuacion == 4:
        return "✅ Fuerte"
    else:
        return "🔥 Muy fuerte"
    
    
def pedir_longitud():
    while True:
        entrada = input("Longitud (8-128) [default 16]: ")

        if entrada == "":
            return 16

        try:
            longitud = int(entrada)
            if 8 <= longitud <= 128:
                return longitud
            else:
                print("❌ Debe estar entre 8 y 128")
        except ValueError:
            print("❌ Introduce un número válido")
            
            
def pedir_cantidad():
    while True:
        entrada = input("¿Cuántas contraseñas quieres generar? (1-10): ")

        try:
            cantidad = int(entrada)
            if 1 <= cantidad <= 10:
                return cantidad
            else:
                print("❌ Debe estar entre 1 y 10")
        except ValueError:
            print("❌ Introduce un número válido")


def main():
    print("🔐 GENERADOR DE CONTRASEÑAS PRO")

    config = obtener_configuracion()
    longitud = pedir_longitud()
    cantidad = pedir_cantidad()

    try:
        pool, _ = construir_pool(config)

        # 1. Generar
        passwords = []

        for _ in range(cantidad):
            _, obligatorios = construir_pool(config)
            password = generar_password(longitud, pool, obligatorios)

            passwords.append({
                "sitio": None,
                "password": password
            })

        # 💾 Guardar en JSON (BIEN COLOCADO)
        with open("passwords.json", "w") as f:
            json.dump(passwords, f, indent=4)

        print("\n💾 Contraseñas guardadas en passwords.json")

        # 2. Mostrar
        print("\n📋 CONTRASEÑAS GENERADAS:\n")
        for i, item in enumerate(passwords, start=1):
            nivel = evaluar_password(item["password"])
            print(f"{i}. {item['password']} → {nivel}")

    except ValueError as e:
        print(e)

# ▶️ Ejecutar
main()