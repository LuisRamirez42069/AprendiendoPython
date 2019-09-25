#Multiplo.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

numero = int(input('Dame un numero entero: '))
#Se almacenan en valores booleanos, si el residuo es igual a 0#
esMultiplo3 = ((numero % 3)==0)
esMultiplo5 = ((numero % 5)==0)
esMultiplo7 = ((numero % 7)==0)

#Se evalua si son multiplos de lo contrario dara una salida#
if((esMultiplo3 and esMultiplo5) or esMultiplo7):
	print('Correcto.')
else:
	print('Incorrecto.')
