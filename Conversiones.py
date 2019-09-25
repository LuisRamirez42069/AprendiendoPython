#Conversiones.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

#Declaramos una variable string con una cadena de dígitos#
numero = "1234"
#Nos muestra el tipo de dato de la variable. La salida de type() no es un str, sino un dato type#
print(type(numero))
#Se convierte la cadena a int#
numero=int(numero)
#Aqui se ve que el tipo ha cambiado, aunque se escribe igual#
print(type(numero))
#Se declara un str con separadores (valores proporcionados usando format)#
salida = "El numero utilizado es: {} "
#Se muestra el resultado y en donde esta {} colocara el valor del numero#
print(salida.format(numero))
