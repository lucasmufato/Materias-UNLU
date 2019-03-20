from .LexicAnaliser2 import LexicAnaliser2
import re
import sys

class LexicAnaliser3(LexicAnaliser2):
    """Clase para el punto 3 - obtengo componentes quimicos y formular(suma de componentes y su resultado)
        Extiende del punto 2 que ya sacaba tokens especiales"""

    def __init__(this):
        super().__init__()
        # f de formular para achicar el nombre de la varible y hacer mas facil la expresion
        f = "(\d*[A-Z][a-z]?\d?)+"
        this.REformula = f
        this.REexpresion = f + "\s*([\+\-]\s*" + f + "\s)*[\=\-]\>\s*" + f + "\s*([\+\-]\s*" + f + ")*"
        # this.REexpresion = r"(\d*[A-Z][a-z]?\d?)+\s*([\+\-]\s*(\d*[A-Z][a-z]?\d?)+\s)*\=\>\s*(\d*[A-Z][a-z]?\d?)+\s*([\+\-]\s*(\d*[A-Z][a-z]?\d?)+)*"
        this.formulas = set()
        this.expresiones = set()

    def extraer(this, linea, fileID):
        """Primero extraigo las formulas y despues los componentes, aunque no extraigo de la linea las formulas hasta q saco los componentes
        por si en una formula un componente se repite mucho signifia q es importante"""
        expresion = []
        formula = re.findall(this.REformula, linea)
        # expresion = re.fullmatch(this.REexpresion, linea)
        matches = re.finditer(this.REexpresion, linea)
        for matchNum, match in enumerate(matches):
            expresion.append( str( match.group() ) )
            print( str(match.group()) )
        # saco de la linea
        linea = this.sacar(expresion, linea)
        linea = this.sacar(formula, linea)
        # meto en los terminos
        this.analizarToken(expresion, fileID)
        this.analizarToken(expresion, fileID)
        # agrego a la lista
        this.formulas |= set(formula)
        this.expresiones |= set(expresion)
        # ejecuto el resto de las extracciones definidas en el padre
        return super().extraer(linea, fileID)


l = LexicAnaliser3()
pre = "3_"
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

# opcionales para este punto
l.mostrarListaArchivos()
l.mostrarIndice()
print(l.formulas)
print(l.expresiones)

l.armarEstadisticas1()
l.armarEstadisticas2()
l.armarEstadisticas3()
