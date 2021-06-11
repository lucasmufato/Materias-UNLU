import os

from SE.io.DocumentProcessor import DocumentProcessor


class DirectoryScannerV2:

    def __init__(self, processor: DocumentProcessor) -> None:
        super().__init__()
        self.processor: DocumentProcessor = processor

    def scan_directory(self, directory: str):
        print("scaning directory: " + directory)
        for filename in os.listdir(directory):
            if os.path.isdir(filename):
                self.scan_directory(filename)
            else:
                with open(directory + filename, 'r', errors="ignore") as file:
                    file_content = file.read()
                    self.processor.process_file(directory + filename, file_content)
        print("finished directory scan")
