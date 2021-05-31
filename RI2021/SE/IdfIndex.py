import math

from SE.Vocabulary import Vocabulary


class IDFIndex:
    """
    indice estilo
    perro : 1.75
    casa : 0.31
    """

    def __init__(self) -> None:
        super().__init__()
        self.__index = {}

    def calculate_from_vocabulary(self, vocabulary: Vocabulary, total_amount_of_documents: int):
        for term in vocabulary.get_terms():
            self.__index[term] = self.calculate_idf(vocabulary.get_document_frequency(term), total_amount_of_documents)

    def get_idf_for(self, term: str) -> float:
        if term not in self.__index:
            return 0
        return self.__index[term]

    def calculate_idf(self, df: int, all_documents: int) -> float:
        return math.log2(all_documents/df)