import struct
import subprocess

import resource

from TP3.booleanToDisc import BooleanToDisc

#poner limite en KB
maxKB = 3000
maxKB *= 1024


soft, hard = resource.getrlimit(resource.RLIMIT_AS)
resource.setrlimit(resource.RLIMIT_AS, (maxKB, hard))

soft, hard = resource.getrlimit(resource.RLIMIT_AS)
print('Memoria  Maxima Asignada  :'+ str(soft))

l = BooleanToDisc()
l.carpeta= "../archivos/"
l.archivoPalabrasVacias = "../palabras_vacias.txt"
l.nombreArchivo1 = "chunkA.bin"
l.nombreArchivo2 = "chunkB.dat"
l.construirIndice()

"""
s = struct.Struct("III")
terminos = [(10,2,4),(3,1,5),(2,1,4),(3,2,4),(2,2,4),(10,1,4),(5,2,4),(6,2,4),(33,2,4),(1,1,4)]


def pasarAArchivos():
    file = open("archivo.dat","wb")
    for tripla in terminos:
        packed = s.pack(*tripla)
        file.write(packed)
    file.close()


def leerArchivo():
    file = open("archivo.dat", "rb")
    for i in range(0, 10):
        content = file.read(3 * 4)
        data = s.unpack(content)
        print("lei: "+str(data))
    file.close()

def ordenar():
    subprocess.run()


pasarAArchivos()
ordenar()
leerArchivo()
"""