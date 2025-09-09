    # =================================================
# SIMULADOR DE LANZAMIENTO DE DADOS (SIN RANDOM)
# =================================================

# Función simple para generar número pseudoaleatorio entre 1 y 6
def dado_aleatorio(seed):
    # Generador congruencial lineal simple
    seed = (seed * 5 + 3) % 6
    return seed + 1, seed  # +1 para que vaya de 1 a 6

def lanzar_dados(cantidad=2, intentos=5):
    """
    Simula lanzamientos de 'cantidad' de dados por 'intentos' veces.
    Devuelve resultados y suma promedio.
    """
    resultados = []
    seed = 7  # semilla inicial para pseudoaleatoriedad

    for i in range(intentos):
        lanzamiento = []
        for _ in range(cantidad):
            valor, seed = dado_aleatorio(seed)
            lanzamiento.append(valor)
        resultados.append(lanzamiento)
        print(f"Lanzamiento {i+1}: {lanzamiento} -> Suma: {sum(lanzamiento)}")

    # Calcular promedio de sumas
    suma_total = 0
    for lan in resultados:
        suma_total += sum(lan)
    promedio = suma_total / intentos
    print(f"\nPromedio de la suma de los lanzamientos: {promedio:.2f}")

    return resultados, promedio

# =================================================
# PRUEBA DEL SIMULADOR
# =================================================
lanzar_dados(cantidad=3, intentos=7)
