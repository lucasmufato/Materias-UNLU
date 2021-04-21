from SE.DocumentStatistic import CorpusStatistics
from SE.EmptyFiles import leerListaVacia
from SE.SearchEngine import SearchEngine
from SE.Tokenizer import SimpleTokenizer
from SE.Vocabulary import Vocabulary


vacia = leerListaVacia("vacias.txt", "\n")
se = SearchEngine(SimpleTokenizer(), CorpusStatistics(), Vocabulary())
se.search("../files/")