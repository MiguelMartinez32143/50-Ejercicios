# VIAJANTE DE COMERCIO (FUERZA BRUTA, SIN LIBRERÍAS)

# Generador pseudoaleatorio simple

semilla = 987654

def numero_aleatorio(min_val, max_val):
    """Generador de números pseudoaleatorios usando congruencia lineal"""
    global semilla
    semilla = (1103515245 * semilla + 12345) % 2**31
    return min_val + (semilla % (max_val - min_val + 1))

# ----------------------------------------------------
# Funciones de distancia
# ----------------------------------------------------
def distancia(ciudad_a, ciudad_b):
    """Calcula distancia euclidiana aproximada entre dos puntos"""
    dx = ciudad_b[0] - ciudad_a[0]
    dy = ciudad_b[1] - ciudad_a[1]
    # sqrt(dx^2 + dy^2) sin usar math
    potencia = dx*dx + dy*dy
    # Aproximar sqrt usando exponentes y método simple
    raiz = potencia ** 0.5
    return round(raiz, 2)

def distancia_total(ciudades, ruta):
    """Suma las distancias de una ruta circular"""
    total = 0
    n = len(ruta)
    for i in range(n):
        actual = ciudades[ruta[i]]
        siguiente = ciudades[ruta[(i+1) % n]]  # ciclo de vuelta al inicio
        total += distancia(actual, siguiente)
    return round(total, 2)

# ----------------------------------------------------
# Generador de permutaciones (sin itertools)
# ----------------------------------------------------
def permutaciones(lista):
    """Genera todas las permutaciones de una lista"""
    if len(lista) == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        elem = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([elem] + p)
    return resultado

# ----------------------------------------------------
# Fuerza bruta TSP
# ----------------------------------------------------
def fuerza_bruta_tsp(ciudades):
    n = len(ciudades)
    if n > 8:
        print("¡Advertencia! Muchas ciudades para fuerza bruta.")
        return None, None

    print(f"Probando todas las rutas posibles para {n} ciudades...")
    indices = list(range(n))
    mejores_ruta = None
    distancia_min = 1e9

    for ruta in permutaciones(indices):
        d = distancia_total(ciudades, ruta)
        if d < distancia_min:
            distancia_min = d
            mejores_ruta = ruta
    return mejores_ruta, distancia_min

# ----------------------------------------------------
# EJEMPLO DE USO
# ----------------------------------------------------
if __name__ == "__main__":
    num_ciudades = 5
    ciudades = []
    for _ in range(num_ciudades):
        x = numero_aleatorio(0, 50)
        y = numero_aleatorio(0, 50)
        ciudades.append((x, y))

    print("Ciudades (coordenadas):", ciudades)

    ruta_optima, distancia_optima = fuerza_bruta_tsp(ciudades)
    if ruta_optima:
        print("\nRuta óptima encontrada:")
        for i in ruta_optima:
            print(ciudades[i], end=" -> ")
        print(ciudades[ruta_optima[0]])  # cerrar ciclo
        print(f"Distancia total: {distancia_optima}")
