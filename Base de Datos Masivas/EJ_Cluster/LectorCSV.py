# -*- coding: utf-8 -*-


class LectorCSV:
    'clase que lee archivos CSV'

    #constructor
    def __init__(self, path, headers, separador):
        #path= path del archivo
        #si tiene headers o no el archivo, recibe "true" u cualquier otra cosa
        #separador dice de que forma separar los atributos, separa cada linea automaticamente
        self.path = path
        self.encabezado = headers
        self.separador = separador

    #metodo para leer el archivo
    def leerArchivo(self):
        #abro el archivo en modo solo lectura
        self.archivo = open(self.path, "r")
        #self.leido = self.archivo.read()
        #si el archivo tiene encabezado, lo leo y guardo
        if(self.encabezado == "true"):
            encabezado = self.archivo.readline()
            print "el encabezado es: \n %s" %encabezado
            encabezado = encabezado.strip("\n")
            self.listaEncabezados = encabezado.split(self.separador)
            print "la lista de encabezados queda como: "
            print self.listaEncabezados
        else:
            #sino, leo la primer linea, veo cuantos atributos tiene y creo un encabezado
            #que contiene atributos del tipo a1,a2,a3... aN
            encabezado = self.archivo.readline()
            encabezado = encabezado.split(self.separador)
            cantidadAtributos = len(encabezado)
            self.listaEncabezados = []
            for i in range(0, cantidadAtributos):
                self.listaEncabezados.append( "a" + str(i) )
            print "El archivo no tenia encabezados, por lo que los mismos quedaron: \n"
            print self.listaEncabezados
            #como la primera linea tambien son datos la tengo q volver a leer en el proximo loop
            self.archivo.seek(0, 0)
        #creo la variable en la q voy a almacear todos los datos
        #va a ser una lista que tenga diccionarios
        self.datos = []
        for lines in self.archivo:
            #print "linea: %s" % lines
            #me queda dividir cada linea por los separadores y agregarla a la lista de datos
            lines = lines.strip("\n")
            diccionario = {}
            lines = lines.split(self.separador)
            #print "lineas: %s" % lines
            for i in range(len(lines)):
                diccionario[self.listaEncabezados[i]] = lines[i]
            #print "diccionario %s" % diccionario
            self.datos.append(diccionario)
        self.archivo.close()
        print "\n los archivo leido queda como una lista de diccionarios: "
        print self.datos


    def get_datos(self):
        """I'm the 'datos' property."""
        return self.datos

    def get_headers(self):
        return self.listaEncabezados

#l = LectorCSV("prueba.csv", "true", ",")
#l.leerArchivo()