#Clase calculadora
class Calculadora:
	numero1 = 0
	numero2 = 0

	#Constructor
	def __init__(self, num1, num2):
		self.numero1 = num1
		self.numero2 = num2

	#Función de suma
	def suma(self):
		resultado = self.numero1 + self.numero2
		return resultado

	#fFunción resta	
	def resta(self):
		resultado = self.numero1 - self.numero2
		return resultado 

	#fFunción división	
	def division(self):
		#resultado = self.numero1 / self.numero2
		#return resultado
		if self.numero2 == 0:
			print("No se puede dividir entre 0")
		else:
			resultado = self.numero1 / self.numero2
			return resultado 

	#fFunción multiplicación	
	def multiplicacion(self):
		# resultado = self.numero1 * self.numero2
		# return resultado
		contador = self.numero2
		resultado = 0
		i = 0

		#Multiplicación con "WHILE"
		# while contador > 0: 
		# 	resultado = resultado + self.numero1
		# 	contador = contador - 1
		# return resultado

		#Multiplicación con "WHILE"
		for i in range(contador):
			resultado = resultado + self.numero1
		return resultado

	#Números desde teclado
	def entrada(self):
		#El número que entre desde teclado lo convertirá de cadena a entero
		n1 = int(input("Ingresa el primer número: "))
		n2 = int(input("Ingresa el segundo número: "))
		self.numero1 = n1
		self.numero2 = n2


#Objeto
objCalc = Calculadora(5, 1)
resultadoEntrada = objCalc.entrada() 	
resultadoSuma = objCalc.suma()
resultadoResta = objCalc.resta()
resultadoDivision = objCalc.division()
resultadoMultiplicacion = objCalc.multiplicacion()

print(resultadoSuma)
print(resultadoResta)
print(resultadoDivision)
print(resultadoMultiplicacion)