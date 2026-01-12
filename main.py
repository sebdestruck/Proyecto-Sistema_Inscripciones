# ============================================
# main.py hace lo siguiente
# se muestra el menu y donde se controla
# la interacción con el usuario
# ============================================

# Importamos las funciones necesarias desde gestion_charlas
from gestion_charlas import registrar_inscripcion, consultar_inscripciones

# Función que nos enseña el menu principal
def menu():

    # Bucle infinito para que el sistema se mantenga activo
    while True:
        print("\n--- SISTEMA DE GESTION DE INSCRIPCIONES ---")
        print("1. Reguistrese en una charla")
        print("2. Consultar inscripciones")
        print("3. Salir")

        try:
            # Aqui se solicita que el usuario escoja una opcion numerica
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                registrar_inscripcion()
            elif opcion == 2:
                consultar_inscripciones()
            elif opcion == 3:
                print("Saliendo del sistema...")
                break
            else:
                # se controla las opciones que no esten dentro del rango
                print("esta opcion no esta balida.")

        # se dara manejo a los errores como: ingresar letras u otro tipo de dato
        except ValueError:
            print("solo se permite numeros ingrese otra ves.")

# desde aqui funcionara el programa
if __name__ == "__main__":
    menu()
