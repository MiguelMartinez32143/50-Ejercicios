# Programa que determina si una persona es mayor de edad

# Se solicita la edad de la persona
edad = int(input("Ingresa tu edad: "))

# Se usa un operador ternario para mostrar el resultado en una sola línea
mensaje = "Eres mayor de edad, puedes votar" if edad >= 18 else "Eres menor de edad, aún no puedes votar"

# Se imprime el mensaje y la edad ingresada
print(mensaje)
print(f"Tu edad es: {edad} años")
