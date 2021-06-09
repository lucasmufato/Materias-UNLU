from collections import Counter

from SE.core.indexs.DocumentIndex import DocumentIndex
from SE.TFxIDF.QueryProcessor import QueryProcessor
from SE.tokenizers.Steammers import DictionaryStemmer
from SE.tokenizers.Tokenizer import Tokenizer
from SE.queries.QueryResult import QueryResult


class QueryProcessingCoordinator:

    def __init__(self, tokenizer: Tokenizer, stemmer: DictionaryStemmer, processor: QueryProcessor, document_index: DocumentIndex) -> None:
        super().__init__()
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.processor = processor
        self.documents = document_index

    def process(self, originalQuery: str) -> [QueryResult]:
        query_vector = self.query_pipeline_converter(originalQuery)
        result = self.processor.process(query_vector)
        self.agregar_nombre_documentos_a_conjunto_resultado(result)
        return result

    def agregar_nombre_documentos_a_conjunto_resultado(self, result):
        for res in result:
            res.doc_name = self.documents.getNameForId(res.doc_id)

    def query_pipeline_converter(self, originalQuery) -> dict:
        query = self.tokenizer.invoke(originalQuery)
        query = self.join_duplicates(query)
        return self.stemmer.stemear_dict(query)

    def join_duplicates(self, query: [str]) -> dict:
        return dict(Counter(query))
