# Programa que muestra y accede a una lista de colores favoritos

# Se pide al usuario que ingrese sus colores favoritos separados por comas
colores = input("Ingresa tus colores favoritos separados por comas: ").split(",")

# Se eliminan posibles espacios en blanco alrededor de cada color
colores = [color.strip() for color in colores]

# Se muestran los datos generales de la lista
print("\nMis colores favoritos son:")
print(f"Lista completa: {colores}")
print(f"Total de colores: {len(colores)}")

# Acceso a posiciones específicas usando índices
print("\nAccediendo a colores individuales:")
print(f"Primer color: {colores[0]}")
print(f"Segundo color: {colores[1]}")
print(f"Último color: {colores[-1]}")
print(f"Penúltimo color: {colores[-2]}")
