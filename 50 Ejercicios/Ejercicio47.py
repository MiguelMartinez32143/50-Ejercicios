# =================================================
# GENERADOR DE CONTRASEÑAS SEGURAS SIN LIBRERÍAS
# =================================================

def generar_contrasena_segura(longitud=12, usar_mayus=True, usar_numeros=True, usar_simbolos=True):
    """
    Genera una contraseña segura combinando letras, números y símbolos
    """
    # Definir manualmente los caracteres posibles
    letras_minus = "abcdefghijklmnopqrstuvwxyz"
    letras_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()-_=+"

    # Construir conjunto de caracteres según parámetros
    caracteres = letras_minus
    if usar_mayus:
        caracteres += letras_mayus
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos

    # Generar contraseña eligiendo caracteres aleatorios
    contrasena = ""
    for _ in range(longitud):
        indice = int(random_float() * len(caracteres))
        contrasena += caracteres[indice]

    # Mostrar mensaje de seguridad según complejidad
    tipo = []
    if usar_mayus: tipo.append("mayúsculas")
    if usar_numeros: tipo.append("números")
    if usar_simbolos: tipo.append("símbolos")
    print(f"Contraseña generada ({longitud} caracteres, incluye {'/'.join(tipo)}): {contrasena}")
    
    return contrasena

# =================================================
# FUNCIONES AUXILIARES SIN LIBRERÍAS
# =================================================
seed = 1
def random_float():
    """Genera un número pseudoaleatorio entre 0 y 1 usando LCG simple"""
    global seed
    # Parámetros de LCG: m = 2**31, a = 1103515245, c = 12345
    seed = (1103515245 * seed + 12345) % (2**31)
    return seed / (2**31)

# =================================================
# EJEMPLO DE USO
# =================================================
generar_contrasena_segura(16)
