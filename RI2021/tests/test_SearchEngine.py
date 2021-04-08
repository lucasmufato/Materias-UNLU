import unittest
from unittest.mock import Mock, call, MagicMock

from SE.SearchEngine import SearchEngine
from SE.Tokenizer import Tokenizer


class TestSearchEngine(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.tokenizer: Tokenizer = Tokenizer()
        self.tokenizer.invoke = MagicMock()
        self.engine: SearchEngine = SearchEngine(self.tokenizer)

    def test_reads_all_files_in_folders_splits_and_calls_tokenizer(self):
        self.engine.scan_directory("files/")

        self.tokenizer.invoke.assert_has_calls([
            call("other\n"),
            call("sarasa"),
            call("sarasa")
        ])


if __name__ == '__main__':
    unittest.main()
