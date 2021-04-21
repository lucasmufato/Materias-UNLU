def leerListaVacia(archivoPalabrasVacias, separadorPalabrasVacias):
    file = open(archivoPalabrasVacias)
    palabras = file.read()
    file.close()
    listaPalabras = palabras.split(separadorPalabrasVacias)
    return listaPalabras