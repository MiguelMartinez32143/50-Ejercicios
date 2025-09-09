# Comparación de algoritmos de búsqueda: Binaria vs Lineal

def busqueda_binaria(arr, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    
    Parámetros:
        arr (list): Lista de elementos ordenados.
        objetivo (int/float/str): Elemento a buscar.
    
    Retorna:
        int: Posición del elemento si se encuentra, -1 si no.
    """
    # Definir los límites iniciales de búsqueda
    izquierda, derecha = 0, len(arr) - 1
    iteracion = 0  # Contador de iteraciones

    print(f"\nIniciando búsqueda binaria para {objetivo} en {arr}")
    
    # Mientras el rango sea válido
    while izquierda <= derecha:
        iteracion += 1
        # Calcular la posición central
        medio = (izquierda + derecha) // 2
        valor_medio = arr[medio]

        # Mostrar información de depuración
        print(f"\nIteración {iteracion}: Rango [{izquierda}, {derecha}], Medio {medio} → {valor_medio}")

        # Caso 1: Se encontró el elemento
        if valor_medio == objetivo:
            print(f"✅ Elemento encontrado en posición {medio}")
            return medio
        # Caso 2: El valor medio es menor → buscar en mitad derecha
        elif valor_medio < objetivo:
            print(f"➡ {valor_medio} < {objetivo}, buscar en la mitad derecha")
            izquierda = medio + 1
        # Caso 3: El valor medio es mayor → buscar en mitad izquierda
        else:
            print(f"⬅ {valor_medio} > {objetivo}, buscar en la mitad izquierda")
            derecha = medio - 1

    # Si el bucle termina, el elemento no se encuentra
    print(f"\n❌ {objetivo} no se encuentra en la lista tras {iteracion} iteraciones")
    return -1


def busqueda_lineal(arr, objetivo):
    """
    Realiza una búsqueda lineal recorriendo la lista elemento por elemento.
    
    Parámetros:
        arr (list): Lista de elementos.
        objetivo (int/float/str): Elemento a buscar.
    
    Retorna:
        tuple: (posición del elemento, número de comparaciones realizadas)
               Devuelve (-1, comparaciones) si no se encuentra.
    """
    # Recorremos cada elemento de la lista
    for indice, valor in enumerate(arr, start=0):
        if valor == objetivo:
            # Se encontró el elemento: retornamos posición y comparaciones
            return indice, indice + 1
    # Si no se encuentra el elemento
    return -1, len(arr)


def main():
    """
    Función principal para ejecutar y comparar ambos algoritmos de búsqueda.
    """
    # Lista de ejemplo (ordenada para búsqueda binaria)
    numeros = [11, 22, 25, 34, 44, 55, 66, 77, 88, 99]
    objetivo = 55

    # Encabezado
    print("\nCOMPARACIÓN DE BÚSQUEDA BINARIA Y LINEAL")
    print("=" * 50)
    print(f"Lista: {numeros}\nElemento a buscar: {objetivo}")

    # Ejecutar búsqueda binaria
    print("\n 1️ Búsqueda Binaria")
    print("-" * 25)
    posicion_bin = busqueda_binaria(numeros, objetivo)

    # Ejecutar búsqueda lineal
    print("\n 2️ Búsqueda Lineal")
    print("-" * 25)
    posicion_lin, comparaciones = busqueda_lineal(numeros, objetivo)
    print(f"Comparaciones realizadas: {comparaciones}")
    if posicion_lin != -1:
        print(f"Elemento encontrado en posición {posicion_lin}")

    # Conclusión sobre eficiencia
    print("\n Conclusión: La búsqueda binaria suele requerir menos comparaciones en listas grandes")


# Ejecutar el programa si se llama directamente
if __name__ == "__main__":
    main()
