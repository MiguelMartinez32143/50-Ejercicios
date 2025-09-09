# Programa que valida una contraseña según reglas básicas

# Se pide al usuario que ingrese la contraseña
contraseña = input("Ingresa tu contraseña: ")

longitud_minima = 8  # Mínimo de caracteres requeridos

# Verificar longitud
if len(contraseña) >= longitud_minima:
    print("✔ La contraseña tiene la longitud correcta")
else:
    print("✘ La contraseña es demasiado corta")

# Verificar si está en minúsculas únicamente
if contraseña.islower():
    print("✘ La contraseña no debe estar solo en minúsculas")

# Verificar si está en mayúsculas únicamente
if contraseña.isupper():
    print("✘ La contraseña no debe estar solo en mayúsculas")

# Verificar si contiene solo números
if contraseña.isdigit():
    print("✘ La contraseña no puede ser solo números")

# Validación general
if (
    len(contraseña) >= longitud_minima
    and not contraseña.islower()
    and not contraseña.isupper()
    and not contraseña.isdigit()
):
    print("✔ La contraseña cumple con los requisitos")
