import sys
import math
import timeit
import random

# global para programacion dinamica
memoize = None

# crea una matriz de i * j y la llena con valores aleatorios entre 1 y oro_maximo
def generarRandom(i, j, oro_maximo):
    matriz = []
    for x in range(i):
        matriz += [[]]
    for x in range(i):
        matriz[x] += [random.randint(1, oro_maximo) for y in range (j)]
    return matriz

# Backtracking del problema de la mina de oro
def mineria_backtracking(i, j, matriz):
    if(i < 0 or i >= len(matriz)):
        return -math.inf
        
    elif (j >= len(matriz[0])):
        return 0
        
    else:
        return matriz[i][j] + max(mineria_backtracking(i - 1, j + 1, matriz), mineria_backtracking(i + 1, j + 1,matriz), 
            mineria_backtracking(i, j + 1, matriz))

    
# Programacion dinamica del problema de la mina de oro
def mineria_dinamica(i, j, matriz):
    global memoize
    if(i < 0 or i >= len(matriz)):
        return -math.inf
    
    elif(j == len(matriz[0]) - 1):
        return matriz[i][j]
    
    elif (memoize[i][j] != -1):
        return memoize[i][j]
        
    else:
        memoize[i][j] = matriz[i][j] + max(mineria_dinamica(i - 1, j + 1, matriz), mineria_dinamica(i, j + 1, matriz),
            mineria_dinamica(i + 1, j + 1, matriz))
        return memoize[i][j]

# recibe una matriz que representa la mina de oro y la cantidad de iteraciones que se quiere realizar
def mineria(matriz, iteraciones):
    global memoize
    memoize = [[-1 for j in range(len(matriz[0]))] for i in range(len(matriz))]
    # ejecución del problema de las minas de oro en programacion dinamica
    tiempo = 0
    for iteracion in range(iteraciones):
        maximo = -math.inf
        tiempo_inicio = timeit.default_timer()
        for x in range(len(matriz)):
            maximo = max(maximo, mineria_dinamica(x, 0, matriz))
        print(maximo)
        tiempo += timeit.default_timer() - tiempo_inicio
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                memoize[i][j] = -1
        
    print("Tiempo promedio de ejecución de programacion dinamica con " + str(iteraciones) + " iteraciones: ")
    print("\t" + str(tiempo/iteraciones))
        
    # ejecución del problema de las minas de oro en backtracking
    tiempo = 0
    for iteracion in range(iteraciones):
        maximo = -math.inf
        tiempo_inicio = timeit.default_timer()
        for x in range(len(matriz)):
            maximo = max(maximo, mineria_backtracking(x, 0, matriz))
        print(maximo)
        tiempo += timeit.default_timer() - tiempo_inicio
        
    print("Tiempo promedio de ejecución de backtracking con " + str(iteraciones) + " iteraciones: ")
    print("\t" + str(tiempo/iteraciones))

def main():
    matriz = []
    # cuando pasa un archivo como argumento
    if(len(sys.argv) == 2):
        # lee el archivo
        try:
            archivo = open(sys.argv[1], 'r')
        except Exception as e:
            print("[-] %s" %e)
            sys.exit(2)
        archivo = open(sys.argv[1], 'r')
        lineas = archivo.readlines()
        archivo.close()
        
        matriz = []
        
        for l in lineas:
            matriz += [l.split(", ")]
        
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] = int(matriz[i][j])
        mineria(matriz, 10)
        
    # cuando no pasa un archivo como argumento
    elif sys.argv[1] == "g" or sys.argv[1] == "-g" or sys.argv[1] == "generar":
        try:
            matriz = generarRandom(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
            mineria(matriz, int(sys.argv[5]))
        except Exception as e:
            print("[-] %s" %e)
            sys.exit(2)
    
    else:
        print("[-]No ingreso bien todos los datos")
    
main()
