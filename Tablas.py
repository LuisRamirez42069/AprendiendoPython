#Tablas.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

for i in range(1,11):
	encabezado = "Tabla de {}"
	print(encabezado.format(i))
	#print sin argumentos es un saldo de linea#
	print()
	# En un for se pone otro for #
	for j in range(1,11):
		#Aqui, i contiene el numero base de la tabla y j el elemento de la misma #
		salida = " {} x {} = {} "
		print(salida.format(i, j, i*j))
		#else:
	#Al concluir se ejecuta este código, que es un salto de línea#
	print()