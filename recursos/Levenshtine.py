import nltk
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.metrics.distance import edit_distance

def corrector(ruta1, ruta2):
	var = 20
	txtBien = []
	#Cargar el archivo que est mal
	with open (ruta1, "r") as file:
		auxMal = file.read()
		txtMal = auxMal.split()
	#Cargar el diccionario de palabras bien	
	with open (ruta2, "r") as file:
		auxDic = file.read()
		diccionario = auxDic.split()
	#Ciclo para recorrer las palabras que están mal	
	for i in range(len(txtMal)):
		#Ciclo para recorrer las palabras del diccionario	
		for j in range(len(diccionario)):
			#Obtener la distancia de Levenshtine
			distancia = edit_distance(txtMal[i], diccionario[j], 1, False)
			#Si la distancia es menor a la variable
			if(distancia < var):
				#Cambiar var sea iguala. distancia
				var = distancia
				palabra = diccionario[j]
		var = 20
		#Guardar en la lista la palabra que se encuentra en la posición j del diccionario en la lista que esta Bien
		txtBien.append(palabra)
		print(i)
	#Guardar la palabra separada por un espacio en un nuevo archivo	
	cadena = " ".join(txtBien)
	with open ("corregido.txt", "w") as file:
		file.write(cadena)


# archivo1 = "corrigeme.txt"
# archivo2 = "listado-general.txt"
# print
corrector("corrigeme.txt","listado-general.txt")

