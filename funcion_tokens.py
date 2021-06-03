import nltk
from nltk.tokenize.toktok import ToktokTokenizer
# Tokenizador TokTok (palabras)
toktok = ToktokTokenizer()
# Tokenizador de oracionesa
es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
# Obtener oraciones de un parrafo
with open ("/Users/davidbellobustamante/Desktop/Curso_Python/recursos/practica3.txt", 'r', encoding="utf8") as file: #ass fp:
  parrafo=file.read()
  oraciones = es_tokenizador_oraciones.tokenize(parrafo)
  # Obtener tokens de cada oraci´on
  var=[]
  for s in oraciones:
    var=var+[t for t in toktok.tokenize(s)]
  print (var)
file.close()
