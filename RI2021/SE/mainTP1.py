import sys
import time

from SE.DocumentIndex import DocumentIndex
from SE.DocumentProcessor import DocumentProcessor
from SE.DocumentStatistic import CorpusStatistics
from SE.EmptyFiles import leerListaVacia
from SE.SearchEngine import SearchEngine
from SE.Steammers import SnowBallSpanishStemmer, MyPorterStemmer, MyLancasterStemmer
from SE.Tokenizer import SimpleTokenizer, Tokenizer
from SE.Vocabulary import Vocabulary


def read_script_params():
    palabrasVacias = [""]
    carpeta = "..files/"
    punto = 1
    if len(sys.argv) == 3:
        punto = sys.argv[1]
        carpeta = sys.argv[2]
    elif len(sys.argv) == 4:
        punto = sys.argv[1]
        carpeta = sys.argv[2]
        palabrasVacias = leerListaVacia(sys.argv[3], "\n")
    else:
        print(
            "Mal paso de parametros! invocalo con: nroPunto directorioAIndexar pathPalabrasVacias")
        print(
            "ej: python3 mainTP1.py 2 ../RI-tknz-data/ ../emptyWords/vacias.txt")
        sys.exit(-1)
    return palabrasVacias, carpeta, punto


palabrasVacias, carpeta, punto = read_script_params()

statistics = CorpusStatistics()
vocabulary = Vocabulary()
document_index = DocumentIndex()
inicio = time.time()
if punto == "1":
    processor = DocumentProcessor(SimpleTokenizer(), statistics, vocabulary, document_index)
    se = SearchEngine(processor)
    se.search(carpeta, palabrasVacias)
elif punto == "2":
    processor = DocumentProcessor(Tokenizer(), statistics, vocabulary, document_index)
    se = SearchEngine(processor)
    se.search(carpeta, palabrasVacias)
elif punto == "3":
    componente = "(?:\d*[A-Z][a-z]?\d?)+"
    c_sin_match = f"(?:{componente})"
    c_con_match = f"({componente})"
    expresion = f"{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match}\\s)*[\\=\\-]\\>\\s*{c_sin_match}\\s*(?:[\\+\\-]\\s*{c_sin_match})*"
    processor = DocumentProcessor(Tokenizer([c_con_match, expresion]), statistics, vocabulary, document_index)
    se = SearchEngine(processor)
    se.search(carpeta, palabrasVacias)
elif punto == "4":
    processor = DocumentProcessor(Tokenizer(), statistics, vocabulary, document_index, SnowBallSpanishStemmer())
    se = SearchEngine(processor)
    se.search(carpeta, palabrasVacias)
elif punto == "5P":
    processor = DocumentProcessor(Tokenizer(), statistics, vocabulary, document_index, MyPorterStemmer())
    se = SearchEngine(processor)
    se.search(carpeta, palabrasVacias)
elif punto == "5L":
    processor = DocumentProcessor(Tokenizer(), statistics, vocabulary, document_index, MyLancasterStemmer())
    se = SearchEngine(processor)
    se.search(carpeta, palabrasVacias)
else:
    print("Le erraste con el punto del tp")
    sys.exit(-1)

statistics.armar_archivos(vocabulary, document_index)
print("tardo " + str(time.time() - inicio))