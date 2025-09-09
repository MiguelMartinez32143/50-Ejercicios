# Programa que calcula el promedio de tres calificaciones

# Se leen las tres notas desde teclado en una sola línea
notas = list(map(float, input("Ingresa tres calificaciones separadas por espacio: ").split()))

# Se calcula el promedio usando la función sum() y la longitud de la lista
promedio = sum(notas) / len(notas)

# Se muestran los resultados
print(f"Calificaciones: {notas}")
print(f"Promedio: {promedio}")
