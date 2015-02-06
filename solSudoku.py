import readline
nombre = raw_input("dame un nombre del archivo\n")
archivo = open(nombre)
lineas = archivo.readlines()
print(str(lineas) + "\n")
matriz = []
for i in range(len(lineas)):
	matriz.append(str(lineas[i]).split())
			
print(matriz)
