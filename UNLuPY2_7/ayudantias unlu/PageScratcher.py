#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from Concurso import Concurso
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
#pongo que acepte caracteres en UTF8


"""
instalo librerias para hacer el scratch  de la pagina
 pip install lxml
 pip install requests
"""

from lxml import html
import requests

class PageScratcher:
    'Este objeto se encarga de pedir la pagina de la unlu, parsearla y devuelver las pasantias publicadas que contengan palabras como "sistemas","computacion" u otras'

    def __init__(self):
        self.pagina = "http://www.dga-dpto-concursos.unlu.edu.ar/?q=node/24"
        self.xPathALaTabla = '//*[@id="node-27"]/div[1]/div/table[1]/tbody'
        self.arbolHtml = None
        self.concursos = []

    def parsearPagina(self):

        pagina = requests.get(self.pagina)
        self.arbolHtml = html.fromstring(pagina.content)
        div = self.arbolHtml.xpath( self.xPathALaTabla )
        for tr in div[0]:
            for td in tr:
                if 'Computación' in td.text:
                    concurso = Concurso()
                    concurso.divison = 'Computación'
                    for dato in td:
                        if dato.text != None:
                            concurso.resolucion = dato.text
                        if dato.tail != None:
                            concurso.area += dato.tail
                    concurso.dividirCampos()
                    self.concursos.append(concurso)

    def mostrar(self):
        print "los concursos son: ", self.concursos
        for conc in self.concursos:
            print conc


