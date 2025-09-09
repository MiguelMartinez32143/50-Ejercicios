# =================================================
# REGISTRO Y RANKING DE ESTUDIANTES
# =================================================

# Lista para almacenar los estudiantes
estudiantes = []

def agregar_estudiante(nombre, notas):
    """
    Agrega un estudiante con su lista de notas
    """
    estudiante = {"nombre": nombre, "notas": notas}
    estudiantes.append(estudiante)
    print(f"Estudiante '{nombre}' agregado con notas: {notas}")

def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas
    """
    if not notas:
        return 0
    return sum(notas) / len(notas)

def mostrar_ranking():
    """
    Muestra los estudiantes ordenados por promedio descendente
    """
    print("\nRanking de estudiantes:")
    ranking = estudiantes.copy()
    # Ordenamiento simple tipo burbuja
    n = len(ranking)
    for i in range(n):
        for j in range(0, n-i-1):
            if calcular_promedio(ranking[j]["notas"]) < calcular_promedio(ranking[j+1]["notas"]):
                ranking[j], ranking[j+1] = ranking[j+1], ranking[j]
    for est in ranking:
        promedio = calcular_promedio(est["notas"])
        print(f"- {est['nombre']}: promedio {promedio:.2f}")

def consultar_estudiante(nombre):
    """
    Muestra el promedio de un estudiante por su nombre
    """
    for est in estudiantes:
        if est["nombre"].lower() == nombre.lower():
            promedio = calcular_promedio(est["notas"])
            print(f"{est['nombre']} tiene un promedio de {promedio:.2f}")
            return
    print(f"No se encontró al estudiante '{nombre}'")

# =================================================
# EJEMPLO DE USO
# =================================================
agregar_estudiante("Ana", [8, 9, 7])
agregar_estudiante("Carlos", [10, 9, 10])
agregar_estudiante("María", [7, 8, 6])

mostrar_ranking()
consultar_estudiante("Carlos")
