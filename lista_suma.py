#Fucnión que recibe una lista con enteros y los suma 
def sumatoria(lista):
	resultado = 0
	for i in lista:
		resultado = resultado + i
	return resultado
	
	#Otra forma
	for i in range(len(lista)):
		resultado = resultado + lista[i]
	return resultado

	#Con WHILE
	contador = 0
	while (contador < len(lista)):
		resultado = resultado + lista[contador]
		contador = contador + 1

print(sumatoria([1,2,3,5,8]))
print(sumatoria([1,2]))