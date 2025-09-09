# -----------------------------------------------------------
# ORDENAMIENTO BURBUJA (VERSIÓN CON SINTAXIS MODIFICADA)
# -----------------------------------------------------------

def burbuja(arr):
    """
    Ordena una lista usando una versión alternativa del algoritmo burbuja.
    """
    n = len(arr)
    resultado = arr[:]  # Copia para no modificar original
    total_comparaciones = 0
    total_intercambios = 0
    paso = 1
    # Mostrar lista inicial
    print(f"Lista inicial: {resultado}\n")
# Bucle principal del algoritmo
    while paso <= n:
        intercambiado = False
        print(f"=== Paso {paso} ===")

        for k in range(n - paso):
            total_comparaciones += 1
            print(f"Comparando {resultado[k]} con {resultado[k + 1]}... ", end="")

            if resultado[k] > resultado[k + 1]:# Comparación
                # Intercambiar
                resultado[k], resultado[k + 1] = resultado[k + 1], resultado[k]
                total_intercambios += 1
                intercambiado = True
                print(f"Intercambiados → {resultado}")
            else:
                print("No se requiere intercambio")

        print(f"Estado después del paso {paso}: {resultado}\n")

        if not intercambiado:
            print("La lista ya está ordenada. Se detiene el proceso.")
            break

        paso += 1
# Mostrar lista final y estadísticas
    print(f"Lista ordenada final: {resultado}")
    print(f"Total comparaciones: {total_comparaciones}, Total intercambios: {total_intercambios}")
    return resultado


# -------------------------------
# EJEMPLO DE USO
# -------------------------------
if __name__ == "__main__":
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("ALGORITMO DE ORDENAMIENTO BURBUJA (VERSIÓN REESTRUCTURADA)")
    print("=" * 55)
    burbuja(numeros)
