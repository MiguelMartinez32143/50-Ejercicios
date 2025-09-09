# Programa que calcula la edad futura de una persona

edad_actual = int(input("¿Cuál es tu edad actual? "))      # Se solicita al usuario su edad actual
anos_futuros = int(input("¿Cuántos años quieres sumar? ")) # Se solicita la cantidad de años a sumar

# Se muestran los resultados usando f-strings
print(f"Tengo {edad_actual} años")
print(f"En {anos_futuros} años tendré {edad_actual + anos_futuros} años")
