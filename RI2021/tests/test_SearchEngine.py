import unittest
from unittest.mock import Mock

from SE.SearchEngine import SearchEngine


class TestSearchEngine(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.processor = Mock()
        self.engine: SearchEngine = SearchEngine(self.processor)

    def test_reads_all_files(self):
        self.engine.scan_directory("files/", [])
        self.processor.process_file.assert_any_call("files/one.txt", [])
        self.processor.process_file.assert_any_call("files/two.txt", [])
        self.processor.process_file.assert_any_call("files/three.txt", [])
