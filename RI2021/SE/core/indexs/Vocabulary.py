from typing import Dict


class Vocabulary:
    """
    Arma una diccionario del tipo:
    "perro" : {doc1: 32, doc2:2}
    "casa" : {doc2: 2, doc3:4}
    """

    def __init__(self):
        self.__terminos: Dict[str, Dict[int, int]] = {}

    def agregar(self, nuevos_terminos: Dict[str, int], docId: int) -> None:
        for term, cant in nuevos_terminos.items():
            if term in self.__terminos:
                self.__actualizar_posting(docId, term, cant)
            else:
                self.__insertar_postlist(docId, term, cant)

    def __insertar_postlist(self, docId:int, term:str, cant:int):
        self.__terminos[term] = {docId: cant}

    def __actualizar_posting(self, docId:int, term:str, cant:int):
        posting = self.__terminos[term]
        if docId in posting:
            posting[docId] += cant
            self.__terminos[term] = posting
        else:
            posting[docId] = cant
            self.__terminos[term] = posting

    def get_terminos(this) -> Dict[str, Dict[int, int]]:
        return this.__terminos

    def get_document_frequency(self, term: str) -> int:
        if term not in self.__terminos:
            return 0
        return len(self.__terminos[term])

    def get_termn_frequency(self, term: str) -> int:
        if term not in self.__terminos:
            return 0
        posting: dict = self.__terminos[term]
        return sum(posting.values())

    def get_posting(self, term) -> Dict[int, int]:
        if term not in self.__terminos:
            return {}
        return self.__terminos[term]

    def get_terms(self):
        return self.__terminos.keys()
