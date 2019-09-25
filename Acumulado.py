#Acumulado.py:
#Autor: Luis Flores Ramirez
#fechaDeCreacion: 22/09/2019
#---------------------------------------------------------------------------------#

#Se declara las variables#
acumulado = int(0)
numero = str("a")


#El true en un while hace un ciclo infinito, solo se detendra hasta que se utilice la instrucción break#
while True:
	numero = input('Dame un numero entero: ')
	if numero == "":
		#Si el numero es vacio, manda error y se sale#
		print("Vacio. Salida del programa.")
		break
	else:
		#Si da un valor, hara la operacion#
		#Se realiza el calculo usando suma incluyente (+=)
		acumulado += int(numero)
		salida = "Monto acumulado: {}"
		print(salida.format(acumulado))
