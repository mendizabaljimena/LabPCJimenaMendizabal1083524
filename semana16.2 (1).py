import random

print("Semana No. 16: Ejercicio 2")

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

matriz = [[random.randint(0, 1000) for _ in range(columnas)] for _ in range(filas)]

numeros_pares = 0
numeros_impares = 0
numero_mayor = matriz[0][0]
numero_menor = matriz[0][0]

for fila in matriz:
    for numero in fila:
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

        if numero > numero_mayor:
            numero_mayor = numero
        
        if numero < numero_menor:
            numero_menor = numero

print(f"\nCantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")
print(f"Número mayor: {numero_mayor}")
print(f"Número menor: {numero_menor}")
