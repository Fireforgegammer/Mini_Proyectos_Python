from ui.menu import mostrar_menu
from ui.acciones import (
    ver_passwords,
    anadir_sitio,
    eliminar_password,
    buscar_password,
    generar_y_guardar_passwords
)
import sys
print("DEBUG PATH:", sys.path)
import os
print("MAIN DESDE:", os.getcwd())

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("Selecione opciones")
            generar_y_guardar_passwords()

        elif opcion == "2":
            print("Mostrando contraseñas")
            ver_passwords()

        elif opcion == "3":
            print("Selecion de nombre")
            anadir_sitio()

        elif opcion == "4":
            print("Selecione opcion")
            eliminar_password()

        elif opcion == "5":
            print("Introduzca nombre")
            buscar_password()

        elif opcion == "6":
            print("Gracias")
            break

        else:
            print("❌ Opción inválida")


if __name__ == "__main__": 
    main()