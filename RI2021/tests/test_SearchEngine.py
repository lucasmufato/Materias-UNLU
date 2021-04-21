import unittest
from unittest.mock import Mock, call, MagicMock

from SE.DocumentStatistic import CorpusStatistics
from SE.SearchEngine import SearchEngine
from SE.Tokenizer import SimpleTokenizer
from SE.Vocabulary import Vocabulary


class TestSearchEngine(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.tokenizer = SimpleTokenizer()
        self.statistics = CorpusStatistics()
        self.vocabulary = Vocabulary()
        self.engine: SearchEngine = SearchEngine(self.tokenizer, self.statistics, self.vocabulary)

    def test_statistics(self):
        self.engine.scan_directory("files/")
        self.assertEqual(106, self.statistics.cant_tokens)
        self.assertEqual(91, self.statistics.cant_terminos)
        self.assertEqual(2, self.statistics.cant_docs)

if __name__ == '__main__':
    unittest.main()
