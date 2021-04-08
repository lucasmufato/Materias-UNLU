from unittest import TestCase

from SE.Tokenizer import Tokenizer


class TestTokenizer(TestCase):

    def setUp(self) -> None:
        self.tokenizer: Tokenizer = Tokenizer()

    def test_invoke(self):
        tokens = self.tokenizer.invoke("hola como andas")
        self.assertEqual(["hola", "como", "andas"], tokens)

    def test_invoke_mails(self):
        tokens = self.tokenizer.invoke("hola como andas lucas@mufato.com")
        self.assertCountEqual(["lucas@mufato.com", "hola", "como", "andas"], tokens)