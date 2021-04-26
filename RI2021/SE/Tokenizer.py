import re
import unicodedata


class SimpleTokenizer:
    def invoke(self, line) -> [str]:
        return line.split(" ")

    def sacar_palabras_vacias(self, tokens, palabras_vacias: [str]):
        if palabras_vacias is None:
            return tokens
        else:
            return [x for x in tokens if x not in palabras_vacias]


class Tokenizer:

    def __init__(self, optional_regexs=None) -> None:
        super().__init__()
        if optional_regexs is None:
            optional_regexs = []
        self.optional_regexs = optional_regexs

    def sacar_palabras_vacias(self, tokens: [str], palabras_vacias: [str]) -> [str]:
        if palabras_vacias is None:
            return tokens
        else:
            return [x for x in tokens if x not in palabras_vacias]

    def invoke(self, original_line: str) -> [str]:
        line = original_line.strip()
        line = self.sacar_acentos(line)
        extracts = self.extrar_tokens_importantes(line)
        line = self.sacar_extracts(extracts, line)
        line = self.sacar_caracteres(line)
        unprocesed_tokens = line.split(" ")
        return unprocesed_tokens + extracts

    def sacar_extracts(self, extracts, line):
        for token in extracts:
            line = line.replace(token, "")
        return line

    def extrar_tokens_importantes(self, line):
        extracts = []
        extracts.extend(self.other_regexs(line))
        extracts.extend(self.extraer_urls(line))
        extracts.extend(self.extraer_nros(line))
        extracts.extend(self.extract_mails(line))
        extracts.extend(self.extraer_fechas(line))
        extracts.extend(self.extraer_abreviaturas(line))
        return extracts

    def sacar_acentos(self, line: str) -> str:
        nfkd_form = unicodedata.normalize('NFKD', line)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    def extraer_nros(self, line: str):
        return re.findall("(\d+(?:[,|\.]\d+)+)", line)

    def extraer_fechas(self, line: str):
        return re.findall("\d{1,2}[\/-]\d\d?[\/-]\d{2,4}", line)

    def extraer_abreviaturas(self, line: str):
        return re.findall("([A-Za-z]\.(?:[A-Za-z]\.[A-Za-z])+)", line)

    def extraer_urls(self, line):
        return re.findall("(http[s]?:\/\/(?:\w+\.)*\w+(?:\/\w+)*)", line)

    def extract_mails(self, line):
        return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line)

    def sacar_caracteres(self, line):
        return re.sub('[^0-9a-zA-Z]+', ' ', line).strip().lower()

    def other_regexs(self, line):
        results = []
        for reg in self.optional_regexs:
            results.extend(re.findall(reg, line))
        return results
