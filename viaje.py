while True:
    opcion = int(input("Las opciones son: \n\n1. Ingresar datos para cotización\n2. Cancelar planes\n \nIngrese un numero: "))

    if opcion == 1 or opcion == 2:
        break
    else:
        print("Opción incorrecta. Por favor, seleccione 1 o 2.")

# Handle the selected option
if opcion == 2:
    print("Has decidido cancelar tus planes.")
elif opcion == 1:
    print("********** INGRESANDO DATOS PARA COTIZACIÓN DE VIAJE **********\n")
  
    # Get user input for destination and customer name
    Destino = input("Ingrese el destino que desea: ")
    nombreCliente = input("Ingrese el nombre del cliente: ")
    
    # Get user input for the number of adults and children
    cantidadAdultos = int(input("Ingrese el número de personas adultas que viajan: "))
    cantidadNiños = int(input("Ingrese el número de niños que viajan: "))
    
    # Define constants for travel costs
    valorAdultoGuajira = 1450000
    valorAdultoCañon = 1450000
    valorAdultoLlanos = 1450000
    valorNiñosGuajira = 870000
    valorNiñosCañon = 960000
    valorNiñosLlanos = 720000

    if Destino.lower() == 'guajira':
        granTotal = (cantidadAdultos * valorAdultoGuajira) + (cantidadNiños * valorNiñosGuajira)
        print(f"El usuario{nombreCliente} viaja con una cantidad de{cantidadAdultos} adultos, y {cantidadNiños} niños, y el total es {granTotal}")
    
    elif Destino.lower() == 'cañon del chicamocha':
        granTotal = (cantidadAdultos * valorAdultoCañon) + (cantidadNiños * valorNiñosCañon)
        print(f"El usuario{nombreCliente} viaja con una cantidad de{cantidadAdultos} adultos, y {cantidadNiños} niños, y el total es {granTotal}")
    
    elif Destino.lower() == 'llanos':
        granTotal = (cantidadAdultos * valorAdultoLlanos) + (cantidadNiños * valorNiñosLlanos)
        print(f"El usuario{nombreCliente} viaja con una cantidad de{cantidadAdultos} adultos, y {cantidadNiños} niños, y el total es {granTotal}")    
    else:
        print("La opcion ingresada es incorrecta")

