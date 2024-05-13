#Menú de opciones

def case1():
    return 6 + 10

def case2():
    return 7 * 7

def case3():
    return 100 - 56

def case4 ():
    return "Salir"

def default_case():
    return "Ingrese opción correcta"

def switch_case(argument):
    switcher = {
        1: case1, 
        2: case2, 
        3: case3, 
        4: case4,
    }

    func = switcher.get(argument, default_case)

    return func()

opcion = int(input("Ingrese opción: "))
print(switch_case(opcion))