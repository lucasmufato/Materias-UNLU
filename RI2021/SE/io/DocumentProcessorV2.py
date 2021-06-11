from SE.core.indexs.DocumentIndex import DocumentIndex
from SE.core.indexs.Vocabulary import Vocabulary
from SE.io.EmptyWords import EmptyWords


class DocumentProcessorV2:

    def __init__(self, tokenizer, vocabulary, documentIndex, empty_words) -> None:
        super().__init__()
        self.tokenizer = tokenizer
        self.documentsIndex: DocumentIndex = documentIndex
        self.vocabulary: Vocabulary = vocabulary
        self.empty_words: EmptyWords = empty_words

    def process_file(self, filename: str, file_content: str):
        doc = self.documentsIndex.createAndReturn(filename)
        tokens = self.tokenizer.invoke(file_content)
        terminos = self.empty_words.sacar_palabras_vacias(tokens)
        self.vocabulary.agregar(terminos, doc.id)