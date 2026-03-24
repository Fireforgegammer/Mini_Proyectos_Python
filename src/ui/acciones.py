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
    passwords = cargar_passwords()

    # 1. Filtrar las que no tienen sitio
    sin_sitio = [p for p in passwords if p.get("sitio") is None]

    if not sin_sitio:
        print("❌ No hay contraseñas sin asignar")
        return

    # 2. Mostrar lista (como opción 2)
    print("\n🔑 Contraseñas sin asignar:")
    for i, p in enumerate(sin_sitio):
        print(f"{i+1}. Sin asignar -> {p['password']}")

    # 3. Elegir una
    try:
        eleccion = int(input("Elige una contraseña: ")) - 1
        seleccionada = sin_sitio[eleccion]
    except:
        print("❌ Selección inválida")
        return

    # 4. Pedir sitio
    sitio = input("🌐 Introduce el sitio: ")

    # 5. Actualizar la original
    for p in passwords:
        if p == seleccionada:
            p["sitio"] = sitio
            break

    # 6. Guardar cambios
    guardar_passwords(passwords)

    print("✅ Sitio añadido correctamente")
    
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
        
def pedir_configuracion_password():
    print("\n📋 ¿Qué caracteres quieres incluir?")
    
    incluir_minus = input("¿Minúsculas? (s/n): ").lower() == 's'
    incluir_mayus = input("¿Mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Símbolos? (s/n): ").lower() == 's'

    return {
        "minus": incluir_minus,
        "mayus": incluir_mayus,
        "numeros": incluir_numeros,
        "simbolos": incluir_simbolos
    }        