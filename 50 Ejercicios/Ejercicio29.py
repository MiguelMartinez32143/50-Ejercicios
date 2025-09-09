# -----------------------------------------------------------
# GENERADOR Y ANÁLISIS DE NÚMEROS PRIMOS (VERSIÓN REESTRUCTURADA)
# -----------------------------------------------------------

def verificar_primo(n):
    """
    Verifica si un número es primo usando división hasta la raíz cuadrada.
    """
    if n < 2:
        return False

    print(f"Comprobando si {n} es primo:")
    limite = int(n ** 0.5) + 1
    for candidato in range(2, limite):
        print(f" ¿{n} divisible por {candidato}? ", end="")
        if n % candidato == 0:
            print(f"Sí → {n} / {candidato} = {n // candidato}")
            return False
        else:
            print("No")
    print(f"✅ {n} es primo")
    return True


def primos_criba(maximo):
    """
    Genera todos los primos hasta 'maximo' usando la Criba de Eratóstenes.
    """
    print(f"\nCriba de Eratóstenes hasta {maximo}")
    es_primo = [True] * (maximo + 1)
    es_primo[0:2] = [False, False]  # 0 y 1 no son primos

    for i in range(2, int(maximo ** 0.5) + 1):
        if es_primo[i]:
            print(f"\nMarcando múltiplos de {i}:")
            for multiplo in range(i*i, maximo + 1, i):
                if es_primo[multiplo]:
                    print(f" {multiplo} → no primo")
                    es_primo[multiplo] = False

    return [num for num, primo in enumerate(es_primo) if primo]


def descomponer_primos(valor):
    """
    Descompone un número en sus factores primos.
    """
    print(f"\nDescomposición en factores primos de {valor}:")
    factores = []
    divisor = 2
    numero_temp = valor

    while divisor * divisor <= numero_temp:
        while numero_temp % divisor == 0:
            factores.append(divisor)
            print(f" {numero_temp} ÷ {divisor} = {numero_temp // divisor}")
            numero_temp //= divisor
        divisor += 1

    if numero_temp > 1:
        factores.append(numero_temp)
        print(f" Factor primo final: {numero_temp}")

    return factores


# -------------------------------
# BLOQUE PRINCIPAL
# -------------------------------
if __name__ == "__main__":
    print("ANÁLISIS DE NÚMEROS PRIMOS")
    print("=" * 40)

    # 1️⃣ Verificación individual
    numeros_a_probar = [17, 25, 29]
    print("\n1. VERIFICACIÓN INDIVIDUAL:")
    for numero in numeros_a_probar:
        es_primo = verificar_primo(numero)
        estado = "es primo ✅" if es_primo else "no es primo ❌"
        print(f"Resultado: {numero} → {estado}\n")

    # 2️⃣ Criba de Eratóstenes
    print("\n2. CRIBA DE ERATÓSTENES")
    print("-" * 30)
    primos_hasta_30 = primos_criba(30)
    print(f"\nPrimos hasta 30: {primos_hasta_30}")
    print(f"Cantidad de primos encontrados: {len(primos_hasta_30)}")

    # 3️⃣ Factorización prima
    print("\n3. FACTORIZACIÓN PRIMA")
    print("-" * 30)
    numero_a_factorizar = 60
    factores = descomponer_primos(numero_a_factorizar)
    print(f"\n{numero_a_factorizar} = {' × '.join(map(str, factores))}")

    # Verificación del producto
    producto = 1
    for f in factores:
        producto *= f
    print(f"Verificación: {' × '.join(map(str, factores))} = {producto}")
