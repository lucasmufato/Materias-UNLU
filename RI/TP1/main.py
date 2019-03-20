from TP1.LexicAnaliser import LexicAnaliser
from TP1.LexicAnaliser2 import LexicAnaliser2
from TP1.LexicAnaliser3 import LexicAnaliser3
from TP1.LexicAnaliser4 import LexicAnaliser4
from TP1.LexicAnaliser5 import LexicAnaliser5
#from TP1.LexicAnaliser6 import LexicAnaliser6
from TP1.LexicAnaliser7 import LexicAnaliser7
import sys
l = LexicAnaliser()
pre = "1_"
if len(sys.argv)==2:
    l.carpeta = sys.argv[1]
    l.archivoPalabrasVacias = ""
elif len(sys.argv)==3:
    l.carpeta = sys.argv[1]
    l.archivoPalabrasVacias = sys.argv[2]
else:
    print("Mal paso de parametros! pasale directorio de archivo(aunque tenga uno solo) y/o path de archivo con palabras vacias")
    sys.exit(-1)



"""
l = LexicAnaliser2()
pre= "2_"

l = LexicAnaliser3()
pre= "3_"
l.carpeta = "tp3/"


l = LexicAnaliser4()
pre= "4_"
l.carpeta = "archivos/"
l = LexicAnaliser5()
pre="5_"

l = LexicAnaliser7()
pre="7_"
"""

l.nombreArchivo1 = pre+"terminos.txt"
l.nombreArchivo2 = pre+"estadisticas.txt"
l.nombreArchivo3 = pre+"estadisticas2.txt"

l.carpeta = "archivos/"
#l.carpeta = "mini/"
#l.carpeta = "quijote/"


l.leerArchivos()
l.mostrarListaArchivos()
l.mostrarIndice()
l.armarEstadisticas1()
l.armarEstadisticas2()
l.armarEstadisticas3()
#.graficar()
"""
l.carpeta = "archivos/"
l.archivoPalabrasVacias = "palabras_vacias.txt"
l.leerArchivos()
l.armarEstadisticas1()
l.armarEstadisticas2()
l.armarEstadisticas3()
#opcionales para este punto
l.mostrarListaArchivos()
l.mostrarIndice()



l.obtenerCF()
l.armarGraficoComun()
l.armarGraficoLogLog()

lista = l.listaTermino_CF.copy()
l.podar(5)
l.armarGraficoComun()
l.armarGraficoLogLog()
l.listaTermino_CF = lista.copy()
l.podar(10)
l.armarGraficoComun()
l.armarGraficoLogLog()
l.listaTermino_CF = lista.copy()
l.podar(15)
l.armarGraficoComun()
l.armarGraficoLogLog()
"""
"""
l.graficar()
#l.mostrarListaArchivos()
#l.mostrarIndice()
l.armarEstadisticas1()
l.armarEstadisticas2()
l.armarEstadisticas3()
#print(l.formulas)
#print(l.expresiones)
#print(l.resultStemear)
"""