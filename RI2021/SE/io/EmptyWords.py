def leerListaVacia(archivoPalabrasVacias, separadorPalabrasVacias):
    file = open(archivoPalabrasVacias)
    palabras = file.read()
    file.close()
    listaPalabras = palabras.split(separadorPalabrasVacias)
    return listaPalabras


class EmptyWords:

    def __init__(self, palabras: [str]) -> None:
        self.__listaPalabras: [str] = palabras

    def crear_con(archivoPalabrasVacias: str, separadorPalabrasVacias: str):
        file = open(archivoPalabrasVacias)
        palabras = file.read()
        file.close()
        listaPalabras = palabras.split(separadorPalabrasVacias)
        return EmptyWords(listaPalabras)

    def sacar_palabras_vacias(self, tokens):
        if self.__listaPalabras is None:
            return tokens
        else:
            return [x for x in tokens if x not in self.__listaPalabras]
