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

    def __str__(self):
        return "Division: "+ self.divison +" | Area: "+self.area+ \
               " |Cargo: "+self.cargo + " |Dedicacion " + self.dedicacion\
               + " |Expediente "+self.expediente

    def dividirCampos(self):
       lineas = self.area.split("\n")
       print len(lineas), lineas
       self.area = lineas[1]
       self.cargo = lineas[2]
       self.dedicacion = lineas[3]
       self.expediente = lineas[4]