class Vocabulary:

    def __init__(this):
        this.terminos: dict = {}

    def agregar(this, terminos: dict, docId: int, verbose: bool = False):
        for term in terminos:
            nuevo_token = term
            if nuevo_token in this.terminos:
                posting = this.terminos[nuevo_token]
                if docId in posting:
                    posting[docId] += terminos[term]
                    this.terminos[term] = posting
                else:
                    posting[docId] = terminos[term]
                    this.terminos[term] = posting
            else:
                this.terminos[nuevo_token] = {docId: terminos[term]}

    def get_terminos(this):
        return this.terminos


