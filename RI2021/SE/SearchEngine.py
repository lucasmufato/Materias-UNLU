import os

from SE.DocumentProcessor import DocumentProcessor


class SearchEngine:

    def __init__(self, processor: DocumentProcessor) -> None:
        super().__init__()
        self.processor: DocumentProcessor = processor

    def search(self, directory: str, vacias: [str]):
        self.scan_directory(directory, vacias)

    def scan_directory(self, directory: str, lista_vacias: [str]):
        print("scaning directory: " + directory)
        for file in os.listdir(directory):
            if os.path.isdir(file):
                self.scan_directory(file, lista_vacias)
            else:
                self.processor.process_file(directory + file, lista_vacias)
        print("finished directory scan")
