#Nombre.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

nombre = input('Nombre:' )
apellidos = input('Apellidos: ')
#Se concatenan los valores str, junto con la literal ' '
nombreCompleto=nombre+' '+apellidos
#El resultado se reemplazara todo en mayúsculas#
nombreCompleto= nombreCompleto.upper()
print(nombreCompleto)
