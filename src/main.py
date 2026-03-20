from ui.menu import mostrar_menu
from ui.acciones import ver_passwords

import sys
print("DEBUG PATH:", sys.path)
import os
print("MAIN DESDE:", os.getcwd())

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            print("Generar (pendiente conectar inputs...)")

        elif opcion == "2":
            ver_passwords()

        elif opcion == "3":
            print("👋 Saliendo...")
            break
        
        elif opcion == "4":
            from ui.acciones import editar_sitio
            editar_sitio()

        elif opcion == "5":
            from ui.acciones import eliminar_password
            eliminar_password()

        elif opcion == "6":
            from ui.acciones import buscar_password
            buscar_password()

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()