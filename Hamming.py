#Programa que obtiene el número de carácteres diferentes de dos cadenas: DISTANCIA DE HAMMING

def distancia(cad1, cad2):
	long1 = len(cad1)
	long2 = len(cad2)
	contador = 0

	if long1 != long2:
		print("La longitud es diferente entre las dos cadenas")
	else:
		for i in range(long1):
			a = cad1[i]
			b = cad2[i]
			if a != b:
				contador = contador + 1
		return contador

print(distancia("abc", "bbc"))

