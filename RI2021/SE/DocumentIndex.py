from typing import List

from SE.DocumentStatistic import DocumentStatistics


class DocumentIndex:

    def __init__(self) -> None:
        super().__init__()
        self.documents: [] = []

    def createAndReturn(self, filename) -> DocumentStatistics:
        fileId = len(self.documents)
        doc = DocumentStatistics(fileId, filename)
        self.documents.insert(fileId, doc)
        return doc

    def getDocumentAmount(self) -> int:
        return len(self.documents)

    def getDocumentsAsList(self) -> List[DocumentStatistics]:
        return self.documents

    def getNameForId(self, doc_id: int) -> str:
        return self.documents[doc_id]

    def getSize(self) -> int:
        return len(self.documents)
