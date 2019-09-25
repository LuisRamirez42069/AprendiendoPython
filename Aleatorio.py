#Aleatorio.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

#Para utilizar un modulo, se ocupa para la librera import#
import random

#Declaramos una variable tipo float#
numero1 = float(10.5)
#Se declara una función y el código tiene que estar a la derecha para que forme parte de ella#
def miFuncion():
	#Se convierte el numero aleatorio#
	#random.randrange(), se ejecutara solo si ponemos la librera import#
	numero2=float(random.randrange(1,5))
	#Se utilizan llaves {} para mostrar los resultados#
	mensaje = "La suma de {} y {} es {} "
	print(mensaje.format(numero1, numero2, numero1+numero2))
#Se ejecuta la función invocandola#
miFuncion()
