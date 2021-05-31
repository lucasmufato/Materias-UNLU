from unittest import TestCase

from SE.IdfIndex import IDFIndex
from SE.QueryProcessor import QueryProcessor
from SE.Vocabulary import Vocabulary


class TestQueryProcessor(TestCase):
    vocabulary = Vocabulary()
    idf = IDFIndex()
    processor = QueryProcessor()

    def test_return_one_matching_document(self):
        # given
        self.vocabulary.agregar({"casa": 1, "perro": 1}, 1)
        self.vocabulary.agregar({"casa": 1, "tero": 1}, 2)
        self.idf.calculate_from_vocabulary(self.vocabulary, total_amount_of_documents=2)
        query = {""}

        # when

