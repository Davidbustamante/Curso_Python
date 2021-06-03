import math
import cmath

def frecuencia(doc, term):
	documento = doc
	termino = term
	contador = 0
	#Cargar el documento
	with open (doc, "r") as file:
		documento = file.read()
		documento = documento.split()
	#"i" contiene cada palabra de un documento
	for i in documento:

		if(i == termino):
			contador = contador + 1
	return contador


def contarTerminos(termino, Documentos):
	contador = 0
	for i in Documentos:
		if(termino in i):
			contador = contador + 1
	return contador


def tfidf(term, doc, Documentos):
	with open (doc, "r") as file:
		documento = file.read()
		documento = documento.split()
	#print(len(doc))
	#print(frecuencia(doc,term))
	longitud = len(documento)
	#longitud = longitud * 1.0
	tf = frecuencia(doc, term) / (longitud*1.0)
	#print(tf)
	idf = math.log(len(Documentos) / contarTerminos(term, Documentos))
	resultado = tf * idf
	return resultado

def td_matrix(terminos, Documentos):
	documentos = []
	fila = []
	columna = []
	for i in Documentos:
		with open(i, "r") as file:
			doc = file.read()
			doc = doc.split()
		documentos.append(doc)
	for i in range(len(Documentos)):
		for j in terminos:
			fila.append(tfidf(j, Documentos[i], documentos))
		columna.append(fila)
		fila = []
	return columna

def coseno(vectorA, vectorB):
	suma = 0
	for i in range(len(vectorA)):
		suma = (vectorA[i] * vectorB[i]) + suma
		sumaA = (vectorA[i] * vectorA[i]) + suma
		sumaB = (vectorB[i] * vectorB[i]) + suma



# resultadoDoc = [["Hola", "como"], ["ola"], ["como"]]
# result = tfidf("Hola", "prueba.txt", resultadoDoc)
# print(result)

terminos = ["Hola", "prueba"]
Documentos = ["prueba.txt", "prueba2.txt"]
matriz = td_matrix(terminos, Documentos)
print(matriz)