import readline
nombre = raw_input("dame un nombre\n")
archivo = open(nombre)
lineas = archivo.readlines()
print(str(lineas) + "\n")
matriz = []
for i in range(len(lineas)):
	matriz.append(str(lineas[i]).split())
			
print(matriz)
