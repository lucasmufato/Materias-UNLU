# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, vel):
        self.tam=2
        self.pesos= self.nuevoVectorPesos(2)
        self.velocidad=vel
        self.figura=None

    def setMostrarSoloFinal(self,a):
        self.mostrarFinal=a

    def nuevoVectorPesos(self,tam):
        vector = []
        for i in range(0,tam):
            vector.append(random.random() )
        vector.append(1)
        print "vector de pesos inicial: ",vector
        return vector

    def aprender(this,matriz,esperado):
        this.matriz=matriz
        this.esperado=esperado
        #for i in range (0, len(this.esperado)):
            #print "para el valor ", this.matriz[i] , "espero el valor: ",this.esperado[i]
        encontrado=False
        this.itera=0
        while (encontrado==False and this.itera<30):
            print "Iteracion Nro ",this.itera
            print ""
            encontrado=True
            for r in range (0,len(this.matriz)):
                funcion=0
                #sumo en funcion las valor1*peso1+valo2*peso2...
                for i in range(0,this.tam):
                    funcion+= this.matriz[r][i] * this.pesos[i]
                #sumo el peso T, que arranca siendo uno
                funcion+=this.pesos[this.tam]
                print "funcion para [",this.matriz[r][0] ,",", this.matriz[r][1],"] queda: ",funcion
                if this.FuncActivac(funcion) == this.esperado[r]:
                    print "Fila ",r," func: ",funcion, "esperado: ",this.esperado[r]
                    encontrado=False
                    this.recalcularPesos(r,funcion)
                else:
                    print "para la fila ",r, "el resultado es correcto"
                r+=1
            this.itera+=1
            if this.mostrarFinal==False:
                this.graficar(False)
            print ""
        print ""
        print "la respuesta es: "
        print this.pesos
        print "tarde: ",this.itera
        this.graficar(True)

    def graficar(this,rta):
        if this.figura == None:
            this.figura= plt.figure()
        #defino tamaño de los ejes
        plt.axis([-3,3,-3,3])
        #creo las rectas de los ejes
        plt.plot([0,0,0,0,0],[-2,-1,0,1,2],"b")
        plt.plot([-2,-1,0,1,2],[0,0,0,0,0],"b")
        #agrego entradas
        for i in range(0,4):
            if this.esperado[i] == 1:
                plt.plot(this.matriz[i],"go")
            else:
                plt.plot(this.matriz[i],"ro")
        #muestro la recta
        recta = []
        r=range(-2,3)
        for i in r:
            y = (-this.pesos[0]/this.pesos[1])*i - (this.pesos[2]/this.pesos[1])
            recta.append(y)
        plt.plot(recta,r,"y")
        if(rta):
            plt.title("Resultado Final:")
        else:
            plt.title("Intermedio:")
        funcion = "",-this.pesos[0],"/",this.pesos[1],"x +", -(this.pesos[2]/this.pesos[1])
        plt.text(0, -2, funcion)
        plt.show()

    def FuncActivac(this, valor):
        if valor>0:
            return 1
        else:
            return 0

    def recalcularPesos(this,fila,funcion):
        for j in range(0,len(this.pesos)):
            p= this.esperado[fila] - funcion
            if j==2:
                modif = this.velocidad * p * 1
            else:
                modif = this.velocidad*p* this.matriz[fila][j]
            print "aumento el vector de pesos[",j,"] en ",modif
            this.pesos[j]+= modif