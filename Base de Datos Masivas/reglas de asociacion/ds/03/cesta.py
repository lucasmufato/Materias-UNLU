# Transformar cesta de compras
archivo = open("groceries_4.csv", "r")

# Inicializamos las estructuras donde guardamos las compras
todos_los_productos=[]
compras={}
i = 0

def actualizar_compras(matriz, factura, producto):
	if matriz.get(factura) == None:
		matriz[factura] = producto + ","
	else:
		matriz[factura] = matriz[factura]+producto+","

for linea in archivo:
	if i<>0: #Para que no le de bola a la linea del encabezado
		factura, producto = linea.split(',')
		producto = producto[0:len(producto)-1]
		actualizar_compras(compras, factura, producto)
		if not(producto in todos_los_productos):
			todos_los_productos.append(producto)
	i = i + 1


# Creamos un archivo y guardamoslos resultados			
print "Termina el procesamiento y comienza el volcado de datos al archivo"
salida = open("cesta_R.csv", "wb")
salida.write("id,")
for prod in todos_los_productos:
	salida.write(prod+",")

salida.write("\n")

for factura in compras:
	productos = compras[factura].split(',')
	salida.write(factura+",")
	for prod in todos_los_productos:
		if prod in productos:
			salida.write("true,")
		else:
			salida.write("false,")
	salida.write('\n')

salida.close()
