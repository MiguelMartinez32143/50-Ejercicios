def contar_vocales(texto):# Función para contar vocales
    """
    Cuenta cuántas veces aparece cada vocal en un texto
    """# vocales a considerar
    vocales = "aeiou"
    conteo = {v:0 for v in vocales} # inicializar conteo
    for letra in texto.lower():# recorrer cada letra del texto
        if letra in vocales:
            conteo[letra] += 1
    return conteo # retornar el conteo

# Ejemplo
texto = "Este es un ejemplo de texto con varias vocales"
print(f"Conteo de vocales: {contar_vocales(texto)}")
