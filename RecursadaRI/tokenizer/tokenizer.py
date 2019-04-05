import re

from unidecode import unidecode


def tokenizar(line: str, verbose: bool = False):
    line = line.replace("\r\n", "")
    if verbose: print("tokenizar:: line=" + line)
    mails = get_mail(line)
    for m in mails:
        line = line.replace(m, " ")
    urls = get_url(line)

    quim = get_formulas_quimicas(line)
    for q in quim:
        line = line.replace(q, " ")

    abbrs = get_abbr(line)
    for a in abbrs:
        line = line.replace(a, " ")
    names = get_nombre_propio(line)
    nros = get_numero(line)
    for n in nros:
        line = line.replace(n, " ")

    line = unidecode(line).lower()
    if verbose: print("tokenizar:: after unidecode -> line=" + line)
    linea = re.sub('[^0-9a-zA-Z]+', ' ', line)
    if verbose: print("tokenizar:: after sub -> line=" + line)
    tokens = linea.split()

    for t in tokens:  # si el token no esta entre el tamaño aceptado
        t.strip()
        if not (3 < len(t) < 20):
            # print("sacando token: "+t)
            tokens.remove(t)
    tokens.extend(mails)
    tokens.extend(urls)
    tokens.extend(abbrs)
    tokens.extend(names)
    tokens.extend(nros)
    tokens.extend(quim)

    return tokens


def sacar_palabras_vacias(tokens: list, lista_vacias: list, verbose: bool = False):
    for elem in lista_vacias:
        tokens = list(filter(lambda a: a != elem, tokens))
    return tokens


def get_abbr(line: str, verbose: bool = False):
    """Abreviaturas como NASA E.E.U.U"""
    abbrs = re.findall(r'[A-Z]+(?:\.?[A-Z])+', line)
    """Abreviaturas como Lic. Doc..."""
    abbrs.extend(re.findall(r'(?:([A-Z][a-z]+\.)(?: [A-Z][a-z]+))', line))
    if verbose:
        print("abbrs:")
        print(*abbrs, sep=", ")
    return abbrs


def get_mail(line: str, verbose: bool = False):
    mails = re.findall(r'\w+(?:-|_|\d)*\w@(?:\w+\.)+\w+', line)
    if verbose:
        print("mails:")
        print(*mails, sep=", ")
    return mails


def get_numero(line: str, verbose: bool = False):
    nros = re.findall(r'\d+(?:[.,]+\d+)*', line)
    if verbose:
        print("nros:")
        print(*nros, sep=", ")
    return nros


def get_nombre_propio(line: str, verbose: bool = False):
    names = re.findall(r'[A-Z][a-z]{2,}(?:\s[A-Z][a-z]+)*', line)
    if verbose:
        print("nombres:")
        print(*names, sep=", ")
    return names


def get_url(line: str, verbose: bool = False):
    urls = re.findall(r'(http[s]?:\/\/(?:\w+\.)*\w+(?:\/\w+)*)', line)
    if verbose:
        print("urls:")
        print(*urls, sep=", ")
    return urls


def get_formulas_quimicas(line: str, verbose: bool = False):
    # Componente quimico como: H2o, Na, CO2Fe2LiNa
    cq = r"(?:\d*[A-Z][a-z]?\d?-?)+"
    # Formulas coomo ClO3K => KCl + 3O
    formulas = cq + r"\s*(?:[\+\-]\s*" + cq + r"\s)*[\=\-]\>\s*" + cq + r"\s*(?:[\+\-]\s*" + cq + ")*"
    forms = re.findall(formulas, line)
    # forms.extend( re.findall(cq, line) )
    if verbose:
        print("formulas quimicas:")
        print(*forms, sep=", ")
    return forms
