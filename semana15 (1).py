import math

def obtener_area_triangulo(base, altura):
    area = base * altura / 2
    return area

def obtener_area_cuadrado(lado):
    area = lado ** 2
    return area

def obtener_area_rectangulo(base, altura):
    area = base * altura
    return area

def obtener_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def mostrar_menu():
    print("Semana No. 12: Ejercicio 1")
    print("Seleccione la opción que desea calcular:")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    print("e. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == 'a':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = obtener_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area}")
        elif opcion == 'b':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = obtener_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area}")
        elif opcion == 'c':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = obtener_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area}")
        elif opcion == 'd':
            radio = float(input("Ingrese el radio del círculo: "))
            area = obtener_area_circulo(radio)
            print(f"El área del círculo es: {area}")
        elif opcion == 'e':
            print("Adiós...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
