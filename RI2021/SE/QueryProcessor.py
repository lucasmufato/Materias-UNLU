from typing import Dict

from SE.queries.QueryResults import QueryResults


class QueryProcessor:
    pass

    def process(self, queryRepresentation: Dict[str, int]) -> [QueryResults]:
        # por cada documentos presenten en las listas de postings de los terminos de la query
        # juntar tuttis postings en 1 por doc_id y calcular
        # (query pesada * doc pesado) / (norma query * norma doc)
        pass