# =================================================
# JUEGO: ADIVINA EL NÚMERO (SIN LIBRERÍAS)
# =================================================

# Número secreto pseudoaleatorio (manual, cambia cada vez que modifiques "semilla")
semilla = 12345  # Cambia este número para "variar" el secreto
minimo = 1
maximo = 50
numero_secreto = (semilla * 7 % (maximo - minimo + 1)) + minimo
# Configuración del juego
intentos_maximos = 5
intento = 1
encontrado = False
# Introducción
print("¡Bienvenido al juego de adivinar el número!")
print("Debes adivinar un número entre", minimo, "y", maximo)
print("Tienes", intentos_maximos, "intentos.\n")
# Bucle principal del juego
while intento <= intentos_maximos and not encontrado:
    entrada = input("Intento " + str(intento) + ": Ingresa tu número: ")
    
    if not entrada.isdigit():
        print("Por favor ingresa un número válido.\n")
        continue
    # Convertir entrada a entero
    valor = int(entrada)
    # Verificar el número
    if valor == numero_secreto:
        print("🎉 ¡Felicidades! Adivinaste el número", numero_secreto, "en", intento, "intento(s).")
        encontrado = True
    elif valor < numero_secreto:
        print("El número es mayor.\n")
    else:
        print("El número es menor.\n")
    # Incrementar intento
    intento += 1

if not encontrado:
    print("❌ ¡Se acabaron los intentos! El número era", numero_secreto)
