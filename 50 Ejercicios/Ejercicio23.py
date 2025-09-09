# Analizador de texto con funciones reutilizables

def contar_palabras(texto: str) -> int:# Cuenta cuántas palabras hay en un texto
    return len(texto.split())# Cuenta palabras separadas por espacios
# Cuenta caracteres, con o sin espacios
def contar_caracteres(texto: str, incluir_espacios: bool = True) -> int:
    """Cuenta caracteres, con o sin espacios"""
    return len(texto) if incluir_espacios else len(texto.replace(" ", ""))
# Cuenta caracteres, con o sin espacios
def palabra_mas_larga(texto: str) -> str:
    """Devuelve la palabra más larga"""
    palabras = texto.split()
    return max(palabras, key=len) if palabras else ""
# Verifica si un texto es palíndromo
def es_palindromo(texto: str) -> bool:
    """Verifica si un texto es palíndromo"""
    limpio = "".join(texto.lower().split())  # quita espacios y pone minúsculas
    return limpio == limpio[::-1]

# --- Probando el analizador ---
frase = "La programación es divertida y educativa"
# Resultados del análisis
print("ANALIZADOR DE TEXTO")
print(f"Texto: '{frase}'")
print("-" * 50)
print(f"Palabras: {contar_palabras(frase)}")
print(f"Caracteres (con espacios): {contar_caracteres(frase)}")
print(f"Caracteres (sin espacios): {contar_caracteres(frase, incluir_espacios=False)}")
print(f"Palabra más larga: '{palabra_mas_larga(frase)}'")
print(f"¿Es palíndromo?: {es_palindromo(frase)}")

# Otra prueba con palíndromo
palindromo = "anita lava la tina"
print(f"\nProbando palíndromo: '{palindromo}'")

print(f"¿Es palíndromo?: {es_palindromo(palindromo)}")
