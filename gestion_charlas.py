# ============================================
# gestion_charlas.py hace lo siguiente
# Gestiona las charlas y las inscripciones
# Controla cupos, validaciones y registros
# ============================================

# Importamos funciones para manejo de archivos
from manejo_archivos import guardar_inscripcion, leer_inscripciones

# He manejado un diccionario que almacena las charlas y sus cupos disponibles
charlas = {
    "Marketing": 3,
    "Finanzas": 2,
    "Liderazgo": 4,
    "Superación": 2,
    "Redes Sociales": 3
}

# Función para pedir los datos al usuario
# uso de recursividad si el dato está vacío
def solicitar_dato(mensaje):
    dato = input(mensaje).strip()

    # aqui realizo la validación de datos vacíos
    if dato == "":
        print("no puede estar vacio el dato.")
        return solicitar_dato(mensaje) # realizo una llamada recursiva

    return dato

# Función que muestra las charlas disponibles
def mostrar_charlas():
    print("\nCharlas disponibles:")

    # realizo una numeracion para mostrar opciones numeradas
    for i, (charla, cupos) in enumerate(charlas.items(), 1):
        print(f"{i}. {charla} (Cupos disponibles: {cupos})")

# esta es la función principal para registrar una inscripción
def registrar_inscripcion():

    # aqui pido los datos personales
    nombre = solicitar_dato("Ingrese su nombre: ")
    correo = solicitar_dato("Ingrese su correo: ")

    # aqui mustro las charlas disponibles
    mostrar_charlas()

    try:

        # en esta parte el usuario selecciona la charla
        opcion = int(input("Seleccione una charla: "))

        # Se obtiene el nombre de la charla seleccionada
        charla_seleccionada = list(charlas.keys())[opcion - 1]

    # Manejo los errores por opcion invalida
    except (ValueError, IndexError):
        print("Opción inválida. Intente nuevamente.")
        return registrar_inscripcion()

    # Validación de cupos disponibles
    if charlas[charla_seleccionada] > 0:

        # aqui se reduce el numero de cupos
        charlas[charla_seleccionada] -= 1

        # Se guarda la inscripción en el archivo
        guardar_inscripcion(nombre, correo, charla_seleccionada)
        print("Inscripción realizada con éxito.")
    else:
        # doy el mensaje si no hay cupos disponibles
        print("Esta charla se quedo sin cupos .")

# Función para consultar todas las inscripciones registradas
def consultar_inscripciones():
    inscripciones = leer_inscripciones()

    # Verificación de registros existentes
    if not inscripciones:
        print("No hay inscripciones registradas.")
    else:
        print("\nInscripciones registradas:")

        # Se recorren y muestran las inscripciones
        for inscripcion in inscripciones:
            nombre, correo, charla = inscripcion.split(",")
            print(f"Nombre: {nombre} | Correo: {correo} | Charla: {charla}")
