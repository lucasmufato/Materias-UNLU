import re


class SimpleTokenizer:
    def invoke(self, line) -> [str]:
        return line.split(" ")

    def sacar_palabras_vacias(self, tokens, lista_vacias):
        return tokens

class Tokenizer:
    pass

    def sacar_palabras_vacias(self, tokens: [str], palabras_vacias: [str]) -> [str]:
        if palabras_vacias is None:
            return tokens
        else:
            return [x for x in tokens if x not in palabras_vacias]

    def invoke(self, line) -> [str]:
        return line.split(" ")

    def extract_mails(self, line) -> [str]:
        return re.findall(r'[a-zA-Z0-9_.+-]+@(?:\w+\.)+\w+', line)
