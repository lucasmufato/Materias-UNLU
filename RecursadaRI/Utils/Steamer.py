from nltk import LancasterStemmer
from nltk.stem.snowball import SpanishStemmer, PorterStemmer


class Steamer:

    def __init__(self):
        self.stemer = None

    def stemear(this, tokens: dict, steamer_name: str, verbose: bool = False):
        """
        :param verbose: to print things in the console
        :param tokens: dictionary containing token and its repetition
        :param steamer_name: name of the stemer to instanciate
        :return:  dictionary with the same format as input but with it tokens stemed and those whose are equall joined
        """
        if steamer_name == "español":
            this.stemer = SpanishStemmer()
        elif steamer_name == "porter":
            this.stemer = PorterStemmer()
        elif steamer_name == "lancaster":
            this.stemer = LancasterStemmer()
        stemedDic = {}
        for token in tokens.keys():
            stemedToken = this.stemer.stem(token)
            if verbose: print("Stemed from: "+token+" to: "+stemedToken)
            if stemedToken in stemedDic:
                stemedDic[stemedToken] = stemedDic[stemedToken] + tokens[token]
            else:
                stemedDic[stemedToken] = tokens[token]
        return stemedDic




