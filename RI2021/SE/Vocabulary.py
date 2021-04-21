class Vocabulary:
    """
    Arma una diccionario del tipo:
    "perro" : {doc1: 32, doc2:2}
    "casa" : {doc2: 2, doc3:4}
    """

    def __init__(self):
        self.terminos: dict = {}

    def agregar(self, terminos: dict, docId: int):
        for term, cant in terminos.items():
            if term in self.terminos:
                self.__actualizar_posting(docId, term, cant)
            else:
                self.__insertar_postlist(docId, term, cant)

    def __insertar_postlist(self, docId, term, cant):
        self.terminos[term] = {docId: cant}

    def __actualizar_posting(self, docId, term, cant):
        posting = self.terminos[term]
        if docId in posting:
            posting[docId] += cant
            self.terminos[term] = posting
        else:
            posting[docId] = cant
            self.terminos[term] = posting

    def get_terminos(this):
        return this.terminos

    def get_document_frequency(self, term: str):
        if term not in self.terminos:
            return 0
        return len(self.terminos[term])

    def get_termn_frequency(self, term: str):
        if term not in self.terminos:
            return 0
        posting: dict = self.terminos[term]
        return sum(posting.values())
