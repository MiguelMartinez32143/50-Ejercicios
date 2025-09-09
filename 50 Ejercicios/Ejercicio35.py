
# COMPRESIÓN DE TEXTO (Huffman + Repetición)
# NODO PARA HUFFMAN
# --------------------------------------------------
def crear_nodo(caracter=None, frecuencia=0, izquierdo=None, derecho=None):
    """Crea un nodo de árbol Huffman como diccionario"""
    return {
        "caracter": caracter,
        "frecuencia": frecuencia,
        "izquierdo": izquierdo,
        "derecho": derecho
    }

def obtener_frecuencia(nodo):
    """Devuelve la frecuencia del nodo"""
    return nodo["frecuencia"]

# --------------------------------------------------
# COMPRESIÓN POR REPETICIÓN SIMPLE
# --------------------------------------------------
def comprimir_repeticion(texto):
    """Comprime cadenas reemplazando secuencias de caracteres repetidos"""
    if not texto:
        return ""
    resultado = []
    actual = texto[0]
    contador = 1

    for c in texto[1:]:
        if c == actual:
            contador += 1
        else:
            if contador > 1:
                resultado.append(str(contador) + actual)
            else:
                resultado.append(actual)
            actual = c
            contador = 1
    # Añadir último grupo
    if contador > 1:
        resultado.append(str(contador) + actual)
    else:
        resultado.append(actual)
    return ''.join(resultado)

# --------------------------------------------------
# GENERACIÓN DE CÓDIGOS HUFFMAN
# --------------------------------------------------
def generar_codigos_huffman(texto):
    """Genera códigos Huffman para cada carácter"""
    if not texto:
        return {}

    # Contar frecuencias
    frecuencias = {}
    for c in texto:
        if c in frecuencias:
            frecuencias[c] += 1
        else:
            frecuencias[c] = 1

    # Crear lista de nodos
    nodos = [crear_nodo(caracter=k, frecuencia=v) for k, v in frecuencias.items()]

    # Construcción del árbol Huffman
    while len(nodos) > 1:
        # Ordenar por frecuencia
        nodos.sort(key=obtener_frecuencia)
        # Tomar los dos con menor frecuencia
        nodo1 = nodos.pop(0)
        nodo2 = nodos.pop(0)
        combinados = crear_nodo(
            caracter=None,
            frecuencia=nodo1["frecuencia"] + nodo2["frecuencia"],
            izquierdo=nodo1,
            derecho=nodo2
        )
        nodos.append(combinados)

    # Nodo raíz
    raiz = nodos[0]

    # Función recursiva para generar códigos
    def asignar_codigos(nodo, prefijo="", codigos=None):
        if codigos is None:
            codigos = {}
        if nodo["caracter"] is not None:
            codigos[nodo["caracter"]] = prefijo or "0"
        else:
            asignar_codigos(nodo["izquierdo"], prefijo + "0", codigos)
            asignar_codigos(nodo["derecho"], prefijo + "1", codigos)
        return codigos

    return asignar_codigos(raiz)

# --------------------------------------------------
# EJEMPLO DE USO
# --------------------------------------------------
if __name__ == "__main__":
    texto = "aaaabbbbcccdde"
    print("Texto original:", texto)

    # Compresión por repetición
    comprimido = comprimir_repeticion(texto)
    print("Compresión repetición simple:", comprimido)

    # Compresión Huffman
    codigos = generar_codigos_huffman(texto)
    print("Códigos Huffman generados:")
    for caracter in codigos:
        print(f" '{caracter}': {codigos[caracter]}")
