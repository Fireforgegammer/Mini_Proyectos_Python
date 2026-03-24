from core.storage import cargar_passwords, guardar_passwords
from core.evaluador import evaluar_password


def ver_passwords():
    print("DEBUG: dentro de la función")  # 👈 AÑADE ESTO

    passwords = cargar_passwords()
    print("DEBUG passwords:", passwords)  # 👈 Y ESTO

    if not passwords:
        print("\n❌ No hay contraseñas")
        return

    for i, item in enumerate(passwords, start=1):
        sitio = item["sitio"] or "Sin asignar"
        nivel = evaluar_password(item["password"])
        print(f"{i}. {sitio} -> {item['password']} -> {nivel
    }")
        
def anadir_sitio():
    sitio = input("🌐 Sitio: ")
    password = input("🔑 Contraseña: ")

    nueva = {
        "sitio": sitio,
        "password": password
    }

    guardar_passwords([nueva])
    print("✅ Guardado correctamente")
    
def eliminar_password():
    print("🗑️ Eliminar password (pendiente implementar)")
    
def buscar_password():
    passwords = cargar_passwords()

    if not passwords:
        print("\n❌ No hay contraseñas")
        return

    busqueda = input("🔍 Introduce el sitio a buscar: ").lower()

    encontrados = [
        p for p in passwords
        if busqueda in p["sitio"].lower()
    ]

    if not encontrados:
        print("❌ No se encontraron resultados")
        return

    for i, item in enumerate(encontrados, start=1):
        print(f"{i}. {item['sitio']} -> {item['password']}")