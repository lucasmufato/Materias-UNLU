# -*- coding: utf-8 -*-

from LectorCSV import LectorCSV
from KMedias import KMedias

#creo el lector csv
lector = LectorCSV("prueba.csv", "true", ",")
lector.leerArchivo()
datos = lector.get_datos()
#print "los datos son: "
#print datos
headers = lector.get_headers()
#print "los headers son: "
#print headers
algoritmoCluster = KMedias(datos, headers)
"""
for i in range(2, 10):
    algoritmoCluster.armarCluster(i, 5)
    algoritmoCluster.imprimirCluster()
"""
#el primer parametro de armarCluster es la cantidad de clusters
#el segundo es la cantidad de repeticiones del algoritmo
algoritmoCluster.armarCluster(3, 3)
algoritmoCluster.imprimirMejorCluster()