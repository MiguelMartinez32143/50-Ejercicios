# =================================================
# ORGANIZADOR DE LISTA (SIN LIBRERÍAS)
# =================================================
# Funciones para ordenar y manipular listas sin usar librerías externas
numeros = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
# Mostrar lista original
print("Lista original:", numeros)
print("Cantidad de elementos:", len(numeros))

# Crear copias para no modificar la original
ascendente = []
descendente = []
mezclada = []
invertida = []

# Copiar lista
i = 0
while i < len(numeros):
    ascendente.append(numeros[i])
    descendente.append(numeros[i])
    mezclada.append(numeros[i])
    invertida.append(numeros[i])
    i += 1

# Orden ascendente (método burbuja)
n = len(ascendente)
i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        if ascendente[j] > ascendente[j + 1]:
            ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
        j += 1
    i += 1
print("\nOrden ascendente:", ascendente)

# Orden descendente (método burbuja modificado)
i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        if descendente[j] < descendente[j + 1]:
            descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
        j += 1
    i += 1
print("Orden descendente:", descendente)

# Mezclar la lista (intercambios simples)
i = 0
while i < n:
    j = n - i - 1
    mezclada[i], mezclada[j] = mezclada[j], mezclada[i]
    i += 2
print("Lista mezclada:", mezclada)

# Invertir la lista original
invertida_final = []
i = len(invertida) - 1
while i >= 0:
    invertida_final.append(invertida[i])
    i -= 1
print("Orden invertido:", invertida_final)

# La lista original sigue igual
print("\nLista original (sin cambios):", numeros)
