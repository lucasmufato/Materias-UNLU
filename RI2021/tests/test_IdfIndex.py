from unittest import TestCase

from SE.TFxIDF.IdfIndex import IDFIndex
from SE.core.indexs.Vocabulary import Vocabulary


class TestIDFIndex(TestCase):
    vocabulary = Vocabulary()
    idfIndex = IDFIndex()

    def test_idf_calc_from_book_example(self):
        self.given_book_example()

        self.idfIndex.calculate_from_vocabulary(self.vocabulary, 5)

        self.assertEqual(2.32, self.get_rounded_idf_for("rueda"))
        self.assertEqual(2.32, self.get_rounded_idf_for("carter"))
        self.assertEqual(1.32, self.get_rounded_idf_for("espejo"))
        self.assertEqual(0.32, self.get_rounded_idf_for("caja"))
        self.assertEqual(1.32, self.get_rounded_idf_for("puerta"))
        self.assertEqual(0.74, self.get_rounded_idf_for("filtro"))

    def given_book_example(self):
        self.vocabulary.agregar({"espejo": 1, "caja": 1, "puerta": 1}, 1)
        self.vocabulary.agregar({"puerta": 2, "filtro": 1}, 2)
        self.vocabulary.agregar({"espejo": 1, "caja": 1, "filtro": 1}, 3)
        self.vocabulary.agregar({"rueda": 1, "caja": 1, "filtro": 1}, 4)
        self.vocabulary.agregar({"carter": 1, "caja": 2}, 5)

    def get_rounded_idf_for(self, term:str):
        return round(self.idfIndex.get_idf_for(term), 2)