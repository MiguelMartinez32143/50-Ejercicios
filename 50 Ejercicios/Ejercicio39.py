def analizar_texto(texto):
    """
    Analiza un texto para contar palabras y frases únicas
    """# Normalizar y separar
    palabras = texto.lower().split()
    frases = [f.strip() for f in texto.split('.') if f.strip()]
    # Usar conjuntos para encontrar únicos
    palabras_unicas = set(palabras)
    frases_unicas = set(frases)
    # Mostrar resultados
    print(f"Total de palabras: {len(palabras)}")
    print(f"Palabras únicas: {len(palabras_unicas)}")
    print(f"Total de frases: {len(frases)}")
    print(f"Frases únicas: {len(frases_unicas)}")

# Ejemplo
texto = "Hola mundo. Esto es un texto. Hola mundo."
analizar_texto(texto)
