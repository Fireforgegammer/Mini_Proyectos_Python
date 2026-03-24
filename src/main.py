from core.generador import generar_password, construir_pantalla
from ui.menu import mostrar_menu
from ui.acciones import (
    ver_passwords,
    anadir_sitio,
    eliminar_password,
    buscar_password,
    pedir_configuracion_password 
)
import sys
print("DEBUG PATH:", sys.path)
import os
print("MAIN DESDE:", os.getcwd())

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        print(f"DEBUG opcion elegida: '{opcion}'")

        if opcion == "1":
            print("👉 ENTRO EN 1")

            config = pedir_configuracion_password() 
            longitud = int(input("Longitud de la contraseña: "))
            cantidad = int(input("¿Cuántas contraseñas quieres generar?: "))

            pantalla, obligatorios = construir_pantalla(config)

            nuevas_passwords = []


            for i in range(cantidad):
                password = generar_password(longitud, pantalla, obligatorios)
                print(f"{i+1}. {password}")

                nuevas_passwords.append({
                    "password": password,
                    "sitio": None
                })

            passwords_existentes = cargar_passwords()
            passwords_existentes.extend(nuevas_passwords)
            guardar_passwords(passwords_existentes)

        elif opcion == "2":
            print("👉 ENTRO EN 2")
            ver_passwords()

        elif opcion == "3":
            print("👉 ENTRO EN 3")
            break   # ✅ AQUÍ VA EL BREAK

        elif opcion == "4":
            print("👉 ENTRO EN 4")
            anadir_sitio()

        elif opcion == "5":
            print("👉 ENTRO EN 5")
            eliminar_password()

        elif opcion == "6":
            print("👉 ENTRO EN 6")
            buscar_password()

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()