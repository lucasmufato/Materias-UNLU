import os


class SearchEngine:


    def __init__(self, tokenizer) -> None:
        super().__init__()
        self.tokenizer = tokenizer

    def scan_directory(self, directory: str):
        lista_vacias = [""]
        print("scaning directory: " + directory)
        for file in os.listdir(directory):
            if os.path.isdir(file):
                self.scan_directory(file)
            else:
                self.process_file(directory + file, lista_vacias)
        print("finished directory scan")

    def process_file(this, filename, lista_vacias):
        with open(filename, 'r', errors="ignore") as file:
            # if this.verbose: print("reading file: " + file)
            # doc = MDoc(len(this.lista_documentos), file)
            # this.lista_documentos.insert(len(this.lista_documentos), doc)
            for linea in file:
                tokens = this.tokenizer.invoke(linea)
                # this.estadisticas.cantTokens += len(tokens)
                # doc.nro_tokens += len(tokens)
                # tokens = sacar_palabras_vacias(tokens, lista_vacias, this.config.verbose_tokenizer)
                # terminos = dict(Counter(tokens))
                # if this.config.steamer != "":
                #     terminos = this.steamer.stemear(terminos, this.config.steamer, this.config.verbose_steamer)
                # doc.nro_term += len(terminos)
                # this.vocabulary.agregar(terminos, doc.id, this.verbose)
            # cuando termine de leer el archivo
            # this.estadisticas.cantTerminos += doc.nro_term
            # a.close()