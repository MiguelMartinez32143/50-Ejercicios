# -----------------------------------------------------------
# SIMULACIÓN DE CRIATURAS EN 2D (SIN CLASES NI LIBRERÍAS)
# -----------------------------------------------------------

# Generador simple de números aleatorios
def numero_aleatorio(min_val, max_val):
    """
    Genera un número pseudoaleatorio entre min_val y max_val usando el tiempo.
    """
    import time
    t = int(time.time() * 1000000)  # Microsegundos
    return min_val + (t % (max_val - min_val + 1))

# Crear criatura
def crear_criatura(nombre, especie, energia=100, coord=(0,0)):
    return {
        "nombre": nombre,
        "especie": especie,
        "energia": energia,
        "coord_x": coord[0],
        "coord_y": coord[1],
        "esta_vivo": True
    }

# Deambular criatura
def deambular(criatura):
    if not criatura["esta_vivo"]:
        print(f"{criatura['nombre']} ya no se mueve (sin vida).")
        return

    # Lista de posibles desplazamientos
    movimientos = [
        (0,1),(1,0),(0,-1),(-1,0),
        (1,1),(1,-1),(-1,1),(-1,-1),(0,0)
    ]

    # Elegir movimiento aleatorio usando nuestro generador
    idx = numero_aleatorio(0, len(movimientos)-1)
    dx, dy = movimientos[idx]
    criatura["coord_x"] += dx
    criatura["coord_y"] += dy

    # Reducir energía
    criatura["energia"] -= 5
    if criatura["energia"] <= 0:
        criatura["energia"] = 0
        criatura["esta_vivo"] = False
        print(f"{criatura['nombre']} ha agotado su energía y ha muerto.")
    else:
        print(f"{criatura['nombre']} se movió a ({criatura['coord_x']}, {criatura['coord_y']}). "
              f"Energía restante: {criatura['energia']}")

# -------------------------------
# EJEMPLO DE USO
# -------------------------------
leon = crear_criatura("Leo", "carnívoro")
deambular(leon)
deambular(leon)
