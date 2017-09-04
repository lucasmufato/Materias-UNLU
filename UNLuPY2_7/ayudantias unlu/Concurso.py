#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
#pongo que acepte caracteres en UTF8

class Concurso:

    def __init__(self):
        self.divison=""
        self.area=""
        self.cargo=""
        self.dedicacion=""
        self.expediente=""
        self.resolucion=""

    def crearDesdeLinea(self,linea):
        atributos = linea.split(",")
        self.divison = atributos[0]
        self.area = atributos[1]
        self.cargo = atributos[2]
        self.dedicacion = atributos[3]
        self.expediente = atributos[4]
        self.resolucion = atributos[5]


    def __str__(self):
        return "Division: "+ self.divison +" | Area: "+self.area+ \
               " |Cargo: "+self.cargo + " |Dedicacion: " + self.dedicacion\
               + " |Expediente: "+self.expediente + " |Resolucion: " + self.resolucion

    def dividirCampos(self):
       lineas = self.area.split("\n")
       #print len(lineas), lineas
       self.area = lineas[1].replace("\t","").replace("ÁREA: ","")
       self.cargo = lineas[2].replace("\t","").replace("CARGO: ","")
       self.dedicacion = lineas[3].replace("\t","").replace("DEDICACIÓN: ","")
       self.expediente = lineas[4].replace("\t","").replace("EXP-LUJ: ","")

    def __eq__(self, other):
        """comparo mediante el nro de resolucion"""
        return self.resolucion == other.resolucion

    def formatoEscritura(self):
        return self.divison + "," + self.area + \
               "," + self.cargo + "," + self.dedicacion \
               + "," + self.expediente + "," + self.resolucion