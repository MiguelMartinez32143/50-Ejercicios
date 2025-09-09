# =================================================
# JUEGO DE LA VIDA SIN LIBRERÍAS
# =================================================

import time  # Solo para obtener la hora actual (para pseudoaleatoriedad)

# -------------------------------------------------
# Función para generar un número pseudoaleatorio
# -------------------------------------------------
def generar_numero_pseudoaleatorio(minimo, maximo):
    """
    Genera un número pseudoaleatorio entre minimo y maximo
    usando la hora actual en milisegundos.
    """
    ahora = int(time.time() * 1000)  # milisegundos actuales
    return (ahora % (maximo - minimo + 1)) + minimo

# -------------------------------------------------
# Inicialización del tablero
# -------------------------------------------------
def inicializar_tablero(filas, columnas, probabilidad=0.3):
    """
    Crea un tablero de tamaño filas x columnas
    con células vivas (1) y muertas (0) según probabilidad.
    """
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Simula azar con la función pseudoaleatoria
            valor = generar_numero_pseudoaleatorio(0, 100) / 100.0
            if valor < probabilidad:
                fila.append(1)  # Célula viva
            else:
                fila.append(0)  # Célula muerta
        tablero.append(fila)
    return tablero

# -------------------------------------------------
# Contar vecinos vivos
# -------------------------------------------------
def contar_vecinos(tablero, x, y):
    """
    Cuenta cuántos vecinos vivos tiene la célula en la posición (x, y)
    revisando la vecindad de 3x3 alrededor.
    """
    total = 0
    filas = len(tablero)
    columnas = len(tablero[0])
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nx, ny = x + dx, y + dy
            # Ignorar la propia célula y controlar límites
            if (dx != 0 or dy != 0) and 0 <= nx < filas and 0 <= ny < columnas:
                total += tablero[nx][ny]
    return total

# -------------------------------------------------
# Generar la siguiente generación
# -------------------------------------------------
def siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en la siguiente generación
    aplicando las reglas de Conway:
      - Célula viva con <2 o >3 vecinos muere
      - Célula muerta con 3 vecinos nace
      - Célula viva con 2 o 3 vecinos sobrevive
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = []
    cambios = []  # Para registrar qué células cambiaron

    for i in range(filas):
        fila_nueva = []
        for j in range(columnas):
            vecinos = contar_vecinos(tablero, i, j)
            estado = tablero[i][j]
            if estado == 1:
                if vecinos < 2 or vecinos > 3:
                    fila_nueva.append(0)  # Célula muere
                    cambios.append((i,j,"murió"))
                else:
                    fila_nueva.append(1)  # Sobrevive
            else:
                if vecinos == 3:
                    fila_nueva.append(1)  # Célula nace
                    cambios.append((i,j,"nació"))
                else:
                    fila_nueva.append(0)  # Sigue muerta
        nuevo_tablero.append(fila_nueva)
    return nuevo_tablero, cambios

# -------------------------------------------------
# Mostrar tablero en consola
# -------------------------------------------------
def mostrar(tablero, generacion):
    """
    Imprime el tablero en consola usando '■' para células vivas
    y espacios para células muertas.
    """
    print(f"\n--- Generación {generacion} ---")
    for fila in tablero:
        linea = ""
        for celula in fila:
            linea += "■" if celula else " "
        print(linea)

# -------------------------------------------------
# Función principal para ejecutar el juego
# -------------------------------------------------
def ejecutar_juego(filas, columnas, pasos=5, densidad=0.3):
    """
    Controla la ejecución del Juego de la Vida.
    - filas, columnas: tamaño del tablero
    - pasos: cuántas generaciones mostrar
    - densidad: probabilidad inicial de células vivas
    """
    tablero = inicializar_tablero(filas, columnas, densidad)
    
    for gen in range(1, pasos+1):
        mostrar(tablero, gen)  # Mostrar tablero actual
        tablero, cambios = siguiente_generacion(tablero)  # Calcular siguiente generación
        
        # Mostrar cambios de esta generación
        if cambios:
            print("Cambios en esta generación:")
            for x,y,motivo in cambios:
                print(f"  Célula ({x},{y}) {motivo}")
        
        # Simular retraso sin librerías
        for _ in range(5000000):
            pass

# -------------------------------------------------
# EJEMPLO DE EJECUCIÓN
# -------------------------------------------------
ejecutar_juego(filas=8, columnas=12, pasos=5, densidad=0.4)
