import os

from SE.DocumentProcessor import DocumentProcessor
from SE.DocumentStatistic import CorpusStatistics
from SE.Vocabulary import Vocabulary


class SearchEngine:

    def __init__(self, statistics, vocabulary, processor: DocumentProcessor) -> None:
        super().__init__()
        self.statistics: CorpusStatistics = statistics
        self.vocabulary: Vocabulary = vocabulary
        self.processor: DocumentProcessor = processor

    def search(self, directory: str, vacias: [str]):
        self.scan_directory(directory, vacias)
        # self.guardar_estadisticas()

    def scan_directory(self, directory: str, lista_vacias: [str]):
        print("scaning directory: " + directory)
        for file in os.listdir(directory):
            if os.path.isdir(file):
                self.scan_directory(file, lista_vacias)
            else:
                self.processor.process_file(directory + file, lista_vacias)
        print("finished directory scan")

    # def guardar_estadisticas(self):
    #     self.statistics.arma_frecuencias_txt(self.vocabulary)
    #     self.statistics.armar_terminos_txt(self.vocabulary)
    #     self.statistics.armar_estadisticas_txt(self.vocabulary, self.documents)
