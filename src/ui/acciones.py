from core.storage import cargar_passwords, guardar_passwords
from core.evaluador import evaluar_password

def mostrar_passwords(passwords):
    for i, item in enumerate(passwords, start=1):
        sitio = item["sitio"] or "Sin asignar"
        print(f"{i}. {sitio} -> {item['password']}")
def ver_passwords():
    passwords = cargar_passwords()

    if not passwords:
        print("\n❌ No hay contraseñas")
        return

    for i, item in enumerate(passwords, start=1):
        sitio = item["sitio"] or "Sin asignar"
        nivel = evaluar_password(item["password"])
        print(f"{i}. {sitio} -> {item['password']} -> {nivel}")
        
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
    except (ValueError, IndexError):
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
    passwords = cargar_passwords()

    if not passwords:
        print("❌ No hay contraseñas para eliminar")
        return

    # 1. Mostrar lista
    print("\n🗑️ Lista de contraseñas:")
    mostrar_passwords(passwords)

    # 2. Elegir
    try:
        eleccion = int(input("Elige el número a eliminar: ")) - 1

        if eleccion < 0 or eleccion >= len(passwords):
            print("❌ Selección fuera de rango")
            return

    except ValueError:
        print("❌ Debes introducir un número")
        return

    # 3. Eliminar
    eliminada = passwords.pop(eleccion)

    # 4. Guardar
    guardar_passwords(passwords)

    # 5. Confirmación
    sitio = eliminada["sitio"] or "Sin asignar"
    print(f"✅ Eliminada: {sitio} -> {eliminada['password']}")
    
def buscar_password():
    passwords = cargar_passwords()

    if not passwords:
        print("\n❌ No hay contraseñas")
        return

    busqueda = input("🔍 Introduce el sitio a buscar: ").strip().lower()

    encontrados = [
        p for p in passwords
        if p["sitio"] and busqueda in p["sitio"].lower()
    ]

    if not encontrados:
        print("❌ No se encontraron resultados")
        return

    for i, item in enumerate(encontrados, start=1):
        print(f"{i}. {item['sitio']} -> {item['password']}")
        
def pedir_opcion(mensaje):
    while True:
        opcion = input(mensaje).strip().lower()

        if opcion in ("s", "n"):
            return opcion == "s"
        else:
            print("❌ Solo puedes introducir 's' o 'n'")
            
def pedir_numero(mensaje, minimo=1):
    while True:
        valor = input(mensaje).strip()

        if valor.isdigit():
            numero = int(valor)
            if numero >= minimo:
                return numero

        print(f"❌ Introduce un número mayor o igual a {minimo}")
        
def pedir_configuracion_password():
    print("\n📋 ¿Qué caracteres quieres incluir?")
    
    incluir_minus = pedir_opcion("¿Minúsculas? (s/n): ")
    incluir_mayus = pedir_opcion("¿Mayúsculas? (s/n): ")
    incluir_numeros = pedir_opcion("¿Números? (s/n): ")
    incluir_simbolos = pedir_opcion("¿Símbolos? (s/n): ")

    return {
        "minus": incluir_minus,
        "mayus": incluir_mayus,
        "numeros": incluir_numeros,
        "simbolos": incluir_simbolos
    }
    
from core.generador import generar_passwords

def generar_y_guardar_passwords():
    config = pedir_configuracion_password()
    longitud = pedir_numero("Longitud de la contraseña: ", minimo=4)
    cantidad = pedir_numero("¿Cuántas contraseñas quieres generar?: ", minimo=1)

    nuevas_passwords = generar_passwords(config, longitud, cantidad)

    for i, p in enumerate(nuevas_passwords, start=1):
        print(f"{i}. {p['password']}")

    passwords_existentes = cargar_passwords()
    passwords_existentes.extend(nuevas_passwords)
    guardar_passwords(passwords_existentes)

    print("✅ Contraseñas guardadas correctamente")