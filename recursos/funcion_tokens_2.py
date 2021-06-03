import nltk
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem.snowball import SnowballStemmer

def tokenzito(ruta):

	# Tokenizador TokTok (palabras)
	toktok = ToktokTokenizer()
	# Tokenizador de oracionesa
	es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
	# Obtener oraciones de un parrafo
	with open (ruta, 'r') as file: #ass fp:
	  parrafo=file.read()
	  oraciones = es_tokenizador_oraciones.tokenize(parrafo)
	  
	  # Obtener tokens de cada oración
	  var=[]
	  for s in oraciones:
	    var = var + [t for t in toktok.tokenize(s)]
	file.close()   
	return (var)


def frecuencia(token): #Funcion para la frecuencia
    listaGeneral=[] #Lista inicializada vacía
    listaNumero=[]
    listaPalabra=[]
    longitud=len(token)#Tamaño de la lista de token
    primera=token[0]
    listaPalabra.append(primera)
    listaNumero.append(1) 
    contador = 0

    #Mientras que el contador sea menor al tamaño de la longitud de los tokens
    while(contador < longitud - 1):
    	#Si la primera palabra es igual a la segunda, tercera, cuarta, ...
    	if(primera == token[contador + 1]):
    		#En la posición toma el valor que tiene MAS uno
    		listaNumero[0] = listaNumero[0] + 1
    	#Si la palabra ya se encuentra en la lista?	
    	elif(token[contador + 1] in listaPalabra):
    		#Preguntar en que posición se tiene guardada para aumentarle el contador
    		indice = listaPalabra.index(token[contador + 1])
    		#Agrega el valor en la pcisión que tiene la palabra igual
    		listaNumero[indice] = listaNumero[indice] + 1
    	else:
    		listaPalabra.append(token[contador + 1])
    		listaNumero.append(1)
    	contador = contador + 1
    #Combinar las dos listas en la listaGeneral
    #El "i" va a ir cambiando desde 0 a la longitud de la listaPalabra
    for i in range(len(listaPalabra)):
    	#Se agrega en la listaGeneral la listaNumero en la pocisión "i" y la listaPalabra en la posición "i"
    	listaGeneral.append((listaNumero[i], listaPalabra[i]))
    #Regresa la lista ordenada de menor a mayor	
    listaGeneral.sort(reverse = True)
    print(longitud)
    return listaGeneral


def dimensionalidad(token):
	longitud = len(token)
	palabrasFuncionales = stopwords.words("spanish")
	contador = 0 #Lleva el ciclo
	auxiliar = 0 #Lleva los indices
	#Mientras hay palabras
	while(contador < longitud - 1):
		#Si token en la posición 0 es igual a la palabra que se encuentra en palabras Funcionales
		if(token[auxiliar] in palabrasFuncionales):
			token.remove(token[auxiliar])
			auxiliar = auxiliar - 1
		contador = contador + 1
		auxiliar = auxiliar + 1
	print(longitud)
	return token


def stemming(token):
    listaStemming = []
    # Stemmer en Espanol  ̃
    stemmer = SnowballStemmer("spanish")

    tokens = token # <- aquı va el texto tokenizado  ́
    for t in tokens:
        # Obtener la raiz
        #print(stemmer.stem(t))
        #Guardar los valores en la lista
        listaStemming.append(stemmer.stem(t))
    return listaStemming   


def lematizacion(ruta, token):
    listIzquierda = []
    listDerecha = []
    listResultado = []
    with open (ruta, "r") as file:
        texto = file.read()
        archivo = texto.split()
    for i in range(len(archivo)):
        #Pregunta si el residuo de la división es 0
        if(i % 2 == 0):
            listDerecha.append(archivo[i])
        else:
            listIzquierda.append(archivo[i])
    for i in token:
        if(i in listDerecha):
            indice = listDerecha.index(i)
            listResultado.append(listIzquierda[indice])
        else:
            listResultado.append(i)
    return listResultado





# #Para probar la función Lematización
tokens1 = 'lemmatization-es.txt'
tokens = tokenzito('practica3.txt')
funcionales = dimensionalidad(tokens)
frecuencias = frecuencia(funcionales)
print(lematizacion(tokens1, frecuencias))

# #Para probar la función Stemming
# tokens = tokenzito("practica3.txt")
# reducir = dimensionalidad(tokens)
# cortadas = stemming(reducir)
# print(frecuencia(cortadas))

#Para probar la función dimensionalidad
# tokens = tokenzito("practica3.txt")
# print(dimensionalidad(tokens))
# print(frecuencia(tokens))

#Para probar la función frecuencia
# tokens = tokenzito("practica3.txt")
# print(frecuencia(tokens))

#Para probar la función tokenzito
#token = tokenzito('practica3.txt')
#print(token)
