import os
from collections import Counter

from SE.DocumentStatistic import DocumentStatistics, CorpusStatistics
from SE.Steammers import EmptySteamer
from SE.Vocabulary import Vocabulary


class SearchEngine:

    def __init__(self, tokenizer, statistics, vocabulary, steamer=EmptySteamer()) -> None:
        super().__init__()
        self.tokenizer = tokenizer
        self.statistics: CorpusStatistics = statistics
        self.documents: [] = []
        self.vocabulary: Vocabulary = vocabulary
        self.steamer: EmptySteamer = steamer

    def search(self, directory: str, vacias: [str]):
        self.scan_directory(directory, vacias)
        self.guardar_estadisticas()

    def scan_directory(self, directory: str, lista_vacias: [str]):
        print("scaning directory: " + directory)
        for file in os.listdir(directory):
            if os.path.isdir(file):
                self.scan_directory(file, lista_vacias)
            else:
                self.process_file(directory + file, lista_vacias)
        print("finished directory scan")

    def process_file(this, filename, lista_vacias):
        with open(filename, 'r', errors="ignore") as file:
            this.statistics.increase_docs()
            fileId = len(this.documents)
            doc = DocumentStatistics(fileId, filename)
            this.documents.insert(fileId, doc)
            for linea in file:
                tokens = this.tokenizer.invoke(linea)
                tokens: [str] = this.tokenizer.sacar_palabras_vacias(tokens, lista_vacias)
                terminos: dict = dict(Counter(tokens))
                terminos = this.steamer.stemear_dict(terminos)
                this.vocabulary.agregar(terminos, fileId)
                this.contarTermsYTokens(doc, terminos, tokens)
            # cuando termine de leer el archivo
            this.statistics.increase_terms(doc.nro_term)
            file.close()

    def contarTermsYTokens(self, doc, terminos:dict, tokens:[str]):
        cant_tokens = len(tokens)
        self.statistics.increase_tokens(cant_tokens)
        doc.increase_tokens(cant_tokens)
        doc.increase_terms(len(terminos))

    def guardar_estadisticas(self):
        self.statistics.arma_frecuencias_txt(self.vocabulary)
        self.statistics.armar_terminos_txt(self.vocabulary)
        self.statistics.armar_estadisticas_txt(self.vocabulary, self.documents)
