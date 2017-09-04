import os
from Concurso import Concurso

class Archivo:

    def __init__(self):
        self.path = ""
        self.nombreArchivo = "concursos.txt"
        self.concursos= []

    def leerArchivo(self):
        """leo el archivo y creo una lista con los concursos leidos"""
        if os.path.isfile(self.path + self.nombreArchivo):
            archivo = open( self.path + self.nombreArchivo,"r")
            for linea in archivo:
                c = Concurso()
                c.crearDesdeLinea(linea)
                self.concursos.append( c )
            archivo.close()
        else:
            print "no hay archivo"

    def guardar(self,concursos):
        archivo = open(self.path + self.nombreArchivo, "a")
        for c in concursos:
            archivo.write( c.formatoEscritura() + "\r\n" )
        archivo.close()
