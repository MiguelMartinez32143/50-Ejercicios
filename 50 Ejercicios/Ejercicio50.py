# =================================================
# INVENTARIO DE PRODUCTOS (SIN CLASES)
# =================================================

# Lista para almacenar productos
inventario = []

def agregar_producto(nombre, categoria, precio, stock):
    """
    Agrega un producto al inventario
    """
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

def buscar_por_categoria(categoria):
    """
    Muestra los productos de una categoría específica
    """
    print(f"\nProductos en la categoría '{categoria}':")
    resultados = []
    idx = 0
    while idx < len(inventario):
        p = inventario[idx]
        if p["categoria"].lower() == categoria.lower():
            print(f"- {p['nombre']}: ${p['precio']}, Stock: {p['stock']}")
            resultados.append(p)
        idx += 1
    return resultados

def estadisticas_inventario():
    """
    Calcula estadísticas generales del inventario
    """
    total_productos = len(inventario)
    total_stock = 0
    suma_precios = 0
    idx = 0
    while idx < len(inventario):
        p = inventario[idx]
        total_stock += p["stock"]
        suma_precios += p["precio"]
        idx += 1

    precio_promedio = suma_precios / max(total_productos, 1)

    print("\nEstadísticas del inventario:")
    print(f"- Total de productos: {total_productos}")
    print(f"- Stock total: {total_stock}")
    print(f"- Precio promedio: ${precio_promedio:.2f}")
    return total_productos, total_stock, precio_promedio

# =================================================
# EJEMPLO DE USO
# =================================================
agregar_producto("Laptop", "Electrónica", 1200, 5)
agregar_producto("Mouse", "Electrónica", 25, 50)
agregar_producto("Camiseta", "Ropa", 15, 30)

buscar_por_categoria("Electrónica")
estadisticas_inventario()
