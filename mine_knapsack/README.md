# Desempeño de la Programación Dinámica

Programa hecho en python3
Archivos:
  - mochila.py
  - mina.py

# Parámetros de entrada de el archivo.txt

  - Mina
  
```sh
$ python3 mina.py mina.txt
```

Ejemplo mina.txt: el contenido del archivo son N líneas y M columnas con números, separados por una cola y un espacio después de cada coma, que representan los valores de cada posición de la mina de oro.

mina.txt
```sh
1, 3, 3, 5, 4, 7, 12
2, 1, 4, 1, 3, 3, 6
11, 6, 4, 2, 1, 4, 0
2, 7, 4, 1, 3, 0, 8
2, 1, 4, 12, 3, 3, 9
2, 9, 4, 9, 3, 4, 6
2, 1, 4, 1, 3, 3, 6
```
Salida: Siendo el la máxima cantidad de oro que se puede recolectar
```sh
50
```

- Mochila

```sh
$ python3 mochila.py archivo.txt
```

Ejemplo archivo.txt: el contenido del archivo la primera línea contiene el largo de la mochila y las demas lineas con n elementos de la siguiente forma:  “peso,beneficio,unidades” , sin ningún enter al final del archivo.

archivo.txt
```sh
50
5,20,4
15,50,3
10,60,3
```
El final del archivo termina en la línea 10,60,3

Salida: Beneficio Máximo con los artículos dentro del contenedor
```sh
260
1,4 #articulo 1 4 unidades
3,3 #articulo 3 3 unidades
```

