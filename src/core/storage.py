import json

def cargar_passwords(archivo="passwords.json"):
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_passwords(passwords, archivo="passwords.json"):
    existentes = cargar_passwords(archivo)
    existentes.extend(passwords)

    with open(archivo, "w") as f:
        json.dump(existentes, f, indent=4)