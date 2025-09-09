# Programa que detecta números pares en un rango

# Se pide al usuario el límite superior
limite = int(input("Ingresa hasta qué número quieres buscar pares: "))

pares_encontrados = 0  # Contador de pares

print(f"\nBuscando números pares entre 1 y {limite}:")

# Se recorre con un bucle for en lugar de while
for numero in range(1, limite + 1):
    if numero % 2 == 0:  # Verifica si el número es par
        print(f"{numero} es par")
        pares_encontrados += 1

# Se muestra el resumen final
print("\nResumen:")
print(f"Se encontraron {pares_encontrados} números pares")
