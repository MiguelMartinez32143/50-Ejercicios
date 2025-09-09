# ==================================================
# SISTEMA DE BIBLIOTECA
# ==================================================

# -------------------------------------------------
# Diccionario para almacenar libros y sus copias
# -------------------------------------------------
catalogo_libros = {}  # {'titulo': cantidad_disponible}

# -------------------------------------------------
# Función para agregar libros
# -------------------------------------------------
def agregar_libro(titulo, cantidad=1):
    """Agrega copias de un libro al catálogo"""
    if titulo in catalogo_libros:
        catalogo_libros[titulo] += cantidad
    else:
        catalogo_libros[titulo] = cantidad
    print(f"Se agregaron {cantidad} copia(s) de '{titulo}'")

# -------------------------------------------------
# Función para prestar un libro
# -------------------------------------------------
def prestar_libro(titulo):
    """Presta un libro si hay copias disponibles"""
    if catalogo_libros.get(titulo, 0) > 0:
        catalogo_libros[titulo] -= 1
        print(f"Se prestó el libro '{titulo}'")
    else:
        print(f"No hay copias disponibles de '{titulo}'")

# -------------------------------------------------
# Función para mostrar el catálogo
# -------------------------------------------------
def mostrar_catalogo():
    """Muestra todos los libros con sus copias disponibles"""
    print("\n--- CATÁLOGO DE LIBROS ---")
    if catalogo_libros:
        for titulo, cantidad in catalogo_libros.items():
            print(f" {titulo}: {cantidad} copia(s) disponibles")
    else:
        print("El catálogo está vacío.")

# -------------------------------------------------
# EJEMPLO DE USO
# -------------------------------------------------
agregar_libro("1984", 3)
prestar_libro("1984")
mostrar_catalogo()
agregar_libro("El Principito", 2)
prestar_libro("Cien Años de Soledad")  # Intento de préstamo sin existencias
mostrar_catalogo()
