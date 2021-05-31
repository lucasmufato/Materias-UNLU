from collections import Counter

from SE.QueryProcessor import QueryProcessor
from SE.Steammers import DictionaryStemmer
from SE.Tokenizer import Tokenizer
from SE.queries.QueryResults import QueryResults


class QueryProcessingCoordinator:

    def __init__(self, tokenizer: Tokenizer, stemmer: DictionaryStemmer, processor: QueryProcessor) -> None:
        super().__init__()
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.processor = processor

    def process(self, originalQuery: str) -> [QueryResults]:
        query_vector = self.query_pipeline_converter(originalQuery)
        return self.processor.process(query_vector)

    def query_pipeline_converter(self, originalQuery) -> dict:
        query = self.tokenizer.invoke(originalQuery)
        query = self.join_duplicates(query)
        return self.stemmer.stemear_dict(query)

    def join_duplicates(self, query: [str]) -> dict:
        return dict(Counter(query))
