from SearchEngine.Vocabulary import Vocabulary


class Estadisticas:

    cantTerminos = 0
    cantTokens = 0

    def armar_terminos_txt(this, vocabulario: Vocabulary):
        print("armando terminos.txt ...")
        file = open("terminos.txt", 'w')
        od = vocabulario.get_terminos().copy().items()
        od = sorted(od, key=lambda x: x[0])
        # lista de tuplas( termino, {fileId:repeticion})
        for tupla in od:
            # tupla( termino, {fileId:repeticion})
            cf = 0
            for fileId in tupla[1]:
                cf += tupla[1][fileId];
            file.write(tupla[0] + "\t\t  -CF: " + str(cf) + "\t\t  -DF: " + str(len(tupla[1])) + " \r\n")
        file.close()
        print("fin terminos")

    def armar_estadisticas_txt(this, vocabulario: Vocabulary, documentos: list):
        print("armando estadisticas.txt")
        cantDocumentos = len(documentos)
        long = 0
        fewRepTerm = []
        copia = vocabulario.get_terminos().copy()
        for termino in copia.keys():
            long += len(termino)
            postingDic = copia[termino]
            # si el termino esta una sola vez en la coleccion
            if len(postingDic) == 1:
                fileId, repeticiones = postingDic.popitem()
                if repeticiones == 1:
                    fewRepTerm.append(termino)
        long = long / len(copia)
        file = open("estadisticas.txt", "w")
        file.write( str(cantDocumentos) + " \r\n")
        file.write( str(this.cantTokens) + "\t\t" + str(len(copia)) + " \r\n")
        file.write( str(this.cantTokens / cantDocumentos) + "\t\t" + str(len(copia) / cantDocumentos) + " \r\n")
        file.write( str(long) + " \r\n")
        shortest_file = min(documentos, key=lambda x:x.nro_tokens)
        biggest_file = max(documentos, key=lambda  x:x.nro_tokens)
        file.write( str(shortest_file.nro_tokens) + "\t\t" + str(shortest_file.nro_term) + "\r\n")
        file.write(biggest_file.name + str(biggest_file.nro_tokens) + "\t\t" + str(biggest_file.nro_term) + " \r\n")
        for term in fewRepTerm:
            file.write( str(term) + " \r\n")
        file.close()
        print("fin estadisticas")


    def arma_frecuencias_txt(this, vocabulario: Vocabulary):
        print("inicio frecuencias.txt")
        ter = 10
        minimos = []
        maximos = []
        vocab = vocabulario.get_terminos()
        for termino in vocab.keys():
            postingDic = vocab[termino]
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
        file = open("frecuencias.txt", "w")
        file.write( str(maximos) + "\r\n")
        file.write( str(minimos) + "\r\n")
        file.close()
        print("fin frecuencias")



