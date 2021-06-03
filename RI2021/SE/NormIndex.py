import math
from typing import Dict

from SE.IdfIndex import IDFIndex
from SE.Vocabulary import Vocabulary


class NormIndex:
    """
    indice tipo
    doc=1 : norma=3.22
    """

    def __init__(self, idf_index: IDFIndex) -> None:
        self.idf_index = idf_index
        self.norm_index: Dict[int, float] = {}

    def calculate_norma_for_document(self, vocabulary: Vocabulary) -> None:
        # esta logica no deberia ir aca por que le pide los datos al vocabulario
        for term, posting in vocabulary.get_terminos().items():
            for doc, freq in posting.items():
                if doc not in self.norm_index:
                    self.norm_index[doc] = self.__cuadrado_tf_por_idf(term, freq)
                else:
                    self.norm_index[doc] += self.__cuadrado_tf_por_idf(term, freq)
        for doc, acumulado in self.norm_index.items():
            self.norm_index[doc] = math.sqrt(acumulado)

    def get_norma_for_doc(self, doc_id: int) -> float:
        if doc_id not in self.norm_index:
            return 0
        return self.norm_index[doc_id]

    def calculate_norma_for_query(self, query: Dict[str, int]) -> float:
        accumulated = 0
        for term, tf in query.items():
            accumulated += self.__cuadrado_tf_por_idf(term, tf)
        return math.sqrt(accumulated)

    def __cuadrado_tf_por_idf(self, term: str, tf: int) -> float:
        peso = tf * self.idf_index.get_idf_for(term)
        return peso * peso
