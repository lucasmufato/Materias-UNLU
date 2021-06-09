from unittest import TestCase
from unittest.mock import Mock

from SE.TFxIDF.IdfIndex import IDFIndex
from SE.TFxIDF.NormIndex import NormIndex
from SE.core.indexs.Vocabulary import Vocabulary


class TestNormIndex(TestCase):

    def setUp(self) -> None:
        self.vocabulary: Vocabulary = Vocabulary()


    def test_calculate_norma_for_query(self):
        # dada la query devuelve los idfs del ejemplo
        self.idf_index: IDFIndex = Mock()
        self.norm_index = NormIndex(self.idf_index)
        query = {"carter": 2, "puerta": 1, "filtro": 1}
        self.idf_index.get_idf_for.side_effect = [2.32, 1.32, 0.74]
        # when get norm
        norm = self.norm_index.calculate_norma_for_query(query)
        # then q norm is 4.88
        self.assertEqual(4.88, round(norm, 2))

    def test_calculate_norma_for_documents(self):
        self.given_book_example()
        self.idf_index = IDFIndex()
        self.norm_index = NormIndex(self.idf_index)
        self.idf_index.calculate_from_vocabulary(self.vocabulary, 5)
        # when
        self.norm_index.calculate_norma_for_document(self.vocabulary)
        # then
        self.assertEqual(1.90, self.rounded_doc_norma_for(doc=1))
        self.assertEqual(2.74, self.rounded_doc_norma_for(doc=2))
        self.assertEqual(1.55, self.rounded_doc_norma_for(doc=3))
        self.assertEqual(2.46, self.rounded_doc_norma_for(doc=4))
        self.assertEqual(2.41, self.rounded_doc_norma_for(doc=5))

    def given_book_example(self):
        self.vocabulary.agregar({"espejo": 1, "caja": 1, "puerta": 1}, 1)
        self.vocabulary.agregar({"puerta": 2, "filtro": 1}, 2)
        self.vocabulary.agregar({"espejo": 1, "caja": 1, "filtro": 1}, 3)
        self.vocabulary.agregar({"rueda": 1, "caja": 1, "filtro": 1}, 4)
        self.vocabulary.agregar({"carter": 1, "caja": 2}, 5)

    def rounded_doc_norma_for(self, doc: int) -> float:
        return round(self.norm_index.get_norma_for_doc(doc), 2)
