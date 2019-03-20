from nltk.stem.snowball import SpanishStemmer
from .LexicAnaliser2 import LexicAnaliser2
import sys

class LexicAnaliser4(LexicAnaliser2):
    def __init__(this):
        super().__init__()
        this.stemmer = SpanishStemmer()
        this.resultStemear = {}  # diccionario de tokensStemeados q apunta a un set de los tokens sin stemear
        # ej: comput -> cumpaticion, computar, computadora...

    def stemear(this, token):
        tokenStemeado = this.stemmer.stem(token)
        # print("token "+ token + "  steam: " + tokenStemeado)
        if tokenStemeado in this.resultStemear:
            #print("agregando el token "+token+" a su raiz: "+tokenStemeado)
            this.resultStemear[tokenStemeado].add(
                token)  # al ser un set si estaba o no el token no me importa, el set se encarga q no se repita
        else:
            this.resultStemear[tokenStemeado] = set()
            this.resultStemear[tokenStemeado].add(token)
        return str(tokenStemeado)


l = LexicAnaliser4()
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
l.armarEstadisticas1()
l.armarEstadisticas2()
l.armarEstadisticas3()
# opcionales para este punto
l.mostrarListaArchivos()
l.mostrarIndice()