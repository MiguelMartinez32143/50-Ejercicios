# -----------------------------------------------------------
# CONTADOR DE FRECUENCIAS
# -----------------------------------------------------------
# Este programa analiza una lista de elementos y cuenta cuántas
# veces aparece cada uno. Además, genera estadísticas y muestra
# cuál es el elemento más frecuente.
# -----------------------------------------------------------

def contar_frecuencias(lista):
    """
    Cuenta cuántas veces aparece cada elemento en la lista.

    Parámetros:
        lista (list): Lista de elementos a analizar.

    Retorna:
        dict: Diccionario con los elementos como claves y sus
              frecuencias como valores.
    """
    frecuencias = {}  # Diccionario para almacenar resultados
    print(f"Analizando lista: {lista}")
    print("\nProceso de conteo:")

    # Recorrer cada elemento de la lista
    for elemento in lista:
        if elemento in frecuencias:
            # Si ya existe, incrementamos su contador
            frecuencias[elemento] += 1
            print(f" {elemento}: incrementado a {frecuencias[elemento]}")
        else:
            # Primera aparición del elemento
            frecuencias[elemento] = 1
            print(f" {elemento}: primera aparición")

    return frecuencias


def encontrar_mas_frecuente(frecuencias):
    """
    Determina el elemento con mayor frecuencia.

    Parámetros:
        frecuencias (dict): Diccionario de frecuencias.

    Retorna:
        tuple: (elemento más frecuente, número de apariciones)
               Devuelve (None, 0) si el diccionario está vacío.
    """
    if not frecuencias:
        return None, 0

    # max() con key obtiene el elemento con la frecuencia más alta
    elemento_max = max(frecuencias, key=frecuencias.get)
    frecuencia_max = frecuencias[elemento_max]
    return elemento_max, frecuencia_max


def mostrar_estadisticas(frecuencias):
    """
    Muestra estadísticas detalladas de frecuencias, incluyendo:
    - Total de elementos
    - Elementos únicos
    - Frecuencias ordenadas de mayor a menor
    - Gráfico de barras simple
    - Elemento más frecuente
    """
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE FRECUENCIA")
    print("=" * 40)

    # Ordenar el diccionario por frecuencia (descendente)
    frecuencias_ordenadas = sorted(
        frecuencias.items(),
        key=lambda x: x[1],
        reverse=True
    )

    total_elementos = sum(frecuencias.values())  # Suma de todas las ocurrencias
    elementos_unicos = len(frecuencias)         # Cantidad de elementos distintos

    print(f"Total de elementos: {total_elementos}")
    print(f"Elementos únicos: {elementos_unicos}")
    print("\nFrecuencias (ordenadas por cantidad):")

    # Mostrar cada elemento con su frecuencia, porcentaje y barra visual
    for elemento, frecuencia in frecuencias_ordenadas:
        porcentaje = (frecuencia / total_elementos) * 100
        barra = "█" * frecuencia  # Gráfico de barras simple
        print(f" {elemento:>3}: {frecuencia:>2} veces ({porcentaje:4.1f}%) {barra}")

    # Obtener el elemento más frecuente
    mas_frecuente, max_freq = encontrar_mas_frecuente(frecuencias)
    print(f"\nElemento más frecuente: {mas_frecuente} ({max_freq} veces)")


# -------------------------------
# BLOQUE PRINCIPAL: PROBANDO EL CONTADOR
# -------------------------------
if __name__ == "__main__":
    print("CONTADOR DE FRECUENCIAS")
    print("=" * 30)

    # Ejemplo con números
    numeros = [1, 2, 3, 2, 1, 4, 2, 5, 2, 1, 3, 2]
    frecuencias_num = contar_frecuencias(numeros)
    mostrar_estadisticas(frecuencias_num)

    # Ejemplo con letras
    print("\n" + "=" * 50)
    texto = "programacion"
    letras = list(texto)  # Convertir el texto en lista de caracteres
    print(f"\nAnalizando la palabra: '{texto}'")
    frecuencias_letras = contar_frecuencias(letras)
    mostrar_estadisticas(frecuencias_letras)
