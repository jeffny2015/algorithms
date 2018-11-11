import math
from random import randint
import sys
from timeit import *
 
 #Peso
peso_item = []
peso_item_aux = []
#Beneficio
beneficio_item = []
beneficio_item_aux = []
#Unidades
cantidad_item = []
#tabla para guardar resultados
memo = []
#capacidad mochila
capacidad_mochila = None
#total de items
cantidad_items = None


def mochilaB(i,capacidad):
	#si ya llego al final ya sea del largo o capacidad devuelva 0
	if i == 0 or capacidad == 0:
		return 0
	#si el peso del item es mayor a la capacidad busque otra opcion
	if (peso_item[i-1] > capacidad):
		return mochilaB(capacidad,i-1)
	else:
		#retorne el maximo de los beneficios
		return max(beneficio_item[i-1] + mochilaB(i-1,capacidad - peso_item[i-1]), mochilaB( i-1,capacidad)) 
def mochila(i,capacidad):
  #Si se pasa
  if capacidad < 0:
    return -math.inf
  #Si termina y ya no hay mas 
  if capacidad == 0 or i >= cantidad_items:
    return 0
  #si ya hay un valor entonces usemoslo
  if memo[i][capacidad] != 0:
    return memo[i][capacidad]
  else:
  	#maximo de todas las posible sopciones
    memo[i][capacidad] = max(mochila(i + 1, capacidad - peso_item[i])  + beneficio_item[i], mochila(i + 1,capacidad))
    return memo[i][capacidad]
def  leerArchivo(archivo):
	
	global cantidad_items
	# Recorremos el archivo para coger los valores  capacidad y  peso-i  beneficio-i cantidad-i
	linea = archivo.readline()
	capacidad_mochila = int(linea)
	
	while True:
	    linea = archivo.readline() 
	    x = linea.split(",")
	    if linea != '':
	    	#los vamos metiendo a la lista
	    	peso_item_aux.append(int(x[0]))
	    	beneficio_item_aux.append(int(x[1]))
	    	cantidad_item.append(int(x[2]))

	    	for i in range(int(x[2])):
	    		peso_item.append(int(x[0]))
	    		beneficio_item.append(int(x[1]))
	    #terminamos cuando ya no haya mas que leer
	    if not linea:
	    	break
	#cerramos archivo
	archivo.close()
	#creamos la tabla de  beneficios
	cantidad_items = len(peso_item)
	for i in range(cantidad_items + 1):
		tmp = []
		for i in range(capacidad_mochila + 1):
			tmp.append(0)
		memo.append(tmp)
	#imprimimos el  maximo beneficio segun la capacidad
	#print(mochila(capacidad_mochila))
	res = mochila(0,capacidad_mochila)
	print(res)
	#Aqui recorremos la tabla para sacar los pesos y sus beneficios qpara imprimir los articulos usados en la mochila
	resultado = []
	capacidad_aux = capacidad_mochila
	# recorremos los beneficios al revez  y vamos revizando a ver cuales articulos se metieron en la mochila y vamos restando
	# las diferencia entre cada posicion que se altere la capacidad de manera que termina cuando la capacidad llega a cero
	for i in range(cantidad_items+1):
		if res <= 0:
			break
		if res != memo[i][capacidad_aux]:
			resultado.append((peso_item[i-1], beneficio_item[i-1]))
			res = res - beneficio_item[i-1]
			capacidad_aux = capacidad_aux - peso_item[i-1]
	#ordenamos los resultados que son una lista de tuplas almacenando peso y beneficio
	resultado.sort()

	# Recorremos la lista y vamos contando
	# las veces que se repiten las tuplas 
	#y vamos impirmiendo el i-ndice + 1 y 
	#la cantidad que aparecen
	
	cantidad = 0
	peso_aux = -1
	beneficio_aux = -1
	for peso, beneficio in resultado:
		if peso == peso_aux and beneficio == beneficio_aux:
			cantidad = cantidad + 1
		elif peso_aux == -1:
			cantidad = 1
			peso_aux = peso
			beneficio_aux = beneficio
		else:
			for i in range(len(peso_item_aux)):
				if peso_item_aux[i] == peso_aux and beneficio_item_aux[i] == beneficio_aux:
					print(str(i+1) + ", " + str(cantidad) +"  #articulo "+ str(i+1) + "  " + str(cantidad)+"  unidades")
					break
			peso_aux = peso
			beneficio_aux = beneficio
			cantidad = 1
			
	#Se imprime los ultimos valores segun peso_aux y beneficio_aux 
	for i in range(len(peso_item_aux)):
		if peso_item_aux[i] == peso_aux and beneficio_item_aux[i] == beneficio_aux:
			print(str(i+1) + ", " + str(cantidad) +"  #articulo "+ str(i+1) + "  " + str(cantidad)+"  unidades")
			break

