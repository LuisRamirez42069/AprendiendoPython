#Entrada.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

entrada = input()
print(type(entrada))
#La variable si es digito y si tiene punto decimal, es (float)
#Si find retorna -1 quiere decir que no tiene punto decimal asi que esEntero sera True#
esEntero = (entrada.isdigit() and entrada.find(".") ==-1)
if (esEntero):
	#Solo se ejecutara si es verdadero#
	print("Dato entero. ¡Muy bien!")
else:
	#Solo se ejecutara si es falso#
	print("Dato no es entero. ¡Sigue intentando!")
