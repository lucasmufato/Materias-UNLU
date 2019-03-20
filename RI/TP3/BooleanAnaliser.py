
from collections import Counter
import struct
from TP1.LexicAnaliser import LexicAnaliser

"""
4 BYTES ID_DOC
4 BYTES TF

OPERADORES DE PROXIMIDAD
CERCA +- 5
ADYACENTE

"""

class BooleanAnaliser(LexicAnaliser):
    def __init__(this):
        this.term_DF={}
        """  termino -> (DF,pos)   """
        super().__init__()
        """termino -> (id1,id2..)"""
        this.terminos = {}
        this.conectores= ["AND","OR","NOT"]

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
                if fileId not in posting:
                    posting.append(fileId)
            else:
                this.terminos[nuevo_token] = [fileId]


    def guardarADisco(this):
        """guardo el vocabulario en disco y armo el lexicon. al final borro el vocabulario"""
        pos=0
        file = open(this.nombreArchivo1, "wb")
        for term in this.terminos:
            posting = this.terminos[term]
            this.term_DF[term]= (len(posting),pos)
            #print(term+" DF al escribir: "+ str(len(posting)) )
            s = struct.Struct("I"*len(posting))
            packed = s.pack(*posting)
            file.write(packed)
            pos=file.tell()
        file.close()
        del this.terminos #borro el indice en memoria ya q lo pase al archivo



    def buscarTerminos(this, term):
        """busco los terminos que me viene en la lista y devuelvo para cada termino en el orden que entraron una lista
        documentos en los que aparece"""
        file_read = open(this.nombreArchivo1, "rb")
        rta=[]
        if term in this.term_DF:
            print(term + " esta en el vocabulario")
            df = this.term_DF[term][0]
            pos = this.term_DF[term][1]
            print(" tiene un df: "+str(df) + " y una pos: "+str(pos) )
            s = struct.Struct("I" * df)
            file_read.seek(pos)  # me posiciono
            content = file_read.read(4*df)
            data = s.unpack(content)
            file_read.close()
            return set(data)
        else:
            print(term + " NO ESTA en el vocabulario")
            file_read.close()
            return set()

    def procesarQuery(this,query):
        """Recibe un string como query, lo parsea y busca los posting y opera con ellos"""
        elem = query.split()
        res1 = res2 = set()
        #query de una palabra
        if len(elem)==1:
            rta = this.buscarTerminos(elem[0])
        elif len(elem)==3:
            res1 = this.buscarTerminos(elem[0])
            res2 = this.buscarTerminos(elem[2])
            if elem[1] == "AND" or elem[1] == "and":
                rta = res1 & res2
            else:
                rta = res1 | res2
        elif len(elem)==4 and (elem[2]=="not" or elem[2]=="NOT"):
            res1 = this.buscarTerminos(elem[0])
            res2 = this.buscarTerminos(elem[3])
            rta = res1 - res2
        else:
            msj = """Query no valida, solo se permite:
            * un solo termino
            * termino and|or termino
            * termino and not termnino"""
            print(msj)
            return
        print("los archivos son:")
        if len(rta)==0:
            print("-- NO HAY RESULTADOS")
        for r in rta:
            print("- "+this.filesIndex[r])

    def minMaxAvgPostingSize(this):
        """saca los calculos de para el punto 2"""
        maxt = max = avg = 0
        min = len( this.terminos[next(iter(this.terminos))] )
        mint = next(iter(this.terminos))
        for t in this.terminos:
            posting = this.terminos[t]
            if len(posting) < min:
                min = len(posting)
                mint = t
            elif len(posting) > max:
                max = len(posting)
                maxt = t
            avg+=len(posting)
        avg= avg/len(this.terminos)
        return min, mint, max, maxt, avg

    def construirIndice(this):
        this.leerArchivos()
        this.guardarADisco()




