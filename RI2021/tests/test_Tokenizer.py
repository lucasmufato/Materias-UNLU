from unittest import TestCase

from SE.Tokenizer import Tokenizer


class TestTokenizer(TestCase):

    def setUp(self) -> None:
        self.tokenizer: Tokenizer = Tokenizer()

    def test_invoke(self):
        tokens = self.tokenizer.invoke("hola como andas")
        self.assertEqual(["hola", "como", "andas"], tokens)

    # def test_invoke_mails(self):
    #     tokens = self.tokenizer.invoke("hola como andas lucas@mufato.com")
    #     self.assertCountEqual(["lucas@mufato.com", "hola", "como", "andas"], tokens)

    def test_sacar_palabras_vacias_empty_list(self):
        tokens = self.tokenizer.sacar_palabras_vacias(["un", "par", "de", "palabras"], None)
        self.assertEqual(["un", "par", "de", "palabras"], tokens)

    def test_sacar_palabras_vacias(self):
        tokens = self.tokenizer.sacar_palabras_vacias(["un", "par", "de", "palabras", "de"], ["un","de","la"])
        self.assertEqual(["par", "palabras"], tokens)

    def test_invoke_mails(self):
        tokens = self.tokenizer.extract_mails("hola soy lucas mi mail es lucas.mufato@etermax.com en el trabajo mientras que es l.mufato@gmail.com en mi personal , tengo un amigo que es john_doe-weelkin@eng.uk.dot")
        self.assertCountEqual(["lucas.mufato@etermax.com","l.mufato@gmail.com","john_doe-weelkin@eng.uk.dot"], tokens)