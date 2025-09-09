import random
import string

# -----------------------------------------------------------
# GENERADOR Y EVALUADOR DE CONTRASEÑAS
# -----------------------------------------------------------

def generar_contraseña(longitud=8, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=False):
    """
    Genera una contraseña aleatoria con las características especificadas.
    - longitud: cantidad de caracteres
    - incluir_mayusculas: si True, se agregan letras mayúsculas
    - incluir_numeros: si True, se agregan números
    - incluir_simbolos: si True, se agregan símbolos
    """
    caracteres = string.ascii_lowercase  # Letras minúsculas (base)

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Agregar mayúsculas

    if incluir_numeros:
        caracteres += string.digits  # Agregar números 0-9

    if incluir_simbolos:
        caracteres += "!@#$%&*"  # Agregar símbolos básicos

    # Construcción de la contraseña carácter por carácter
    contraseña = ""
    for i in range(longitud):
        caracter_aleatorio = random.choice(caracteres)  # Se elige un caracter de forma aleatoria
        contraseña += caracter_aleatorio

    return contraseña


def evaluar_fortaleza(contraseña):
    """
    Evalúa qué tan fuerte es una contraseña según:
    - Longitud
    - Inclusión de mayúsculas
    - Inclusión de números
    """
    puntos = 0
    comentarios = []

    # Longitud
    if len(contraseña) >= 8:
        puntos += 2
        comentarios.append("✔ Longitud adecuada")
    else:
        comentarios.append("✘ Muy corta (mínimo 8 caracteres)")

    # Mayúsculas
    if any(c.isupper() for c in contraseña):
        puntos += 1
        comentarios.append("✔ Contiene mayúsculas")
    else:
        comentarios.append("✘ Sin mayúsculas")

    # Números
    if any(c.isdigit() for c in contraseña):
        puntos += 1
        comentarios.append("✔ Contiene números")
    else:
        comentarios.append("✘ Sin números")

    # Evaluación final
    if puntos >= 4:
        fortaleza = "Muy fuerte"
    elif puntos >= 3:
        fortaleza = "Fuerte"
    elif puntos >= 2:
        fortaleza = "Moderada"
    else:
        fortaleza = "Débil"

    return fortaleza, comentarios


# -------------------------------
# PROBANDO EL GENERADOR
# -------------------------------
print("GENERADOR DE CONTRASEÑAS")
print("=" * 40)

# Generar contraseñas con diferentes configuraciones
contraseña1 = generar_contraseña(12, True, True, False)
contraseña2 = generar_contraseña(8, True, True, True)
contraseña3 = generar_contraseña(6, False, False, False)

# Lista de pruebas
contraseñas = [
    ("Estándar (12 caracteres)", contraseña1),
    ("Con símbolos (8 caracteres)", contraseña2),
    ("Solo minúsculas (6 caracteres)", contraseña3)
]

# Evaluación de las contraseñas generadas
for descripcion, contraseña in contraseñas:
    fortaleza, comentarios = evaluar_fortaleza(contraseña)
    print(f"\n{descripcion}:")
    print(f"Contraseña: {contraseña}")
    print(f"Fortaleza: {fortaleza}")
    for comentario in comentarios:
        print(f" - {comentario}")
