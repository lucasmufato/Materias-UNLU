from unittest import TestCase

from SE.Steammers import SnowBallSpanishStemmer, MyPorterStemmer, MyLancasterStemmer


class TestDictionaryStemmer(TestCase):

    def test_spanish_steamer(self):
        steamer = SnowBallSpanishStemmer()
        token = steamer.stemear_token("computadora")
        self.assertEqual("comput", token)
        token = steamer.stemear_token("computar")
        self.assertEqual("comput", token)

    def test_spanish_steamer_dict(self):
        steamer = SnowBallSpanishStemmer()
        token = steamer.stemear_dict({"computadora": 2})
        self.assertEqual({"comput": 2}, token)

    def test_spanish_steamer_two_words_with_same_root(self):
        steamer = SnowBallSpanishStemmer()
        token = steamer.stemear_dict({"computadora": 2, "computar": 1})
        self.assertEqual({"comput": 3}, token)

    def test_spanish_steamer_many_words(self):
        steamer = SnowBallSpanishStemmer()
        token = steamer.stemear_dict({"computadora": 2, "computar": 1, "cocinar": 2, "cocina": 10, "ser": 1})
        self.assertEqual({"comput": 3, "cocin": 12, "ser": 1}, token)

    def test_porter_steamer_many_words(self):
        steamer = MyPorterStemmer()
        token = steamer.stemear_dict({"cook": 2, "cooker": 1, "cooking": 2, "course": 10, "being": 1})
        self.assertEqual({"cook": 4, "cours": 10, "cooker": 1, "be": 1}, token)

    def test_lancaster_steamer_many_words(self):
        steamer = MyLancasterStemmer()
        token = steamer.stemear_dict({"cook": 2, "cooker": 1, "cooking": 2, "course": 10, "being": 1})
        self.assertEqual({"cook": 5, "cours": 10, "being": 1}, token)