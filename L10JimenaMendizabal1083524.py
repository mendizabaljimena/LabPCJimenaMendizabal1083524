print("Semana No. 10: Ejercicio 1")
mesEntrada = int(input("Ingrese un número del 1 al 12: "))
mesSalida = ""
if 1 <= mesEntrada <= 12:
    match mesEntrada:
        case 1:
            mesSalida = "Enero"
        case 2:
            mesSalida = "Febrero"
        case 3:
            mesSalida = "Marzo"
        case 4:
            mesSalida = "Abril"
        case 5:
            mesSalida = "Mayo"
        case 6:
            mesSalida = "Junio"
        case 7:
            mesSalida = "Julio"
        case 8:
            mesSalida = "Agosto"
        case 9:
            mesSalida = "Septiembre"
        case 10:
            mesSalida = "Octubre"
        case 11:
            mesSalida = "Noviembre"
        case 12:
            mesSalida = "Diciembre"
    print("MES: ", mesSalida)
else:
    print("ERROR: El número a ingresar debe estar entre los valores del 1 al 12")



# Ejercicio 2: Determinar el mayor entre tres números
print("\nSemana 10: Ejercicio 2")
A = 0
B = 0
C = 0
# Se solicita el ingreso de los valores
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))

if A > B:
    if A > C:
        print("A es el mayor")
    elif A == C:
        print("A y C son los mayores")
    else:
        print("C es el mayor")
elif A == B:
    if A > C:
        print("A y B son los mayores")
    elif A == C:
        print("A, B y C son iguales")
    else:
        print("C es el mayor")
else:
    if B > C:
        print("B es el mayor")
    elif B == C:
        print("B y C son los mayores")
    else:
        print("C es el mayor")

print("\n" "Semana No. 10: Ejercicio 3 signos zodiacales")
dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento (en número): "))
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
else:
    signo = "Fecha inválida"
print("Tu signo zodiacal es:", signo)
