# =================================================
# JUEGO DE ADIVINANZA (SIN LIBRERÍAS)
# =================================================

# Número secreto (puedes cambiarlo manualmente)
numero_secreto = 7
intentos_maximos = 3

print("¡Bienvenido al juego de adivinanza!")
print("Tienes", intentos_maximos, "intentos para adivinar el número del 1 al 10")

intento = 1
while intento <= intentos_maximos:
    print("\nIntento", intento, "de", intentos_maximos)
    
    # Solicitar número al usuario
    adivinanza = input("Ingresa tu número: ")
    
    # Validar que sea un número
    if not adivinanza.isdigit():
        print("Por favor, ingresa un número válido.")
        continue
    
    adivinanza = int(adivinanza)
    
    # Comparar con el número secreto
    if adivinanza == numero_secreto:
        print("🎉 ¡GANASTE! El número era", numero_secreto)
        break
    elif adivinanza < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    intento = intento + 1
else:
    print("\n❌ ¡Se acabaron los intentos! El número era", numero_secreto)
