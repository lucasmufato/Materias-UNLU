# -*- coding: utf-8 -*-

from Perceptron import Perceptron

# matriz para todo el ejercicio
matriz = [[0,0],[0,1],[1,0],[1,1]]

#operaciones harcodeadas
op_and = [0,0,0,1]
op_or = [0,1,1,1]

p = Perceptron(0.7)
p.setMostrarSoloFinal(True)
x=None
while x!=0:
    print ""
    print ""
    print ""
    print "Simulacion del Perceptron"
    print "Para Salir ingrese 0 (cero)"
    print "Para simular un AND ingrese 1"
    print "Para simular un OR ingrese 2"

    x = raw_input("ingrese el dato \n")
    if x == "1":
        p.aprender(matriz,op_and)
    else:
        if x== "2":
            p.aprender(matriz,op_or)
        else:
            if x!= "0":
                print "orden no encontrada :("
    print ""
    print ""
    print ""



