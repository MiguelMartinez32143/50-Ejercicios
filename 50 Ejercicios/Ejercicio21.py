# Ejemplo de función que genera un saludo

def saludar(nombre: str) -> str:
    """
    Devuelve un saludo personalizado.
    Parámetros:
        nombre (str): nombre de la persona
    Retorna:
        str: mensaje de saludo
    """
    return f"¡Hola {nombre}! ¿Cómo estás?"

# Guardar resultados en variables
saludos = [saludar("Ana"), saludar("Carlos"), saludar("María")]

print("Usando mi función de saludo:")
for mensaje in saludos:
    print(mensaje)

# También se puede invocar directamente dentro de print()
print("\nUsando directamente:")
print(saludar("Pedro"))
print(saludar("Laura"))
