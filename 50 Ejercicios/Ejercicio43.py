def factorial(n):
    """
    Calcula el factorial de un número usando recursión
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Probando la función
numeros = [0, 3, 5, 7]
for num in numeros:
    print(f"{num}! = {factorial(num)}")
