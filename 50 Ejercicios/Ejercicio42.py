# =================================================
# GENERADOR DE CONTRASEÑAS (SIN LIBRERÍAS)
# =================================================

# Función para generar contraseña segura
def generar_contrasena(longitud=12):
    """Genera una contraseña con letras, números y símbolos"""
    # manualmente definimos conjuntos de caracteres
    letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"# numeros del 0 al 9
    simbolos = "!@#$%&*?"# Conjunto de caracteres
    
    todos_caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos
    
    contrasena = ""
    semilla = 7  # Número base para "aleatoriedad" simple
    
    for i in range(longitud):
        # Generar índice pseudoaleatorio
        semilla = (semilla * 3 + i + 5) % len(todos_caracteres)
        contrasena += todos_caracteres[semilla]
    
    return contrasena

# =================================================
# PRUEBA DEL GENERADOR
# =================================================
for i in range(3):
    print(f"Contraseña generada {i+1}: {generar_contrasena()}")
