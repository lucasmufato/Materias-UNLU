from SE.Vocabulary import Vocabulary


class DocumentStatistics:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.nro_term = 0
        self.nro_tokens = 0

    def increase_tokens(self, tokens):
        self.nro_tokens += tokens

    def increase_terms(self, terms):
        self.nro_term += terms


class CorpusStatistics:

    def __init__(self) -> None:
        super().__init__()
        self.cant_terminos = 0
        self.cant_tokens = 0
        self.cant_docs = 0

    def increase_tokens(self, tokens):
        self.cant_tokens += tokens

    def increase_terms(self, terms):
        self.cant_terminos += terms

    def increase_docs(self):
        self.cant_docs += 1

    def armar_terminos_txt(self, vocabulario: Vocabulary):
        print("armando terminos.txt ...")
        file = open("terminos.txt", 'w')
        od = vocabulario.get_terminos().copy().items()
        od = sorted(od, key=lambda x: x[0])
        # lista de tuplas( termino, {fileId:repeticion})
        for tupla in od:
            # tupla( termino, {fileId:repeticion})
            cf = 0
            for fileId in tupla[1]:
                cf += tupla[1][fileId]
            file.write(tupla[0] + "\t\t  -CF: " + str(cf) + "\t\t  -DF: " + str(len(tupla[1])) + " \r\n")
        file.close()
        print("fin terminos")

    def armar_estadisticas_txt(self, vocabulario: Vocabulary, documentos: list):
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
        file.write("cant documentos: {0} \r\n".format(str(cantDocumentos)))
        file.write("cantidad tokens: {0}\t\t cantidad terminos: {1} \r\n".format(str(self.cant_tokens), str(len(vocabulario.terminos))))
        file.write("promedio tokens: {0}\t\t promedio terminos: {1} \r\n".format(str(self.cant_tokens / cantDocumentos), str(len(vocabulario.terminos) / cantDocumentos)))
        file.write("largo promedio token: {0} \r\n".format(str(long)))
        shortest_file = min(documentos, key=lambda x: x.nro_tokens)
        biggest_file = max(documentos, key=lambda x: x.nro_tokens)
        file.write("archivos mas corto es {2} -> tokens: {0}\t\t terminos: {1}\r\n".format(str(shortest_file.nro_tokens), str(shortest_file.nro_term), shortest_file.name))
        file.write("archivos mas largo es {2} -> tokens: {0}\t\t terminos: {1} \r\n".format(str(biggest_file.nro_tokens), str(biggest_file.nro_term),  shortest_file.name))
        file.write("Terminos que se repiten una vez:")
        for term in fewRepTerm:
            file.write("{0} \r\n".format(str(term)))
        file.close()
        print("fin estadisticas")

    def arma_frecuencias_txt(self, vocabulario: Vocabulary):
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
        file.write(str(maximos) + "\r\n")
        file.write(str(minimos) + "\r\n")
        file.close()
        print("fin frecuencias")