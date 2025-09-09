# Programa de juego de adivinanza

import random

# Se genera un número secreto aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Se pide al jugador que ingrese su número
adivinanza = int(input("Adivina el número (entre 1 y 10): "))

# Se muestran las elecciones
print(f"El número secreto es: {numero_secreto}")
print(f"Tu adivinanza es: {adivinanza}")

# Se evalúa la adivinanza
if adivinanza == numero_secreto:
    print("¡FELICIDADES! Adivinaste el número")
elif adivinanza < numero_secreto:
    print("Tu número es menor. Intenta con uno más grande")
else:
    print("Tu número es mayor. Intenta con uno más pequeño")
