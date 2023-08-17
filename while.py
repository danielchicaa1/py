# la condicion se pone antes de iniciar el ciclo y despues
# de finalizar el ciclo 

respuesta =1

while respuesta == 1:
    respuesta= int(input("1.Si\n2.No\nEscriba el numero para continuar:  "))
    
    while respuesta !=  1 and respuesta  != 2:
        print("usted digito mal")
        respuesta=int(input("1.Si\n2.No\nEscriba el numero para continuar:  "))
        