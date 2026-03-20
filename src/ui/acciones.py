from core.storage import cargar_passwords, guardar_passwords
from core.evaluador import evaluar_password


def ver_passwords():
    passwords = cargar_passwords()

    if not passwords:
        print("\n❌ No hay contraseñas")
        return

    for i, item in enumerate(passwords, start=1):
        sitio = item["sitio"] or "Sin asignar"
        nivel = evaluar_password(item["password"])
        print(f"{i}. {sitio} → {item['password']} → {nivel}")