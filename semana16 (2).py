import random

print("Semana No. 16, ejercicio 01")

lista = []

for x in range (10):
    lista.append(random.randint(0,10))

opcion = 'a'

while(opcion != 'e'):
    print("Menú")
    print("a. mostrar números, b. promedio,c. Longitud, d. posición, e. Salir")
    opcion = input("Ingrese su opción")
    match opcion:
        case 'a':
            for x in range(len(lista)):
                print(f"No. {x}: {lista[x]}")
        case 'b':
            print("PROMEDIO")
            sumatoria = 0
            for x in range(len(lista)):
                sumatoria += lista[x]
            promedio =sumatoria / len(lista)
            print(f"----Promedio: {promedio}")
        case 'c':
            print("Longitud")
            print(len(lista))
        case 'd':
            print("Elementos pares de la matriz (lista):")
            pares = 0
            impares = 0
            for i in range(len(lista)):  
                if lista[i] % 2 == 0: 
                    print(lista[i])
                    pares += 1
            print("Cantidad de elementos pares:", pares)
            print("Elementos impares de la matriz (lista):")
            for i in range(len(lista)):
                if lista[i] % 2 != 0:
                    print(lista[i])
                    impares += 1
            print("Cantidad de elementos impares:", impares)
        case 'e':
            print("Saliendo del programa...")
        case '':
            print("Esa opción no existe entre las mencionadas")

cantFilas = int(input("Ingrese la cantidad de filas"))
cantCols = int(input("Ingrese la cantidad de columnas"))

matriz = [[0 for x in range(cantCols)] for y in range(cantFilas)]
mayor = matriz[0][0]
menor = 1000
pares2 = 0
impares2 = 0

for xFilas in range (cantFilas):
    for xCols in range(cantCols):
        matriz[xFilas][xCols] = random.randint(0,1001)
        
        if(matriz[xFilas][xCols] > mayor):
            mayor = matriz[xFilas][xCols]

        if(matriz[xFilas][xCols] < menor):
            menor = matriz[xFilas][xCols]

        if(matriz[xFilas][xCols] % 2 == 0):
            pares2 += 1

        if(matriz[xFilas][xCols] % 2 != 0):
            impares2 += 1

print(matriz)
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"El número de números pares es: {pares2}")
print(f"El número de números impares es: {impares2}")