#!/usr/bin/python
# -*- coding: latin-1 -*-
# number of elements
n = int(input("Hola por favor ingresa la cantidad de numeros a consultar : ")) 
listado = list(map(int,input("\nAhora Ingresa los numeros separados por espacio y ordenados ascendentemente : ").strip().split()))[:n]
buscar = listado
for i in buscar:
        if i in listado:
            if i <= min(listado):
                resultado = "X"
            else:
                result = listado.index(i)
                resultado = listado[result-1]            
            if i == max(listado):
                resdos = "X"
            else:
                resultd = listado.index(i)
                resdos = listado[resultd+1]
            print(resultado,resdos)
        else:
            print("los valores de la lista 'buscar' no se encuentra dentro de la lista 'listado'")