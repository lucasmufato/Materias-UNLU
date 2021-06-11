import unittest

from SE.core.indexs.PositionalVocabulary import PositionalVocabulary
from SE.core.indexs.Vocabulary import Vocabulary


class test_PositionalVocabulary(unittest.TestCase):

    def test_insertar_un_termino(self):
        v = PositionalVocabulary()
        v.agregar(["casa", "perro"], 1)
        self.assertEqual({"casa": {1: [0]}, "perro": {1: [1]}}, v.get_terminos())

    def test_actualizar_repeticiones_de_un_termino(self):
        v = PositionalVocabulary()
        v.agregar(["casa", "perro"], 1)
        v.agregar(["tomate", "perro"], 2)
        self.assertEqual({"casa": {1: [0]}, "perro": {1: [1], 2:[1]}, "tomate": {2: [0]}}, v.get_terminos())

    def test_añadir_2_documentos(self):
        v = PositionalVocabulary()
        v.agregar(["casa", "perro", "tomate", "perro"], 1)
        self.assertEqual({"casa": {1: [0]}, "perro": {1: [1,3]}, "tomate": {1: [2]}}, v.get_terminos())

    def test_Document_Frequency(self):
        v = PositionalVocabulary()
        v.agregar(["casa", "perro"], 1)
        v.agregar(["tomate", "perro"], 2)
        self.assertEqual(2, v.get_document_frequency("perro"))
        self.assertEqual(1, v.get_document_frequency("casa"))
        self.assertEqual(1, v.get_document_frequency("tomate"))

    def test_Termn_Frequency(self):
        v = PositionalVocabulary()
        v.agregar(["casa", "perro"], 1)
        v.agregar(["tomate", "perro"], 2)
        self.assertEqual(2, v.get_termn_frequency("perro"))
        self.assertEqual(1, v.get_termn_frequency("casa"))
        self.assertEqual(1, v.get_termn_frequency("tomate"))

    # def test_get_postlists(self):
    #     v = PositionalVocabulary()
    #     v.agregar({"casa": 1, "perro": 2}, 1)
    #     v.agregar({"tomate": 1, "perro": 1}, 2)
    #     self.assertEqual({1: 1}, v.get_posting("casa"))
    #     self.assertEqual({1: 2, 2: 1}, v.get_posting("perro"))