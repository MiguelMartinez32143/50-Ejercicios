# Programa que muestra la tabla de multiplicar de un número

# Se pide el número al usuario
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")
print("=" * 25)  # Línea decorativa

# Se recorre del 1 al 10 usando for
for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")

print("=" * 25)
print("¡Tabla completa!")  
print("Gracias por usar el programa.")
