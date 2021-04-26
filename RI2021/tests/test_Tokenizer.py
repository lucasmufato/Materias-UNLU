from unittest import TestCase

from SE.Tokenizer import Tokenizer


class TestTokenizer(TestCase):

    def setUp(self) -> None:
        self.tokenizer: Tokenizer = Tokenizer()

    def test_invoke_simple(self):
        tokens = self.tokenizer.invoke("hola como andas")
        self.assertEqual(["hola", "como", "andas"], tokens)

    def test_sacar_palabras_vacias_empty_list(self):
        tokens = self.tokenizer.sacar_palabras_vacias(["un", "par", "de", "palabras"], None)
        self.assertEqual(["un", "par", "de", "palabras"], tokens)

    def test_sacar_palabras_vacias(self):
        tokens = self.tokenizer.sacar_palabras_vacias(["un", "par", "de", "palabras", "de"], ["un", "de", "la"])
        self.assertEqual(["par", "palabras"], tokens)

    def test_invoke_mails(self):
        tokens = self.tokenizer.extract_mails( "mi mail es lucas.mufato@etermax.com en el trabajo mientras que es l.mufato@gmail.com en mi personal, tengo un amigo que es john_doe-weelkin@eng.uk.dot")
        self.assertCountEqual(["lucas.mufato@etermax.com", "l.mufato@gmail.com", "john_doe-weelkin@eng.uk.dot"], tokens)

    def test_sacar_acentos(self):
        tokens = self.tokenizer.sacar_acentos("Hola, soy una palàbrá rara con varíós acéntos")
        self.assertEqual("Hola, soy una palabra rara con varios acentos", tokens)

    def test_sacar_fechas(self):
        tokens = self.tokenizer.extraer_fechas("hoy es 22/4/2021, la ultima vez que curse RI fue en el 2019, creo q el 8-5-19")
        self.assertCountEqual(["22/4/2021", "8-5-19"], tokens)

    def test_sacar_abreviaturas(self):
        tokens = self.tokenizer.extraer_abreviaturas("hoy es 22/4/2021, visite u.s.a y A.R.G")
        self.assertCountEqual([ "u.s.a", "A.R.G"], tokens)

    def test_sacar_urls(self):
        tokens = self.tokenizer.extraer_urls("mi pagina es https://mufato.com.ar")
        self.assertCountEqual(["https://mufato.com.ar"], tokens)

    def test_sacar_mails(self):
        tokens = self.tokenizer.extract_mails("este es mi mail lucas@gmail.com y lucas.mufato@etermax.com.ar")
        self.assertCountEqual(["lucas@gmail.com", "lucas.mufato@etermax.com.ar"], tokens)

    def test_sacar_nros(self):
        tokens = self.tokenizer.extraer_nros("hola, esto salio 200.50$ y tambien viene con 0.2 aumento + 12,12 extra")
        self.assertCountEqual(["200.50", "0.2", "12,12"], tokens)

    def test_sacar_caracteres(self):
        tokens = self.tokenizer.sacar_caracteres("hola, como andas... todo bien? +=!#$ - _ aca al 20%")
        self.assertEqual("hola como andas todo bien aca al 20", tokens)

    def test_invoke_completo(self):
        tokens = self.tokenizer.invoke("hola como andàs Maíl lucas@gmail.com naci.' ' el, 11/4/1992 con el             "
                                       "      20%")
        self.assertCountEqual(["hola", "como", "andas", "mail", "lucas@gmail.com", "naci", "el", "11/4/1992","con","el","20"], tokens)

    def test_optional_chemical(self):
        self.tokenizer = Tokenizer(["((?:\d*[A-Z][a-z]?\d?)+)"])
        tokens = self.tokenizer.invoke("68.03 oxigeno (O2) 23.15")
        self.assertCountEqual(["68.03", "oxigeno", "O2", "23.15"], tokens)

    def test_optional_chemical_2(self):
        self.tokenizer = Tokenizer(["((?:\d*[A-Z][a-z]?\d?)+)"])
        tokens = self.tokenizer.invoke("se descompone el óxido. Hg + O => HgO")
        self.assertCountEqual(["se", "descompone", "el", "oxido", "Hg", "O", "HgO"], tokens)

    def test_optional_chemical_expresion(self):
        f = "(?:(?:\d*[A-Z][a-z]?\d?)+)"
        expresion = f + "\s*(?:[\+\-]\s*" + f + "\s)*[\=\-]\>\s*" + f + "\s*(?:[\+\-]\s*" + f + ")*"
        self.tokenizer = Tokenizer([expresion])
        tokens = self.tokenizer.invoke("se descompone el óxido. Hg + O => HgO")
        self.assertCountEqual(["se", "descompone", "el", "oxido", "Hg + O => HgO"], tokens)

    def test_optional_chemical_complete(self):
        componente = "(?:\d*[A-Z][a-z]?\d?)+"
        c_sin_match = f"(?:{componente})"
        c_con_match = f"({componente})"
        expresion = f"{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match}\\s)*[\\=\\-]\\>\\s*{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match})*"
        self.tokenizer = Tokenizer([c_con_match, expresion])
        tokens = self.tokenizer.invoke("se descompone el óxido. Hg + O => HgO")
        self.assertCountEqual(["se", "descompone", "el", "oxido", "Hg + O => HgO", "Hg", "O", "HgO"], tokens)

    def test_optional_chemical_complete_sin_match(self):
        componente = "(?:\d*[A-Z][a-z]?\d?)+"
        c_sin_match = f"(?:{componente})"
        c_con_match = f"({componente})"
        expresion = f"{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match}\\s)*[\\=\\-]\\>\\s*{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match})*"
        self.tokenizer = Tokenizer([c_con_match, expresion])
        tokens = self.tokenizer.invoke("se descompone el óxido")
        self.assertCountEqual(["se", "descompone", "el", "oxido"], tokens)
