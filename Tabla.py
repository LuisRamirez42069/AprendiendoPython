#Tabla.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

numero = input("Dame un numero del 1 al 9: ")
numero = int(numero)

# for se ejecuta un num, determinado de veces cuando un rango de valores.
# El range, no se incluye en la serie solo es para delimitar el rango ejemplo del 1-10
for i in range(1,11):
	# i va cambiando a cada iteración#
	salida = " {} x {} = {} "
	print(salida.format(numero, i, i*numero))
