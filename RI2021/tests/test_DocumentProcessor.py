from unittest import TestCase

from SE.core.indexs.DocumentIndex import DocumentIndex
from SE.io.DocumentProcessor import DocumentProcessor
from SE.statistics.DocumentStatistic import CorpusStatistics
from SE.tokenizers.Tokenizer import Tokenizer
from SE.core.indexs.Vocabulary import Vocabulary

class TestDocumentProcessor(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.statistics = CorpusStatistics()
        self.vocabulary = Vocabulary()
        self.index = DocumentIndex()
        self.processor = DocumentProcessor(Tokenizer(), self.statistics, self.vocabulary, self.index)

    def test_one_file(self):
        """
        this is a very very very short text text
        that is not long
        """
        self.processor.process_file("files/three.txt", [])
        self.assertEqual(1, self.index.getDocumentAmount())
        # 9 es el tamaño del vocabulario
        self.assertEqual(9, len(self.vocabulary.get_terminos()) )
        # 10 es la cantidad de terminos extraidos de cada linea
        self.assertEqual(10, self.statistics.get_cant_terminos() )
        self.assertEqual(13, self.statistics.get_cant_tokens() )
