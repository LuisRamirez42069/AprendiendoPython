#Compara.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

numero1 = input()
numero2 = input()
salida = 'Numeros proporcionados: {} y {}. {}.'
if(numero1==numero2):
	#Entra si los números son iguales#
	print(salida.format({}, {}, "Los números son iguales"))
else:
	#if dentro de otro if para ver si los números no son iguales#
	if(numero1>numero2):
		#Imprime si el primer numero es mayor al segundo#
		print(salida.format(numero1, numero2, "El mayor es el segundo"))
	else:
		#De lo contrario, si el primero no es mayor al segundo#
		print(salida.format(numero1, numero2, "El mayor es el segundo"))
