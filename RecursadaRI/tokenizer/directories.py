
def leer_archivo_palabras_vacias(path, separador = "\n\r"):
    print("leyendo palabras vacias")
    a = open(path)
    palabras = a.read()
    listaPalabras = palabras.split(separador)
    return listaPalabras

