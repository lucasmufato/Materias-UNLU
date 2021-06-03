from unittest import TestCase

from SE.IdfIndex import IDFIndex
from SE.NormIndex import NormIndex
from SE.QueryProcessor import QueryProcessor
from SE.Vocabulary import Vocabulary


class TestQueryProcessor(TestCase):
    vocabulary = Vocabulary()
    idf = IDFIndex()
    normas: NormIndex = NormIndex(idf)
    processor = QueryProcessor(vocabulary, idf, normas)

    def test_sacado_del_libro_de_tolosa(self):
        # given
        self.given_vocabulary_with_book_example()
        self.given_calcule_idfs()
        self.given_calcule_normas()
        query_representation = {"carter": 2, "puerta": 1, "filtro": 1}

        ranking = self.processor.process(query_representation)

        self.assertEqual(5, ranking[0].doc_id)
        self.assertEqual(0.92, round(ranking[0].weight,2))
        self.assertEqual(2, ranking[1].doc_id)
        self.assertEqual(0.30, round(ranking[1].weight,2))
        self.assertEqual(1, ranking[2].doc_id)
        self.assertEqual(0.19, round(ranking[2].weight,2))
        self.assertEqual(3, ranking[3].doc_id)
        self.assertEqual(0.07, round(ranking[3].weight,2))
        self.assertEqual(4, ranking[4].doc_id)
        self.assertEqual(0.05, round(ranking[4].weight,2))

    def given_vocabulary_with_book_example(self):
        self.vocabulary.agregar({"espejo": 1, "caja": 1, "puerta": 1}, 1)
        self.vocabulary.agregar({"puerta": 2, "filtro": 1}, 2)
        self.vocabulary.agregar({"espejo": 1, "caja": 1, "filtro": 1}, 3)
        self.vocabulary.agregar({"rueda": 1, "caja": 1, "filtro": 1}, 4)
        self.vocabulary.agregar({"carter": 1, "caja": 2}, 5)

    def given_calcule_idfs(self):
        self.idf.calculate_from_vocabulary(self.vocabulary, 5)

    def given_calcule_normas(self):
        self.normas.calculate_norma_for_document(self.vocabulary)

