import os
from collections import Counter

from SearchEngine.Configuration import Configuration
from SearchEngine.Vocabulary import Vocabulary
from Utils.Steamer import Steamer
from output.Estadisticas import Estadisticas
from model.MDoc import MDoc
from tokenizer.tokenizer import tokenizar, sacar_palabras_vacias


class SearchEngine:

    def __init__(this, config: Configuration):
        this.verbose = config.verbose_search_engine
        this.vocabulary = Vocabulary()
        this.config = config
        this.lista_documentos = []
        this.estadisticas = Estadisticas()
        this.steamer: Steamer = Steamer()

    def scan_directory(this, directory: str):
        lista_vacias = [""]
        print("scaning directory: " + directory)
        for file in os.listdir(directory):
            if (os.path.isdir(file)):
                # recursive call
                this.scan_directory(file)
            else:
                a = open(directory + file, 'r', errors="ignore")
                if this.verbose: print("reading file: " + file)
                doc = MDoc(len(this.lista_documentos), file)
                this.lista_documentos.insert(len(this.lista_documentos), doc)
                for linea in a:
                    tokens = tokenizar(linea, this.config.verbose_tokenizer)
                    this.estadisticas.cantTokens += len(tokens)
                    doc.nro_tokens += len(tokens)
                    tokens = sacar_palabras_vacias(tokens, lista_vacias, this.config.verbose_tokenizer)
                    terminos = dict( Counter(tokens) )
                    if this.config.steamer != "":
                        terminos = this.steamer.stemear(terminos, this.config.steamer, this.config.verbose_steamer)
                    doc.nro_term += len(terminos)
                    this.vocabulary.agregar(terminos, doc.id, this.verbose)
                # cuando termine de leer el archivo
                this.estadisticas.cantTerminos += doc.nro_term
                a.close()
        print("finished directory scan")

    def armar_archivos_estadisticos(this):
        this.estadisticas.armar_terminos_txt(this.vocabulary)
        this.estadisticas.armar_estadisticas_txt(this.vocabulary, this.lista_documentos)
        this.estadisticas.arma_frecuencias_txt(this.vocabulary)
