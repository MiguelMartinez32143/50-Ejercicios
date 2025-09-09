# Programa que suma todos los números desde 1 hasta un límite

# Se pide al usuario el número límite
limite = int(input("¿Hasta qué número quieres sumar? "))

suma_total = 0  # Variable acumuladora

print(f"\nSumando números del 1 al {limite}...")


for numero in range(1, limite + 1):
    suma_total += numero
    print(f"Sumando {numero} - Total hasta ahora: {suma_total}")


print("\nResultado final:")
print(f"La suma de todos los números del 1 al {limite} es: {suma_total}")
print("Gracias por usar el programa")