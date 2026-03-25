import string
import secrets

def construir_pantalla(config):
    opciones = {
        "mayus": string.ascii_uppercase,
        "minus": string.ascii_lowercase,
        "numeros": string.digits,
        "simbolos": string.punctuation
    }

    pool = ""
    required_chars = []

    for clave, activo in config.items():
        if activo:
            caracteres = opciones[clave]
            pool += caracteres
            required_chars.append(secrets.choice(caracteres))

    if not pool:
        raise ValueError("❌ Debes seleccionar al menos un tipo de carácter")

    return pool, required_chars


def generar_password(longitud, pantalla, required_chars):
    if longitud < len(required_chars):
        raise ValueError("La longitud es menor que los caracteres required_chars")
    
    restante = longitud - len(required_chars)

    password = required_chars + [
        secrets.choice(pantalla) for _ in range(restante)
    ]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def generar_passwords(config, longitud, cantidad):
    pantalla, required_chars_base = construir_pantalla(config)
    passwords = []

    for _ in range(cantidad):
        required_chars = required_chars_base.copy()
        password = generar_password(longitud, pantalla, required_chars)

        passwords.append({
            "sitio": None,
            "password": password
        })

    return passwords