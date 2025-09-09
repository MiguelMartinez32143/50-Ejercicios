# =================================================
# ANÁLISIS DE TEXTO SIN LIBRERÍAS
# =================================================
# Funciones para análisis básico de texto sin usar librerías externas
def evaluar_estructura(texto):
    """Analiza estructura básica del texto"""
    num_caracteres = len(texto)
    num_sin_espacios = len(texto.replace(" ", ""))
    palabras = texto.split()
    num_palabras = len(palabras)
    num_oraciones = texto.count('.') + texto.count('!') + texto.count('?')
    num_parrafos = texto.count('\n\n') + 1 if texto.strip() else 0
    # Retornar estadísticas
    return {
        "caracteres_totales": num_caracteres,
        "caracteres_sin_espacios": num_sin_espacios,
        "palabras": num_palabras,
        "oraciones": num_oraciones,
        "parrafos": num_parrafos
    }
# Funciones para extraer patrones simples sin regex
def extraer_emails(texto):
    """Busca patrones simples de emails (sin regex)"""
    emails = []
    partes = texto.split()
    for palabra in partes:
        if '@' in palabra and '.' in palabra:
            emails.append(palabra)
    return emails
    # Función para extraer números de teléfono simples
def extraer_telefonos(texto):
    """Busca números de teléfono simples (sin regex)"""
    telefonos = []
    partes = texto.split()
    for palabra in partes:
        numeros = ''.join(c for c in palabra if c.isdigit())
        if len(numeros) >= 10:
            telefonos.append(numeros)
    return telefonos
# función para análisis de sentimiento simple
def analisis_sentimiento_simple(texto):
    """Detecta sentimiento básico con palabras clave"""
    # Listas de palabras positivas y negativas
    positivas = ["excelente", "genial", "fantastico", "increible", "perfecto",
                 "bueno", "feliz", "contento", "alegre", "maravilloso"]
    negativas = ["terrible", "malo", "horrible", "triste", "enojado",
                 "molesto", "frustrado", "decepcionado", "pesimo"]
    texto_lower = texto.lower()
    cont_pos = sum(1 for p in positivas if p in texto_lower)
    cont_neg = sum(1 for n in negativas if n in texto_lower)
    if cont_pos > cont_neg:
        sentimiento = "Positivo"# para el caso de empate
    elif cont_neg > cont_pos:
        sentimiento = "Negativo"# si son iguales o ninguno
    else:
        sentimiento = "Neutral"# Retornar resultado
    return {
        "sentimiento": sentimiento,
        "positivas_encontradas": cont_pos,
        "negativas_encontradas": cont_neg
    }
# Función para encontrar palabras repetidas

def palabras_repetidas(texto, longitud_min=4):
    """Encuentra palabras repetidas sin regex"""
    palabras = [p.strip('.,!?;:()').lower() for p in texto.split()]
    freq = {}
    for p in palabras:
        if len(p) >= longitud_min:
            freq[p] = freq.get(p, 0) + 1
    return {p: f for p, f in freq.items() if f > 1}

def resumen_legible(estadisticas):
    """Genera resumen simple legible"""
    palabras_por_oracion = estadisticas["palabras"] / max(estadisticas["oraciones"], 1)
    resumen = [
        f"Caracteres totales: {estadisticas['caracteres_totales']}",
        f"Palabras: {estadisticas['palabras']} en {estadisticas['oraciones']} oraciones",
        f"Promedio de palabras por oración: {palabras_por_oracion:.1f}"
    ]
    if estadisticas["parrafos"] > 1:
        resumen.append(f"Organizado en {estadisticas['parrafos']} párrafos")
    return resumen
# Función principal para análisis completo
def analisis_completo(texto):
    """Realiza un análisis completo sin librerías"""
    print("=== ANÁLISIS COMPLETO DEL TEXTO ===\n")
    estructura = evaluar_estructura(texto)
    print("Estructura del texto:", estructura, "\n")# Extraer emails y teléfonos
    print("Emails encontrados:", extraer_emails(texto))# Extraer emails
    print("Teléfonos encontrados:", extraer_telefonos(texto))# Extraer teléfonos
    print("Sentimiento:", analisis_sentimiento_simple(texto))
    print("Palabras repetidas:", palabras_repetidas(texto))
    print("\nResumen legible:")
    for linea in resumen_legible(estructura):
        print(" -", linea)

# =====================
# EJEMPLO DE USO
# =====================
texto_ejemplo = """Hola, mi correo es ejemplo@mail.com. 
Si deseas llamarme, mi teléfono es 1234567890. 
Estoy muy feliz con el resultado, fue excelente y maravilloso!"""
analisis_completo(texto_ejemplo)
