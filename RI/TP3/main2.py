"""
overhead = tamaño estructura / tamaño corpus + tamaño estructura

"""

from TP3.BooleanAnaliser import BooleanAnaliser
import time
import os

l = BooleanAnaliser()
l.carpeta= "../archivos/"
l.archivoPalabrasVacias = "../palabras_vacias.txt"
l.nombreArchivo1 = "booleanIndex.bin"

start_time = time.time()
l.leerArchivos()
indexTime= time.time() - start_time
print("El tiempo de lectura de corpus y armado del indice en memoria fue: "+str(indexTime)+ " s")

min, mint, max, maxt, avg = l.minMaxAvgPostingSize()
print("termino con posting mas chica: '{}' tamaño: '{}'. mas grande '{}' con tamaño:'{}'. Avg: {}".format(mint, min, maxt, max, avg))

start_time = time.time()
l.guardarADisco()
writeTime= time.time() - start_time
print("El tiempo de escribir el indice fue: "+str(writeTime)+ " s")

tamanioCorpus = sum(os.path.getsize(l.carpeta+f) for f in os.listdir(l.carpeta) if os.path.isfile(l.carpeta+f))
tamanioIndice = os.path.getsize(l.nombreArchivo1)
overhead = tamanioIndice / (tamanioCorpus +tamanioIndice)
print("el tamaño del corpus es: " + str(tamanioCorpus) + "bytes, el del indice: " + str(tamanioIndice) + "bytes, y el overhead es: " + str(overhead))

while True:
    print()
    print("ingrese la query a buscar - 'end' para salir -")
    print()
    query= input()
    if query=="end":
        break
    start_time = time.time()
    l.procesarQuery(query)
    searchTime = time.time() - start_time
    print("Resultado de la query obtenido en: " + str(searchTime)+ " s")
