import sys
import time

from SE.DocumentIndex import DocumentIndex
from SE.DocumentProcessor import DocumentProcessor
from SE.DocumentStatistic import CorpusStatistics
from SE.EmptyFiles import leerListaVacia
from SE.IdfIndex import IDFIndex
from SE.NormIndex import NormIndex
from SE.QueryInterface import QueryInterface
from SE.QueryProcessingCoordinator import QueryProcessingCoordinator
from SE.QueryProcessor import QueryProcessor
from SE.SearchEngine import SearchEngine
from SE.Steammers import EmptySteamer
from SE.Tokenizer import Tokenizer
from SE.Vocabulary import Vocabulary

palabrasVacias = ["la"]
carpeta = "..collectins/tolosa"
punto = 1

if len(sys.argv) == 2:
    carpeta = sys.argv[1]
elif len(sys.argv) == 3:
    carpeta = sys.argv[1]
    palabrasVacias = leerListaVacia( sys.argv[2], "\n")
else:
    print(
        "Mal paso de parametros! invocalo con: directorioAIndexar pathPalabrasVacias")
    print(
        "ej: python3 mainTP2.py ../collections/tolosa/ ../emptyWords/vacias.txt")
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
print("tardo {0} en armar vocabulario y estadisticas...".format(str(time.time() - inicio)))
print("armando IDFs y normas de doc")
idf_index = IDFIndex()
idf_index.calculate_from_vocabulary(vocabulary, document_index.getSize())
norm_index = NormIndex(idf_index)
norm_index.calculate_norma_for_document(vocabulary)
print("indices listo, levantando UI")
queryProcesor = QueryProcessor(vocabulary, idf_index, norm_index)
queryCoordinator = QueryProcessingCoordinator(tokenizer, EmptySteamer(), queryProcesor, document_index)
interface = QueryInterface(queryCoordinator)
interface.main_menu_loop()
