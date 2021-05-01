import unittest
from unittest.mock import Mock

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
        self.processor = Mock()
        self.engine: SearchEngine = SearchEngine(self.statistics, self.vocabulary, self.processor)

    def test_reads_all_files(self):
        self.engine.scan_directory("files/", [])
        self.processor.process_file.assert_any_call("files/one.txt", [])
        self.processor.process_file.assert_any_call("files/two.txt", [])
        self.processor.process_file.assert_any_call("files/three.txt", [])

    # def test_statistics(self):
    #     self.engine.scan_directory("files/", [])
    #     self.assertEqual(106, self.statistics.cant_tokens)
    #     self.assertEqual(91, self.statistics.cant_terminos)
    #     self.assertEqual(2, self.statistics.cant_docs)