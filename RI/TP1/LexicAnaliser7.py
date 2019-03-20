from .LexicAnaliser2 import LexicAnaliser2
import os
import matplotlib.pyplot as plt
import sys

class LexicAnaliser7(LexicAnaliser2):

    def __init__(this):
        super().__init__()
        this.listaDeTuplas=[]
        this.archivoPalabrasVacias=""

    def leerArchivos(this):
        """igual que en el punto uno nada mas q agrego """
        lista_vacias = []
        if (this.archivoPalabrasVacias != ""):
            print("Leyendo palabras vacias")
            lista_vacias = this.leerListaVacia()
        cantTerminos = 0
        cantTokens = 0
        print("Leyendo archivos")
        for file in os.listdir(this.carpeta):
            if not (os.path.isdir(file)):
                a = open(this.carpeta + file, 'r',errors="ignore")
                fileId = len(this.filesIndex)
                this.filesIndex[fileId]=file
                for linea in a:
                    tokens = this.extraer(linea, fileId)
                    # extraigo tokens importantes(fechas, nombres, etc)
                    tokens = this.tokenizar(tokens)
                    # normalizo y tokenizo
                    tokens = this.sacar_palabras_vacias(tokens, lista_vacias)
                    # saco palabras vacias
                    cantTokens += len(tokens)
                    cantTerminos += len(set(tokens))
                    this.analizarToken(tokens, fileId, True)
                    this.listaDeTuplas.append( (cantTerminos,len(this.terminos)) )              #LE AGREGO SOLO ESTO
                # cuando termine de leer el archivo
                this.cantTokensTotales += cantTokens
                if (cantTokens > this.biggestFileTokens):
                    this.biggestFileTerms = cantTerminos
                    this.biggestFileTokens = cantTokens
                    this.biggestFileID = fileId
                if cantTokens < this.smallestFileTokens or this.smallestFileTokens == -1:
                    this.smallestFileTokens = cantTokens
                    this.smallestFileTerms = cantTerminos
                    this.smallestFileID = fileId
                cantTerminos = 0
                cantTokens = 0
                a.close()

    def graficar(this):
        x = []
        y = []
        for t in this.listaDeTuplas:
            x.append(t[0])
            y.append(t[1])
        plt.xlabel('Terminos Totales')
        plt.ylabel('Terminos unicos')
        plt.title('Crecimiento del Vocabulario')
        plt.plot(x, y)
        plt.grid()
        plt.show()

l = LexicAnaliser7()
pre = "4_"
if len(sys.argv) == 2:
    l.carpeta = sys.argv[1]
    l.archivoPalabrasVacias = ""
elif len(sys.argv) == 3:
    l.carpeta = sys.argv[1]
    l.archivoPalabrasVacias = sys.argv[2]
else:
    print(
        "Mal paso de parametros! pasale directorio de archivo(aunque tenga uno solo) y/o path de archivo con palabras vacias")
    sys.exit(-1)

l.leerArchivos()
l.graficar()