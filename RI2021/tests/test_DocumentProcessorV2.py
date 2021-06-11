from unittest import TestCase
from unittest.mock import Mock

from SE.core.indexs.DocumentIndex import DocumentIndex
from SE.io.DocumentProcessorV2 import DocumentProcessorV2
from SE.io.EmptyWords import EmptyWords
from SE.tokenizers.Tokenizer import Tokenizer


class TestDocumentProcessorV2(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.vocabulary = Mock()
        self.index = DocumentIndex()
        self.empty_words = EmptyWords(["la"])
        self.processor = DocumentProcessorV2(Tokenizer(), self.vocabulary, self.index, self.empty_words)

    def test_one_file(self):
        self.processor.process_file("files/three.txt", "contenido del archivo leido la la")
        self.assertEqual(1, self.index.getDocumentAmount())
        self.vocabulary.agregar.assert_called_with(["contenido","del","archivo","leido"], 0)

