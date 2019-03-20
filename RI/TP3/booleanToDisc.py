import os
import struct
from collections import Counter

from TP3.BooleanAnaliser import BooleanAnaliser


class BooleanToDisc(BooleanAnaliser):

    def __init__(this):
        super().__init__()
        this.termIndex={}
        this.lastTermId=0
        this.terminos=[]

        #varaibles para el manejo de los archivos

        this.primera=True
        this.struct = struct.Struct("III")
        this.packed=0.0

    def construirIndice(this):
        this.leerArchivos()
        this.guardarADisco()

    """re-escribo esta parte para meterle el try catch"""
    def leerArchivos(this):
        this.file = open(this.nombreArchivo1, "wb")
        lista_vacias = []
        if (this.archivoPalabrasVacias != ""):
            print("Leyendo palabras vacias")
            lista_vacias = this.leerListaVacia()
        cantTerminos = 0
        cantTokens = 0
        a=0
        print("Leyendo archivos")
        for file in os.listdir(this.carpeta):
            if not (os.path.isdir(file)):
                a = open(this.carpeta + file, 'r',errors="ignore")
                fileId = len(this.filesIndex)
                this.filesIndex[fileId]=file
                for linea in a:
                    try:
                        tokens = this.extraer(linea, fileId)
                        # extraigo tokens importantes(fechas, nombres, etc)
                        tokens = this.tokenizar(tokens)
                        # normalizo y tokenizo
                        tokens = this.sacar_palabras_vacias(tokens, lista_vacias)
                        # saco palabras vacias
                        cantTokens += len(tokens)
                        cantTerminos += len(set(tokens))
                        this.analizarToken(tokens, fileId, True)# paso los tokens a
                    except MemoryError:
                        print("ya revente la memoria!")
                        this.ordenar()
                        this.pasarAArchivos()
                        this.mergear()
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
        this.ordenar()
        this.pasarAArchivos()
        this.mergear()

    def analizarToken(this, tokens, fileId, stemear=False):
        """cuenta la cantidad de repeticiones de cada token y devuelve diccionario del tipo
        {a:2,B:3....} si es necesario se stemea, y se agrega a la lista de terminos"""
        tokens = dict(Counter(tokens))
        for orig_token in tokens:
            nuevo_token = orig_token
            if stemear:
                nuevo_token = this.stemear(orig_token)  # stemeo ciertos tokens nomas, no todos
            #empiezo a guardar los id de termino en ves del termino
            if nuevo_token not in this.termIndex:
                this.termIndex[nuevo_token]=this.lastTermId
                this.lastTermId+=1
            nuevo_token = this.termIndex[nuevo_token]
            if (nuevo_token,fileId) in this.terminos:
                print("la tupla "+str( (nuevo_token,fileId)) + "esta en la lista")
                i = this.terminos.index( (nuevo_token,fileId) )
                triplet = this.terminos[i]
                triplet[2] = triplet[2]+tokens[orig_token]
            else:
                this.terminos.append( (nuevo_token,fileId,tokens[orig_token]) )

    def pasarAArchivos(this):
        """Paso las triplas al archivo y las borro de memoria"""
        for term in this.terminos:
            this.packed = this.struct.pack(*term)
            this.file.write(this.packed)
            del term
        this.file.close()
        if this.primera:
            this.file = open(this.nombreArchivo2,"wb")

    def ordenar(this):
        this.terminos.sort()

    def mergear(this):
        if this.primera:
            #si es la primera ves q entro al merge no mergeo nada
            print("primera")
            this.primera=False
            return
        fileA = open(this.nombreArchivo1,"rb")
        fileB = open(this.nombreArchivo2,"rb")
        fileC = open(this.nombreArchivo3,"wb")

        this.content = fileA.read(4 * 3)
        tuplaA = this.struct.unpack(this.content)
        this.content = fileB.read(4 * 3)
        tuplaB = this.struct.unpack(this.content)
        finArchivo="" #para saber si un archivo se termino de leer antes que el otro
        while finArchivo=="":
            print("A: "+str(tuplaA)+ "  B: "+str(tuplaB))
            #si el ID de termino de a menor q el de B
            if tuplaA[0] < tuplaB[0]:
                fileC.write( this.struct.pack(*tuplaA) )
                this.content = fileA.read(4 * 3)
                if this.content == "":
                    finArchivo="A"
                else:
                    tuplaA = this.struct.unpack(this.content)
            elif tuplaB[0] < tuplaA[0]:     #si el de B es menor
                fileC.write(this.struct.pack(*tuplaB))
                this.content = fileB.read(4 * 3)
                if this.content == "":
                    finArchivo = "B"
                else:
                    tuplaB = this.struct.unpack(this.content)
            else:
                #si el id de termino es igual comparo por documento
                if tuplaA[1] < tuplaB[1]:
                    fileC.write(this.struct.pack(*tuplaA))
                    this.content = fileA.read(4 * 3)
                    if this.content == "":
                        finArchivo = "A"
                    else:
                        tuplaA = this.struct.unpack(this.content)
                elif tuplaB[1] < tuplaA[1]:     #si el de B es menor
                    fileC.write(this.struct.pack(*tuplaB))
                    this.content = fileB.read(4 * 3)
                    if this.content == "":
                        finArchivo = "B"
                    else:
                        tuplaB = this.struct.unpack(this.content)
                else:
                    #si tiene el mismo termino y el mismo docId lo sumo
                    newTupla = (tuplaA[0], tuplaA[1], tuplaA[2]+tuplaB[2])
                    fileC.write(this.struct.pack(*newTupla))
                    #obtengo el primero de ambos archivos
                    this.content = fileA.read(4 * 3)
                    if this.content == "":
                        finArchivo = "A"
                    else:
                        tuplaA = this.struct.unpack(this.content)
                    this.content = fileB.read(4 * 3)
                    if this.content == "":
                        finArchivo = "B"
                    else:
                        tuplaB = this.struct.unpack(this.content)
        #copio y comparo hasta llegar al fin de archivo. veo en cual llege y entonces leo y paso el otro hasta terminarlo
        if finArchivo=="A":
            finArchivo = fileB
        else:
            finArchivo = fileA
        while True:
            this.content = finArchivo.read(4*3)
            if this.content == "":
                break
            tupla = this.struct.unpack(this.content)
            fileC.write(this.struct.pack(*tupla))
        fileA.close()
        fileB.close()
        fileC.close()
        os.remove(this.nombreArchivo1)
        os.rename(this.nombreArchivo3,this.nombreArchivo1)
        os.remove(this.nombreArchivo3)
        this.file = open(this.nombreArchivo2,"wb")
        this.primera=True

    def pasarChucksAIndiceInvertido(this):
        this.file = open(this.nombreArchivo1,"rb")
        bandera=True
        while bandera:
            linea = this.file.read(4*3)
            tripla = this.struct.unpack(linea)
            lastTermino = tripla[0] #tripla[0] = termino
            #pero mira q lindo corte de control de programacion 1!!
            while tripla[0] == lastTermino:
                this.agregarAIndice(tripla)
                linea = this.file.read(4 * 3)
                tripla = this.struct.unpack(linea)
            print("el indice x el momento queda: ")
            print(this.terminos)
        this.file.close()

    def agregarAIndice(this, tripla):
        if tripla[0] in this.terminos:
            posting = this.terminos[tripla[0]]


