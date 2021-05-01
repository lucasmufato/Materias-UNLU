import sys

from SE.DocumentIndex import DocumentIndex
from SE.DocumentProcessor import DocumentProcessor
from SE.DocumentStatistic import CorpusStatistics
from SE.EmptyFiles import leerListaVacia
from SE.SearchEngine import SearchEngine
from SE.Steammers import SnowBallSpanishStemmer
from SE.Tokenizer import SimpleTokenizer, Tokenizer
from SE.Vocabulary import Vocabulary

palabrasVacias = [""]
carpeta = "..files/"
punto = 1

if len(sys.argv) == 3:
    punto = sys.argv[1]
    carpeta = sys.argv[2]
elif len(sys.argv) == 4:
    punto = sys.argv[1]
    carpeta = sys.argv[2]
    palabrasVacias = leerListaVacia("../emptyWords/vacias.txt", "\n")
else:
    print(
        "Mal paso de parametros! invocalo con: nroPunto directorioAIndexar pathPalabrasVacias")
    print(
        "ej: python3 main.py 2 ../RI-tknz-data/ ../emptyWords/vacias.txt")
    sys.exit(-1)


statistics = CorpusStatistics()
vocabulary = Vocabulary()
document_index = DocumentIndex()

if punto == "1":
    processor = DocumentProcessor(SimpleTokenizer(), statistics, vocabulary, document_index)
    se = SearchEngine(statistics, vocabulary, processor)
    se.search(carpeta, palabrasVacias)
elif punto == "2":
    processor = DocumentProcessor(Tokenizer(), statistics, vocabulary, document_index)
    se = SearchEngine(statistics, vocabulary, processor)
    se.search(carpeta, palabrasVacias)
    statistics.armar_archivos(vocabulary, document_index)
elif punto == "3":
    componente = "(?:\d*[A-Z][a-z]?\d?)+"
    c_sin_match = f"(?:{componente})"
    c_con_match = f"({componente})"
    expresion = f"{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match}\\s)*[\\=\\-]\\>\\s*{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match})*"
    processor = DocumentProcessor(Tokenizer([c_con_match, expresion]), statistics, vocabulary, document_index)
    se = SearchEngine(statistics, vocabulary, processor)
    se.search(carpeta, palabrasVacias)
elif punto == "4":
    processor = DocumentProcessor(Tokenizer(), statistics, vocabulary, document_index, SnowBallSpanishStemmer())
    se = SearchEngine(statistics, vocabulary, processor)
    se.search(carpeta, palabrasVacias)
else:
    print("Le erraste con el punto del tp")
    sys.exit(-1)
