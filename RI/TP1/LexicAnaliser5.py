from .LexicAnaliser2 import LexicAnaliser2
import matplotlib.pyplot as plt
import math as m
import sys

class LexicAnaliser5(LexicAnaliser2):
    def __init__(this):
        super().__init__()
        this.listaTermino_CF=[]
        this.terminosTotales=0
        this.coef = 0,5

    def graficarLeyZipf(this):
        this.obtenerCF()
        this.armarGraficoComun()
        this.armarGraficoLogLog()

    def obtenerCF(this):
        """obtengo las CF para cada termino y devuelvo una lista ordenada por el CF de mayor a menor"""
        listaOrdenada = []
        for termino in this.terminos.items():
            # tupla( termino, {fileId:repeticion})
            cf = 0
            for fileId in termino[1]:
                cf += termino[1][fileId]
            listaOrdenada.append( (termino[0],cf) )
            this.terminosTotales+=cf
        listaOrdenada = sorted(listaOrdenada, key=lambda x:-x[1])
        this.listaTermino_CF = listaOrdenada

    def podar(this, porcentaje):
       # print("Suma de Cf de cada termino: "+str(this.terminosTotales))
        print("longuitud de lista de terminos antes de la poda: "+str(len(this.listaTermino_CF)))
        print("Lista originar: "+ str(this.listaTermino_CF))
        podado=0
        eliminar=[]
        for i in range(0,len(this.listaTermino_CF)):
            if podado < porcentaje:
                eliminar.append(i)
                podado+= (this.listaTermino_CF[i][1] * 100) / this.terminosTotales
            else:
                break
        print("Del principio pode un: "+str(podado) + " son subindices entre " + str(eliminar[0])+" y "+str(eliminar[len(eliminar)-1]))
        podado=0
        for i in reversed(eliminar):
            del this.listaTermino_CF[i]
        eliminar=[]
        for i in range(len(this.listaTermino_CF)-1,0,-1):
            if podado < porcentaje:
                eliminar.append(i)
                podado+= (this.listaTermino_CF[i][1] * 100) / this.terminosTotales
            else:
                break
        print("Del final pode un: " + str(podado) + " son subindices entre " + str(eliminar[0])+" y "+str(eliminar[len(eliminar)-1]))
        for i in eliminar:
            del this.listaTermino_CF[i]
        print("longuitud de lista de terminos DESPUES de la poda: " + str(len(this.listaTermino_CF)))
        print("Lista despues de las poda: " + str(this.listaTermino_CF))

    def calcuarZipf(this):
        primero = this.listaTermino_CF[0][1]
        rectaZipf = [primero]
        suma = sum(i for _, i in this.listaTermino_CF)
        for rank in range(1,len(this.listaTermino_CF)):
            itermino = (1 / rank**this.coef) / ( rank ** this.coef)

    def armarGraficoComun(this):
        """dibujo la linea sacando los datos de la lista"""
        x=[]
        y=[]
        for i in range(0,len(this.listaTermino_CF)):
            #lista: [ (termino, cf),(termino,cf)..]
            x.append( i )
            y.append( this.listaTermino_CF[i][1] )
        plt.xlabel('Termino')
        plt.ylabel('Collection Frequency')
        plt.title('Ley de Zipf escala comun')
        plt.plot(x, y)
        plt.grid()
        plt.show()

    def armarGraficoLogLog(this):
        """dibujo a linea pero en version Log-Log"""
        x = []
        y = []
        for i in range(1, len(this.listaTermino_CF)+1):
            # lista: [ (termino, cf),(termino,cf)..]
            x.append(m.log(i))
            y.append(m.log(this.listaTermino_CF[i-1][1]))
        plt.xlabel('Termino')
        plt.ylabel('Collection Frequency')
        plt.title('Ley de Zipf escala Log-Log base e')
        plt.plot(x, y)
        plt.grid()
        plt.show()


l = LexicAnaliser5()
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
#l.armarEstadisticas1()
#l.armarEstadisticas2()
#l.armarEstadisticas3()
# opcionales para este punto
#l.mostrarListaArchivos()
#l.mostrarIndice()
l.obtenerCF()
l.armarGraficoComun()
l.armarGraficoLogLog()
#lista auxiliar para no tener q volver a leer el archivo
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