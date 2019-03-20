from .LexicAnaliser import LexicAnaliser
import re
import sys
class LexicAnaliser2(LexicAnaliser):
    """clase para el punto 2 - Extraigo tokens especiales"""

    def __init__(this):
        """agrego variables especificas para el punto"""
        super().__init__()
        this.REurl = "(http[s]?:\/\/(?:\w+\.)*\w+(?:\/\w+)*)"
        this.REfecha = "\d{1,2}[\/-]\d\d?[\/-]\d{2,4}"
        this.REmail = "[a-z](a-z|0-9|_|-)+@(a-z+\.)*\.a-z+"
        # this.REnro = "\d+[\.?\d+]*[\,?\d+]?";
        this.REnro = "\d+"
        this.REnombres = "[A-Z][a-z]{2,}(?:\s[A-Z][a-z]+)*"
        this.REabreviatura = "([A-Z][a-z]+\.(?: [A-Z][a-z]+))"
        this.nombres = []
        this.urlsYmails = []
        this.nros = []
        this.abreviaturas = []

    def extraer(this, linea, fileId):
        """busco patrones en las lineas, si encuentro las saco de la linea y envio a agregar a la lista de terminos"""
        # obtengo de la linea y luego saco lo encontrado
        fechas = re.findall(this.REfecha, linea)
        linea = this.sacar(fechas, linea)
        mail = re.findall(this.REmail, linea)
        linea = this.sacar(mail, linea)
        urls = re.findall(this.REurl, linea)
        linea = this.sacar(urls, linea)
        nros = re.findall(this.REnro, linea)
        linea = this.sacar(nros, linea)
        abrev = re.findall(this.REabreviatura, linea)
        linea = this.sacar(abrev, linea)
        nombres = re.findall(this.REnombres, linea)
        linea = this.sacar(nombres, linea)
        # guardo lo encontrado como tokens
        this.analizarToken(abrev, fileId)
        this.analizarToken(fechas, fileId)
        this.analizarToken(mail, fileId)
        this.analizarToken(urls, fileId)
        this.analizarToken(nombres, fileId)
        # agrego a las listas
        this.nombres.extend(nombres)
        this.urlsYmails.extend(mail)
        this.urlsYmails.extend(urls)
        this.nros.extend(nros)
        """
        print(linea)
        print("prueba: "+ str( re.findall("([A-Z]\.)+",linea)))
        print("prueba: "+ str( re.findall("[A-Z]\w+(?:\s[A-Z]\w+?)?\s(?:[A-Z]\w+?)?[\.\,\;\:]?",linea)))
        print("fechas: "+str( fechas))
        print("mails: "+str( mail))
        print("nros: "+str( nros))
        print("urls: "+str( urls))
        print("nombres: "+str( nombres))
        """
        return linea

    def sacar(this, lista, linea):
        """reemplazo en la linea los tokens que devolvio la expresion regular"""
        for elemento in lista:
            # print("borrando '"+ elemento + "' de: "+ str(linea))
            linea = linea.replace(elemento, "")
        return linea


l = LexicAnaliser2()
pre = "2_"
if len(sys.argv) == 2:
    l.carpeta = sys.argv[1]
    l.archivoPalabrasVacias = ""
elif len(sys.argv) == 3:
    l.carpeta = sys.argv[1]
    l.archivoPalabrasVacias = sys.argv[2]
else:
    print(
        "Mal paso de parametros! pasale directorio de archivo(aunque tenga uno solo) y/o path de archivo con palabras vacias")
    sys.exit(-1)

l.leerArchivos()
l.armarEstadisticas1()
l.armarEstadisticas2()
l.armarEstadisticas3()
# opcionales para este punto
l.mostrarListaArchivos()
l.mostrarIndice()