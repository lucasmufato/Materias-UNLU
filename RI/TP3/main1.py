from TP3.BooleanAnaliser import BooleanAnaliser


l = BooleanAnaliser()
l.carpeta= "../archivos/"
l.archivoPalabrasVacias = "../palabras_vacias.txt"
l.nombreArchivo1 = "booleanIndex.bin"
l.construirIndice()
while True:
    print()
    print("ingrese la query a buscar - 'end' para salir -")
    print()
    query= input()
    if query=="end":
        break
    l.procesarQuery(query)
