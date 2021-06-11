from typing import Dict, List


class PositionalVocabulary:
    """
        guarda en una estructura tipo:
        {
            "algo": {doc1: [1, 30, 500], doc3: [pos3 ,pos50, pos90]  }
            "casa": {doc2: [1, 30, 500], doc3: [pos3 ,pos50, pos90]  }
        }
    """
    def __init__(self):
        self.__terminos: Dict[str, Dict[int, List[int]]] = {}

    def agregar(self, positionated_terms: List[str], docId: int) -> None:
        for position, term in enumerate(positionated_terms):
            if term in self.__terminos:
                self.__actualizar_posting(docId, term, position)
            else:
                self.__insertar_postlist(docId, term, position)

    def __insertar_postlist(self, docId: int, term: str, position: int):
        self.__terminos[term] = {docId: [position]}

    def __actualizar_posting(self, docId: int, term: str, position: int):
        posting = self.__terminos[term]
        if docId in posting:
            posting[docId].append(position)
        else:
            posting[docId] = [position]

    def get_terminos(this) -> Dict[str, Dict[int, List[int]]]:
        return this.__terminos

    def get_document_frequency(self, term: str) -> int:
        if term not in self.__terminos:
            return 0
        return len(self.__terminos[term])

    def get_termn_frequency(self, term: str) -> int:
        if term not in self.__terminos:
            return 0
        posting: Dict[int, List[int]] = self.__terminos[term]
        count = 0
        for v in posting.values():
            count+=len(v)
        return count

    def get_posting(self, term) -> Dict[int, int]:
        # if term not in self.__terminos:
        #     return {}
        # return self.__terminos[term]
        # todo
        pass

    def get_terms(self):
        # return self.__terminos.keys()
        # todo
        pass
