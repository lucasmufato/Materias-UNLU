from typing import Dict

from SE.TFxIDF import IdfIndex
from SE.TFxIDF.NormIndex import NormIndex
from SE.core.indexs.Vocabulary import Vocabulary
from SE.queries.QueryResult import QueryResult


class QueryProcessor:

    def __init__(self, vocabulary: Vocabulary, idf_index: IdfIndex, norm_index: NormIndex) -> None:
        self.vocabulary: Vocabulary = vocabulary
        self.idf_index: IdfIndex = idf_index
        self.norma_index :NormIndex = norm_index

    def process(self, query_representation: Dict[str, int]) -> [QueryResult]:
        documentos_evaluados = self.calcular_producto_query_por_documentos(query_representation)
        norma_query = self.norma_index.calculate_norma_for_query(query_representation)
        results = self.calcula_resultados_para_cada_documento(documentos_evaluados, norma_query)
        results.sort(key=lambda r: r.weight, reverse=True)
        return results

    def calcula_resultados_para_cada_documento(self, documentos_evaluados: Dict[int, float], norma_query: float) -> [QueryResult]:
        results: [QueryResult] = []
        for doc_id, producto_vectorial in documentos_evaluados.items():
            producto_normas = norma_query * self.norma_index.get_norma_for_doc(doc_id)
            weight = producto_vectorial / producto_normas
            results.append(QueryResult(doc_id, weight))
        return results

    def calcular_producto_query_por_documentos(self, query_representation: Dict[str, int]) -> Dict[int, float]:
        documentos_evaluados: Dict[int, float] = {}
        for termino, freq_in_query in query_representation.items():
            idf = self.idf_index.get_idf_for(termino)
            posting = self.vocabulary.get_posting(termino)
            for doc_id, freq_in_doc in posting.items():
                if doc_id in documentos_evaluados:
                    documentos_evaluados[doc_id] += (freq_in_query * idf) * (freq_in_doc * idf)
                else:
                    documentos_evaluados[doc_id] = (freq_in_query * idf) * (freq_in_doc * idf)
        return documentos_evaluados
