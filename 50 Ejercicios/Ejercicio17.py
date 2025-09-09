# Programa que gestiona una lista de compras

# Se crea la lista inicial de compras
compras = ["pan", "leche", "huevos"]
print("Lista inicial:", compras)

# Agregar varios elementos de una sola vez usando extend()
compras.extend(["queso", "yogur"])
print("\nDespués de agregar queso y yogur:")
print(compras)

# Insertar en una posición específica (ejemplo: posición 1)
compras[1:1] = ["mantequilla"]  # Otra forma de insertar sin usar insert()
print("\nDespués de insertar mantequilla en posición 1:")
print(compras)

# Eliminar un elemento usando comprensión de listas (eliminamos "huevos")
compras = [item for item in compras if item != "huevos"]
print("\nDespués de eliminar huevos:")
print(compras)

# Eliminar el primer elemento usando slicing
elemento_eliminado, compras = compras[0], compras[1:]
print(f"\nEliminamos el primer elemento: {elemento_eliminado}")
print("Lista final:", compras)
