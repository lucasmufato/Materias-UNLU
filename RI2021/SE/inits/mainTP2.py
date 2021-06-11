import sys
import time

from SE.core.indexs.DocumentIndex import DocumentIndex
from SE.io.DocumentProcessor import DocumentProcessor
from SE.statistics.DocumentStatistic import CorpusStatistics
from SE.io.EmptyWords import leerListaVacia
from SE.TFxIDF.IdfIndex import IDFIndex
from SE.TFxIDF.NormIndex import NormIndex
from SE.io.QueryInterface import QueryInterface
from SE.TFxIDF.QueryProcessingCoordinator import QueryProcessingCoordinator
from SE.TFxIDF.QueryProcessor import QueryProcessor
from SE.io.DirectoryScanner import DirectoryScanner
from SE.tokenizers.Steammers import EmptySteamer
from SE.tokenizers.Tokenizer import Tokenizer
from SE.core.indexs.Vocabulary import Vocabulary

palabrasVacias = ["la"]
carpeta = "..collections/tolosa"
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
se = DirectoryScanner(processor)
se.scan_directory(carpeta, palabrasVacias)
print("tardo {0} en armar vocabulario...".format(str(time.time() - inicio)))
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
