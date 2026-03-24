from core.generador import generar_password, construir_pantalla
from ui.menu import mostrar_menu
from ui.acciones import (
    ver_passwords,
    anadir_sitio,
    eliminar_password,
    buscar_password
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
           # Configuración fija para pruebas
          config = {
                "minus": True,
                "mayus": True,
                "numeros": True,
                "simbolos": False
            }
            
            # Valores fijos
          longitud = 12
          pantalla, obligatorios = construir_pantalla(config)
            
            # Generar contraseña
          password = generar_password(longitud, pantalla, obligatorios)
          print(f"\n✅ Contraseña generada: {password}\n")
        elif opcion == "2":
          print("👉 ENTRO EN 2")
          ver_passwords()

        elif opcion == "3":
          print("👉 ENTRO EN 3")
          break

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