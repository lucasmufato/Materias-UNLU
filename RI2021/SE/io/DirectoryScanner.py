import os

from SE.io.DocumentProcessor import DocumentProcessor


class DirectoryScanner:

    def __init__(self, processor: DocumentProcessor) -> None:
        super().__init__()
        self.processor: DocumentProcessor = processor

    def scan_directory(self, directory: str, lista_vacias: [str]):
        print("scaning directory: " + directory)
        for file in os.listdir(directory):
            if os.path.isdir(file):
                self.scan_directory(file, lista_vacias)
            else:
                self.processor.process_file(directory + file, lista_vacias)
        print("finished directory scan")
