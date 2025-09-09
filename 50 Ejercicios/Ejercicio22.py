# Calculadora con funciones
# Devuelve la suma de dos números
def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números"""
    return a + b
# Devuelve la resta de dos números
def restar(a: float, b: float) -> float:
    """Devuelve la resta de dos números"""
    return a - b
# Devuelve la multiplicación de dos números
def multiplicar(a: float, b: float) -> float:
    """Devuelve la multiplicación de dos números"""
    return a * b
# Devuelve la división de dos números (valida división por cero)
def dividir(a: float, b: float):
    """Devuelve la división de dos números (valida división por cero)"""
    return a / b if b != 0 else "Error: División entre cero"

# --- Probando la calculadora ---
num1, num2 = 15, 3

print("CALCULADORA CON FUNCIONES")
print(f"Números a operar: {num1} y {num2}")
print("-" * 30)

operaciones = {
    "Suma": sumar(num1, num2),
    "Resta": restar(num1, num2),
    "Multiplicación": multiplicar(num1, num2),
    "División": dividir(num1, num2),
    "División entre cero": dividir(num1, 0)
}

for nombre, resultado in operaciones.items():
    print(f"{nombre}: {resultado}")
