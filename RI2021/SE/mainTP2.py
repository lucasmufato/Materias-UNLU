import sys
import time

from SE.DocumentIndex import DocumentIndex
from SE.DocumentProcessor import DocumentProcessor
from SE.DocumentStatistic import CorpusStatistics
from SE.EmptyFiles import leerListaVacia
from SE.SearchEngine import SearchEngine
from SE.Tokenizer import Tokenizer
from SE.Vocabulary import Vocabulary

palabrasVacias = [""]
carpeta = "..files/"
punto = 1

if len(sys.argv) == 2:
    carpeta = sys.argv[1]
elif len(sys.argv) == 3:
    carpeta = sys.argv[1]
    palabrasVacias = leerListaVacia( sys.argv[2], "\n")
else:
    print(
        "Mal paso de parametros! invocalo con: nroPunto directorioAIndexar pathPalabrasVacias")
    print(
        "ej: python3 mainTP2.py ../RI-tknz-data/ ../emptyWords/vacias.txt")
    sys.exit(-1)


statistics = CorpusStatistics()
vocabulary = Vocabulary()
document_index = DocumentIndex()
inicio = time.time()
tokenizer = Tokenizer()
processor = DocumentProcessor(tokenizer, statistics, vocabulary, document_index)
se = SearchEngine(processor)
se.search(carpeta, palabrasVacias)
statistics.armar_archivos(vocabulary, document_index)
print("tardo " + str(time.time() - inicio))
# QueryInterface()
