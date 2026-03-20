from ui.menu import mostrar_menu
from ui.acciones import ver_passwords
from core.generador import generar_passwords
from core.storage import guardar_passwords

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

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()