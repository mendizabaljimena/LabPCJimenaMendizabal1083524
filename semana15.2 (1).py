X = 0
Y = 0

def mover_arriba():
    global Y
    Y += 1

def mover_abajo():
    global Y
    Y -= 1

def mover_derecha():
    global X
    X += 1

def mover_izquierda():
    global X
    X -= 1

def mostrar_coordenadas_finales():
    print(f"Coordenadas finales del personaje: {X},{Y}")

def mostrar_menu():
    print("Seleccione la dirección a la que desea mover el objeto:")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")

def main():
    print("Semana No. 12: Ejercicio 2")
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == 'a':
            mover_arriba()
        elif opcion == 'b':
            mover_abajo()
        elif opcion == 'c':
            mover_izquierda()
        elif opcion == 'd':
            mover_derecha()
        elif opcion == 'e':
            mostrar_coordenadas_finales()
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

