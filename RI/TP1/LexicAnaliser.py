import sys
import os
from collections import Counter
import collections
import unidecode
import re


class LexicAnaliser:
    """Clase para el punto uno"""

    def __init__(this):
        this.carpeta = "archivos/"
        this.archivoPalabrasVacias = "palabras_vacias.txt"
        this.separadorPalabrasVacias = "\n"
        this.terminos = {}
        this.filesIndex = {}
        this.cantTokensTotales = 0
        this.longMaxTermino = 20
        this.longMinTermino = 2
        this.biggestFileID = 0
        this.biggestFileTokens = 0
        this.biggestFileTerms = 0
        this.smallestFileID = 0
        this.smallestFileTokens = -1
        this.smallestFileTerms = 0
        this.cantTokens = 0
        this.cantTerminos = 0
        this.nombreArchivo1 = "1_terminos.txt"
        this.nombreArchivo2 = "1_estadisticas.txt"
        this.nombreArchivo3 = "1_estadisticas2.txt"

    def tokenizar(this, linea):
        """recibo la linea entera, le saco ciertos terminos y cosas separo por espacios"""
        linea = unidecode.unidecode(linea).lower()
        # linea = unidecode.unidecode( linea.lower().replace("."," ").replace(","," ").replace("'"," ").replace('"',' ') )
        # linea = linea.replace("("," ").replace(")"," ").replace("{"," ").replace("}").replace("["," ").replace("]"," ")
        # linea = linea.replace(":"," ").replace("^"," ").replace("="," ")
        linea = re.sub('[^0-9a-zA-Z]+', ' ', linea)
        tokens = linea.split()
        for t in tokens:  # si el token no esta entre el tamaño aceptado
            t.strip()
            if not (this.longMinTermino < len(t) < this.longMaxTermino):
                # print("sacando token: "+t)
                tokens.remove(t)
        return tokens

    def leerArchivos(this):
        lista_vacias = []
        if (this.archivoPalabrasVacias != ""):
            print("Leyendo palabras vacias")
            lista_vacias = this.leerListaVacia()
        cantTerminos = 0
        cantTokens = 0
        print("Leyendo archivos")
        for file in os.listdir(this.carpeta):
            if not (os.path.isdir(file)):
                a = open(this.carpeta + file, 'r',errors="ignore")
                fileId = len(this.filesIndex)
                this.filesIndex[fileId]=file
                for linea in a:
                    tokens = this.extraer(linea, fileId)
                    # extraigo tokens importantes(fechas, nombres, etc)
                    tokens = this.tokenizar(tokens)
                    # normalizo y tokenizo
                    tokens = this.sacar_palabras_vacias(tokens, lista_vacias)
                    # saco palabras vacias
                    cantTokens += len(tokens)
                    cantTerminos += len(set(tokens))
                    this.analizarToken(tokens, fileId, True)# paso los tokens a
                # cuando termine de leer el archivo
                this.cantTokensTotales += cantTokens
                if (cantTokens > this.biggestFileTokens):
                    this.biggestFileTerms = cantTerminos
                    this.biggestFileTokens = cantTokens
                    this.biggestFileID = fileId
                if cantTokens < this.smallestFileTokens or this.smallestFileTokens == -1:
                    this.smallestFileTokens = cantTokens
                    this.smallestFileTerms = cantTerminos
                    this.smallestFileID = fileId
                cantTerminos = 0
                cantTokens = 0
                a.close()
            #print(this.terminos)

    def extraer(this, linea, fileId):
        """para completar en una clase q extienda"""
        return linea

    def leerListaVacia(this):
        a = open(this.archivoPalabrasVacias)
        palabras = a.read()
        listaPalabras = palabras.split(this.separadorPalabrasVacias)
        return listaPalabras

    def sacar_palabras_vacias(this, tokens, lista_vacia):
        for elem in lista_vacia:
            tokens = list(filter(lambda a: a != elem, tokens))
        return tokens

    def analizarToken(this, tokens, fileId, stemear=False):
        """cuenta la cantidad de repeticiones de cada token y devuelve diccionario del tipo
        {a:2,B:3....} si es necesario se stemea, y se agrega a la lista de terminos"""
        tokens = dict(Counter(tokens))
        for orig_token in tokens:
            nuevo_token = orig_token
            if stemear:
                nuevo_token = this.stemear(orig_token)  # stemeo ciertos tokens nomas, no todos
            if nuevo_token in this.terminos:
                posting = this.terminos[nuevo_token]
                if fileId in posting:
                    posting[fileId] += tokens[orig_token]
                    this.terminos[orig_token]=posting
                else:
                    posting[fileId] = tokens[orig_token]
                    this.terminos[orig_token] = posting
            else:
                this.terminos[nuevo_token] = {fileId: tokens[orig_token]}

    def mostrarListaArchivos(this):
        print("LISTA DE ARCHIVOS ID -> NOMBRE")
        print(this.filesIndex)

    def mostrarIndice(this):
        print("INDICE INVERTIDO DE TERMINOS -> POSTING (fileId:repeticiones)")
        print(this.terminos)
        for termino in this.terminos.keys():
            print(termino + "  -->  " + str(this.terminos[termino]))

    def stemear(this, token):
        """Se completa en alguna clase que lo extienda"""
        return token

    def armarEstadisticas1(this):
        print("armando estadisticas 1...")
        file = open(this.nombreArchivo1, 'w');
        od = this.terminos.copy().items()
        od = sorted(od, key=lambda x: x[0])
        # lista de tuplas( termino, {fileId:repeticion})
        for tupla in od:
            # tupla( termino, {fileId:repeticion})
            cf = 0
            for fileId in tupla[1]:
                cf += tupla[1][fileId];
            file.write(tupla[0] + "\t\t  -CF: " + str(cf) + "\t\t  -DF: " + str(len(tupla[1])) + " \r\n")
        file.close()
        print("fin estadisticas1")

    def armarEstadisticas2(this):
        print("armando estadisticas2")
        cantDocumentos = len(this.filesIndex)
        long = 0
        fewRepTerm = []
        copia = this.terminos.copy()
        for termino in copia.keys():
            long += len(termino)
            postingDic = copia[termino]
            # si el termino esta una sola vez en la coleccion
            if len(postingDic) == 1:
                fileId, repeticiones = postingDic.popitem()
                if repeticiones == 1:
                    fewRepTerm.append(termino)
        long = long / len(this.terminos)
        file = open(this.nombreArchivo2, "w")
        file.write("cantidad de documentos: " + str(cantDocumentos) + " \r\n")
        file.write("cantidad de tokens extraidos: " + str(this.cantTokensTotales) + " \r\n")
        file.write("cantidad de terminos extraidos: " + str(len(this.terminos)) + " \r\n")
        file.write("promedio de tokens por documento: " + str(this.cantTokensTotales / cantDocumentos) + " \r\n")
        file.write("promedio de terminos por documento: " + str(len(this.terminos) / cantDocumentos) + " \r\n")
        file.write("largo promedio de un termino: " + str(long) + " \r\n")
        file.write(
            "El archivo mas corto(por cantidad de tokens) es: " + this.filesIndex[this.smallestFileID] + " con " + str(
                this.smallestFileTokens)
            + " tokens y " + str(this.smallestFileTerms) + " terminos" + " \r\n")
        file.write(
            "El archivo mas largo(por cantidad de tokens) es: " + this.filesIndex[this.biggestFileID] + " con " + str(
                this.biggestFileTokens)
            + " tokens y " + str(this.biggestFileTerms) + " terminos" + " \r\n")
        file.write("Los terminos que aparecen una sola ves en la coleccion son: " + str(fewRepTerm) + " \r\n")

        print("fin estadisticas2")
        file.close()

    def armarEstadisticas3(this):
        print("inicio estadisticas3")
        ter = 10
        minimos = []
        maximos = []
        for termino in this.terminos.keys():
            postingDic = this.terminos[termino]
            cant = 0
            for fileId, repeticiones in postingDic.items():
                cant += repeticiones
            t = (cant, termino)
            if len(maximos) < ter:  # si no estan llenas las listas las lleno con los 10 primeros q encuentro
                maximos.append(t)
                minimos.append(t)
                minimos = sorted(minimos, key=lambda x: x[0])
                maximos = sorted(maximos, key=lambda x: x[0])
            else:
                if cant > maximos[0][0]:
                    maximos[0] = t
                    maximos = sorted(maximos, key=lambda x: x[0])
                if cant < minimos[ter - 1][0]:
                    minimos[ter - 1] = t
                    minimos = sorted(minimos, key=lambda x: x[0])
        file = open(this.nombreArchivo3, "w")
        file.write("los terminos que mas se repiten son: " + str(maximos) + "\r\n")
        file.write("los terminos que menos se repiten son: " + str(minimos) + "\r\n")
        file.close()
        print("fin estadisticas3")
