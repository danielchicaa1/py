# Get user input for the password
clave = int(input("Ingrese su clave: "))

# Set the maximum number of attempts
max_attempts = 3
attempts = 1

# Loop for authentication attempts
while clave != 123 and attempts < max_attempts:
    print("Contraseña incorrecta. Intentos restantes:", max_attempts - attempts)
    clave = int(input("Ingrese su clave: "))
    attempts += 1

# Check if the password is correct
if clave == 123:
    print("Bienvenido a su cuenta 😎")
else:
    print("Contraseña incorrecta. Cuenta bloqueada por 24 horas.")

