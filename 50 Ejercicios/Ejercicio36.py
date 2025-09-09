# =================================================
# SIMULADOR DE TIENDA DE FRUTAS
# =================================================

# -------------------------------------------------
# Inicialización de stock y ventas
# -------------------------------------------------
stock_frutas = {
    "manzana": 10,
    "banana": 15,
    "naranja": 8
}

ventas_totales = {}

# -------------------------------------------------
# Función para vender frutas
# -------------------------------------------------
def vender_fruta(fruta, cantidad):
    """Vende una cantidad de fruta si hay suficiente stock"""
    if fruta in stock_frutas:
        if stock_frutas[fruta] >= cantidad:
            stock_frutas[fruta] -= cantidad
            if fruta in ventas_totales:
                ventas_totales[fruta] += cantidad
            else:
                ventas_totales[fruta] = cantidad
            print(f"Vendidas {cantidad} {fruta}(s).")
        else:
            print(f"No hay suficiente stock de {fruta}. Stock disponible: {stock_frutas[fruta]}")
    else:
        print(f"La fruta '{fruta}' no está disponible en la tienda.")

# -------------------------------------------------
# Función para mostrar reporte
# -------------------------------------------------
def mostrar_reporte():
    """Imprime el stock actual y las ventas acumuladas"""
    print("\n--- REPORTE DE LA TIENDA ---")
    print("Stock actual:")
    for fruta, cantidad in stock_frutas.items():
        print(f" {fruta}: {cantidad}")
    print("Ventas totales:")
    if ventas_totales:
        for fruta, cantidad in ventas_totales.items():
            print(f" {fruta}: {cantidad}")
    else:
        print(" No se han registrado ventas aún.")

# -------------------------------------------------
# EJEMPLO DE USO
# -------------------------------------------------
vender_fruta("manzana", 5)
vender_fruta("banana", 20)  # Intento de venta mayor al stock
vender_fruta("naranja", 3)

mostrar_reporte()
