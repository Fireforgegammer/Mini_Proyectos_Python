import string
import secrets

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

    caracteres = ""

    for clave, activo in config.items():
        if activo:
            caracteres += opciones[clave]

    if not caracteres:
        raise ValueError("❌ Debes seleccionar al menos un tipo de carácter")

    return caracteres


def generar_password(longitud, caracteres):
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))


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


def main():
    print("🔐 GENERADOR DE CONTRASEÑAS PRO")

    config = obtener_configuracion()
    longitud = pedir_longitud()

    try:
        pool = construir_pool(config)
        password = generar_password(longitud, pool)
        nivel = evaluar_password(password)

        print("\n✅ Contraseña generada:", password)
        print("📊 Fortaleza:", nivel)

    except ValueError as e:
        print(e)


# ▶️ Ejecutar
main()