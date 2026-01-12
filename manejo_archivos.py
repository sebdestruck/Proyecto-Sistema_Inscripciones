# ============================================
#manejo_archivos.py que funcion tiene
#Manejo de lectura y escritura de archivos
# ============================================

# Nombre del archivo donde se guardan las inscripciones
ARCHIVO = "inscripciones_charlas.txt"

#esta función me permite guardar una inscripción en el archivo
def guardar_inscripcion(nombre, correo, charla):
    try:

        # Se abre el archivo en modo agregar
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{correo},{charla}\n")

    # Manejo de error de escritura
    except IOError:
        print("Error al guardar la inscripción.")

# Función para leer todas las inscripciones
def leer_inscripciones():
    inscripciones = []
    try:

        # Se abre el archivo en modo lectura
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                inscripciones.append(linea.strip())

    # Manejo del error si el archivo no existe
    except FileNotFoundError:
        pass
    return inscripciones
