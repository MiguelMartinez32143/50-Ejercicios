# Programa que convierte grados Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):        # Función para realizar la conversión
    return (celsius * 9/5) + 32

# Se pide al usuario la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)  # Se llama la función de conversión

# Se muestra el resultado en pantalla
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")
