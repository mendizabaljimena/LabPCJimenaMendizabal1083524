print("Ejercicio 1: Operaciones Matematicas")
a = int(input("Ingerese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = a + b
resta = a - b
multiplicacion = a * b

if b == 0 :
    print ("No se puede dividir en 0")
    division = None 
    divisionEntera = None
    divisionModular = None
else: 
    division = a / b
    divisionEntera = int(a/b)
    divisionModular = a % b
    


print("La suma de ", a, " + ", b, " es: ", suma )
print("La resta de ", a, " - ", b, " es: ", resta)
print("La multiplicacion de ", a, " * ", b, " es: ", multiplicacion)
print("La division de " , a , " / " , b , "es: ", division )
print("La division entera de ", a, " / ", b, " es: ", divisionEntera )
print("La division modular de ", a, " % ", b, " es: ", divisionModular )

print("\n" + "-----------------------------------------------------------" + "\n")
print("Ejercicio 2: Operaciones booleanas")
print("a es mayor que b:", a > b)
print("a es mayor o igual que b: ", a >= b)
print("a es menor que b:", a < b)
print("a es menor o igual que b: ", a <= b)
print("a es igual a b:", a == b)
print("a es diferente de b:", a != b)

print("\n" + "-----------------------------------------------------------" + "\n")
print("Ejercicio 3: Jerarquia de operaciones")
a = float(input ("Ingrese el valor de a: "))
b = float(input ("Ingrese el valor de b: "))
c = float(input ("Ingrese el valor de c: "))

if c == 0:
    print ("El valor de c = 0 causa problemas en la ejecucion")
else:
    operacion1 = a * b + c
    operacion2 = a(b + c)
    operacion3 = a / (b + c)
    operacion4 = (3*a + 2*b) / (c * c)



print("Operacion 1: ", operacion1)
print("Operacion 2: ", operacion2)
print("Operacion 3: ", operacion3)
print("Operacion 4: ", operacion4)



