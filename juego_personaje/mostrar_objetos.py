from datos import objetos
# Función para mostrar todos los objetos disponibles
def mostrar_objetos():
    print("\n--- Objetos disponibles ---")
    for categoria, items in objetos.items():
        print(f"\n{categoria.capitalize()}:")
        for nombre, stats in items.items():
            print(f"  {nombre} -> {stats}")
