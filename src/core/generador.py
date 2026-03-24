import string
import secrets

def construir_pantalla(config):
    opciones = {
        "mayus": string.ascii_uppercase,
        "minus": string.ascii_lowercase,
        "numeros": string.digits,
        "simbolos": string.punctuation
    }

    pantalla = ""
    obligatorios = []

    for clave, activo in config.items():
        if activo:
            caracteres = opciones[clave]
            pantalla += caracteres
            obligatorios.append(secrets.choice(caracteres))

    if not pantalla:
        raise ValueError("❌ Debes seleccionar al menos un tipo de carácter")

    return pantalla, obligatorios


def generar_password(longitud, pantalla, obligatorios):
    if longitud < len(obligatorios):
        raise ValueError("La longitud es menor que los caracteres obligatorios")
    
    restante = longitud - len(obligatorios)

    password = obligatorios + [
        secrets.choice(pantalla) for _ in range(restante)
    ]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def generar_passwords(config, longitud, cantidad):
    pantalla, obligatorios_base = construir_pantalla(config)
    passwords = []

    for _ in range(cantidad):
        obligatorios = obligatorios_base.copy()
        password = generar_password(longitud, pantalla, obligatorios)

        passwords.append({
            "sitio": None,
            "password": password
        })

    return passwords