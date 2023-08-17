nombre=input("ingrese su nombre: ")
nota1= float(input("Ingrese Nota 1: "))
nota2=float(input("Ingrese Nota 2: "))
nota3=float(input("Ingrese Nota 3: ")) 
definitiva=(nota1 + nota2 + nota3)/3
print((f"la nota 1 es: {nota1} \nla nota 2 es: {nota2} \nla nota 3 es: {nota3} \nla definitiva es {definitiva} \n"))

if(definitiva  > 0 and definitiva <= 2.0):
     print(f"el estudiante {nombre} tiene una nota definitiva de {definitiva} y tiene problemas de atencion")
elif(definitiva > 2.0  and definitiva <= 3.0):
     print(f"el estudiante{nombre} puede recuperar {definitiva}")
elif(definitiva > 3.0 and definitiva <= 4.0 ):
    print(f"el estudiante{nombre}ha ganado con una definitiva de {definitiva}")
elif(definitiva > 4.0 and definitiva <= 4.6):
    print(f"el estudiante {nombre} ha ganado con una nota de {definitiva}y es genial")
elif(definitiva > 4.6 and definitiva <= 5.0):
    print(f"el estudiante {nombre} ha ganado con una de {definitiva} y es el mejor")
else:
    print("error , su nota no se encuentra en el rango de 0 a 5")
    