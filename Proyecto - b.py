#INTENGRANDES: Rodrigo Beltran y Jimena Mendizabal
#IMPORTAR LIBRERIA "REGEX"
import re

#INICIANLIZANDO VARIABLES
leche = "con Leche Deslactosada"
azucar = "Sin azúcar"
tamano = "de Tamaño Normal"
respuesta_nit = ""
respuesta_menu = 0
precio = 20.00
agrandar = False
opcion = 0
nit = ""
nombre_cliente = ""
opcion_leche = 0

#INICIALIZANDO CONTADORES
cucharadas_azucar = 0

#PEDIR NOMBRE
while True:   
    nombre_cliente = input("Ingrese su Nombre -> ")

    if not nombre_cliente.strip(): #Validar que la variable "nombre_clienteW no este vacía
            print("Por favor, ingrese un nombre válido.")
    elif not re.fullmatch(r"[A-Za-zñÑáéíóúÁÉÍÓÚ ]{1,50}", nombre_cliente): #Validar que el nombre solo contenga letras
            print("El nombre debe contener únicamente letras. Por favor, inténtelo de nuevo.")
    else: 
        break

#PEDIR NIT
respuesta_nit = input("\n¿Desea ingresar NIT? S/N -> ")
respuesta_nit_mayuscula = respuesta_nit.upper()

while True: 

    if(respuesta_nit_mayuscula == "S"): 
        nit = input("\nIngrese su número de NIT -> ")    

        if not nit.strip(): 
                print("Por favor, ingrese un NIT válido.")
        elif not nit.isdigit(): 
                print("El NIT debe contener únicamente dígitos. Por favor, inténtelo de nuevo.")
        elif not len(nit) <= 10: 
                print("La longitud del NIT debe ser de 9 dígitos. Por favor, inténtelo de nuevo.")   
        else: 
            print(f"\n¡BIENVENIDO {nombre_cliente}!")
            break

    elif(respuesta_nit_mayuscula == "N"): 
        print("¡No hay problema!")
        print(f"\n¡BIENVENIDO {nombre_cliente}!")
        nit = "c/f"
        break

    else: 
        print("Ingrese una respuesta válida")

#IMPRIMIR MENÚ DE OPCIONES
print(f"""\
    \nMENÚ DE OPCIONES 
      
      1. Ver Información del Pedido
      2. Agregar Azúcar
      3. Modificar Leche
      4. Agrandar
      5. Confirmar

      Tu producto actual es: Licuado de Fresa {leche} {azucar} {tamano} -> Precio: Q. {precio}
      """)

#CICLO DE SOLICITUD DE OPCIONES - SE DETIENE AL ESCOGER "CONFIRMAR"
while True: 

    #PEDIR OPCIÓN
    opcion = int(input("¿Qué deseas cambiar de tu licuado? -> "))

    #ACCIONES A REALIZAR SEGÚN LA OPCIÓN ESCOGIDA
    match (opcion): 

        #VER INFORMACIÓN DEL PEDIDO - OPCIÓN 1
        case 1: 
            print(f"""\
                  INFORMACIÓN DEL PEDIDO
                  
                    Nombre del Cliente: {nombre_cliente}
                    NIT: {nit}
                    Producto: Licuado de Fresa {leche} {azucar} {tamano}
                    Precio Actual: Q.{round(precio, 2)}
                  """)
            
            #Mostrar el menú nuevamente  
            print(f"""\
                        \nMENÚ DE OPCIONES 
      
                            1. Ver Información del Pedido
                            2. Agregar Azúcar
                            3. Modificar Leche
                            4. Agrandar
                            5. Confirmar
                            """)
            
        #AGREGAR AZÚCAR - OPCIÓN 2
        case 2: 
            cucharadas_azucar = cucharadas_azucar + 1

            if(cucharadas_azucar <= 2): 
                azucar = "con " + str(cucharadas_azucar) + " Cucharadas de Azúcar"
                precio = precio + 0.50
                print("¡Hemos agregado una cucharada más de azúcar! :D")
            else: 
                print("Has alcanzado el máximo de cucharadas de azúcar permitidas. ¡CUIDAMOS TU SALUD! :D")

            #Mostrar el menú nuevamente
            print(f"""\
                        \nMENÚ DE OPCIONES 
      
                            1. Ver Información del Pedido
                            2. Agregar Azúcar
                            3. Modificar Leche
                            4. Agrandar
                            5. Confirmar
                            """)

        #CAMBIAR LECHE - OPCIÓN 3
        case 3: 
            print("""\
                    \nOPCIONES DE LECHE: 
                        1. Sin Leche (únicamente con agua)
                        2. Leche Deslactosada
                        3. Leche Entera
                        4. Leche de Soya
                  """)
            
            opcion_leche = input("\n¿Qué tipo de Leche Deseas? Ingrese el número -> ")

            match(opcion_leche): 

                #SIN LECHE
                case "1": 
                    if (leche == "con Leche de Soya"): 
                        precio = precio - 3.00

                    precio = precio - 2.00
                    leche = "Sin Leche"
                
                #LECHE DESLACTOSADA
                case "2": 
                    if (leche == "Sin Leche"):
                        precio = precio + 2.00
                    elif (leche == "con Leche de Soya"): 
                        precio = precio - 3.00

                    leche = "con Leche Deslactosada"
                
                #LECHE ENTERA
                case "3": 
                    if (leche == "Sin Leche"):
                        precio = precio + 2.00
                    elif (leche == "con Leche de Soya"): 
                        precio = precio - 3.00
                        
                    leche = "con Leche Entera"
                
                #LECHE DE SOYA
                case "4": 

                    if (leche == "Sin Leche"):
                        precio = precio + 2.00
                        
                    precio = precio + 3.00
                    leche = "con Leche de Soya"
                
                #OPCIÓN INVÁLIDA (FUERA DEL RANGO PERMITDO)
                case _:
                    print("Ingrese una opción válida: ")
                    opcion_leche = int(input("\n¿Qué tipo de Leche Deseas? Ingrese el número -> "))
            
            print("¡Hemos cambiado la leche! :D")

            #Mostrar el menú nuevamente  
            print(f"""\
                        \nMENÚ DE OPCIONES 
      
                            1. Ver Información del Pedido
                            2. Agregar Azúcar
                            3. Modificar Leche
                            4. Agrandar
                            5. Confirmar
                            """)

        #AGRANDAR - OPCIÓN 4
        case 4: 
            if (agrandar == False): 
                agrandar = True
                precio = precio + (precio * 0.05)
                tamano = "de Tamaño Grande"
                print("¡Hemos hecho de tamaño GRANDE tu licuado! :D")
            else: 
                print("Tu licuado ya es de tamaño grande, no lo puesdes agrandar más!!")
            
            #Mostrar el menú nuevamente  
            print(f"""\
                        \nMENÚ DE OPCIONES 
      
                            1. Ver Información del Pedido
                            2. Agregar Azúcar
                            3. Modificar Leche
                            4. Agrandar
                            5. Confirmar
                            """)

        #CONFIRMAR - OPCIÓN 5
        case 5: 
            break

        #ERROR - OPCIÓN FUERA DEL RANGO PERMITIDO
        case _:
            print("Opción Inválida. Ingrese una opción correcta.")

#SALIDA
print(f"""\
      \nPEDIDO CONFIRMADO
      
                    Nombre del Cliente: {nombre_cliente}
                    NIT: {nit}
                    Producto Adquirido: Licuado de Fresa {leche} {azucar} {tamano}
                    Precio: Q.{round(precio, 2)}

                    Disfruta tu licuado. ¡Ten un Hermoso Día! :b
      """)