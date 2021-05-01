from typing import Dict

from nltk import PorterStemmer, LancasterStemmer
from nltk.stem.snowball import SpanishStemmer


class DictionaryStemmer:

    def stemear_dict(this, terminos: Dict[str, int]) -> Dict[str, int]:
        new_dict: Dict[str, int] = {}
        for token, cant in terminos.items():
            steamed_token = this.stemear_token(token)
            if steamed_token in new_dict:
                new_dict[steamed_token] = new_dict[steamed_token] + terminos[token]
            else:
                new_dict[steamed_token] = terminos[token]
        return new_dict

    def stemear_token(this, token: str) -> str:
        tokenStemeado = this.stemmer.stem(token)
        if tokenStemeado in this.resultStemear:
            this.resultStemear[tokenStemeado].add(token)
        else:
            this.resultStemear[tokenStemeado] = set()
            this.resultStemear[tokenStemeado].add(token)
        return tokenStemeado


class EmptySteamer(DictionaryStemmer):

    def stemear_dict(self, terminos: Dict[str, int]) -> Dict[str, int]:
        return terminos


class SnowBallSpanishStemmer(DictionaryStemmer):

    def __init__(self) -> None:
        super().__init__()
        self.stemmer = SpanishStemmer()
        self.resultStemear = {}


class MyPorterStemmer(DictionaryStemmer):

    def __init__(self) -> None:
        super().__init__()
        self.stemmer = PorterStemmer()
        self.resultStemear = {}


class MyLancasterStemmer(DictionaryStemmer):

    def __init__(self) -> None:
        super().__init__()
        self.stemmer = LancasterStemmer()
        self.resultStemear = {}