def generarRandom(W, N ,pesoMax, beneficioMax, cantidadMax, iteraciones):
	'''
	W es el tamaño del contenedor
	N la cantidad de elementos
	pesoMax el máximo valor para generar el peso
	beneficioMax el máximo valor para los beneficios
	cantidadMax el máximo valor para las cantidades.
	iteraciones la cantidad de veces que se debe correr el sistema.
	'''
	global capacidad_mochila
	global cantidad_items

	capacidad_mochila = W
	cantidad_items = N
	#agregamos valores random
	for i in range(cantidad_items):
		peso_item.append(randint(1,pesoMax))
		beneficio_item.append(randint(1,beneficioMax))
		cantidad_item.append(randint(1,cantidadMax))
	

	resultado1 = None
	resultado2 = None
	tiempo = 0
	print("[-]Dinamica =>  Tiempo promedio: ",end=" ")
	#Cantidad de veces que se va a ejecutar mochila
	for i in range(iteraciones):
		inicio = default_timer() 
		#creamos la tabla para guardar los valores
		for i in range(cantidad_items + 1):
			tmp = []
			for i in range(capacidad_mochila + 1):
				tmp.append(0)
			memo.append(tmp)
		#Dinamica
		resultado1 = mochila(0,capacidad_mochila)
		tiempo += default_timer() - inicio

	print(str(tiempo) + " / " + str(iteraciones) + " = " + str(tiempo/iteraciones))
	tiempo = 0
	print("[-]Backtracking =>  Tiempo promedio: ",end=" ")
	#Cantidad de veces que se va a ejecutar mochila
	for i in range(iteraciones):
		inicio = default_timer() 
		#Backtracking
		resultado2 = mochilaB(cantidad_items,capacidad_mochila)
		tiempo += default_timer() - inicio
	print(str(tiempo) + " / " + str(iteraciones) + " = " + str(tiempo/iteraciones))
	if resultado1 == resultado2 and resultado1 != None:
		print("[-]Beneficio Max: " + str(resultado1))
def main():
	'''
	No se validad mucho, se espera que el usuario ingrese correctamente los datos
	si el segundo argumento es una g/-g/generar  mas los demas argumentos se evaluan los
	experimentos

	Sino supone que el segundo argumento es un archivo con la capacidad y sus pesos beneficios y unidades respectivas separadas por "," y sin espacios
	y sin salto final al final del archivo
	'''
	if len(sys.argv) < 2:
		print("[-]No ingreso bien todos los datos")
	elif sys.argv[1] == "g" or sys.argv[1] == "-g" or sys.argv[1] == "generar":
		try:
			generarRandom(int(sys.argv[2]), int(sys.argv[3]) ,int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
		except Exception as e:
			print("[-] %s" %e)
			sys.exit(2)	
	else:
		inputFile = None
		try:
			inputFile = open(sys.argv[1], 'r+')
		except Exception as e:
			print("[-] %s" %e)
			sys.exit(2)
		leerArchivo(inputFile)

if __name__ == '__main__':
	main()
