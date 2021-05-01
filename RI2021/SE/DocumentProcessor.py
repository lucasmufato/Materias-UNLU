from collections import Counter

from SE.DocumentIndex import DocumentIndex
from SE.DocumentStatistic import CorpusStatistics
from SE.Steammers import EmptySteamer, DictionaryStemmer
from SE.Vocabulary import Vocabulary


class DocumentProcessor:

    def __init__(self, tokenizer, statistics, vocabulary, documentIndex, steamer=EmptySteamer()) -> None:
        super().__init__()
        self.tokenizer = tokenizer
        self.documentsIndex: DocumentIndex = documentIndex
        self.steamer: DictionaryStemmer = steamer
        self.statistics: CorpusStatistics = statistics
        self.vocabulary: Vocabulary = vocabulary

    def process_file(this, filename, lista_vacias):
        with open(filename, 'r', errors="ignore") as file:
            doc = this.documentsIndex.createAndReturn(file.name)
            for linea in file:
                tokens = this.tokenizer.invoke(linea)
                tokens: [str] = this.tokenizer.sacar_palabras_vacias(tokens, lista_vacias)
                terminos: dict = this.armarTerminos(tokens)
                terminos = this.steamer.stemear_dict(terminos)
                this.vocabulary.agregar(terminos, doc.id)
                this.contarTermsYTokens(doc, terminos, tokens)
            this.statistics.increase_terms(doc.nro_term)

    def armarTerminos(self, tokens):
        return dict(Counter(tokens))

    def contarTermsYTokens(self, doc, terminos:dict, tokens:[str]):
        cant_tokens = len(tokens)
        self.statistics.increase_tokens(cant_tokens)
        doc.increase_tokens(cant_tokens)
        doc.increase_terms(len(terminos))
