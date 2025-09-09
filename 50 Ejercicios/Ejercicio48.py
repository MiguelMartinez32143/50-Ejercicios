# =================================================
# GESTOR DE TAREAS SIN LIBRERÍAS
# =================================================

# Lista global de tareas
tareas = []

def agregar_tarea(descripcion, prioridad):
    """
    Agrega una tarea con su prioridad a la lista
    Menor número = mayor prioridad
    """
    tarea = {"descripcion": descripcion, "prioridad": prioridad}
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' agregada con prioridad {prioridad}.")

def mostrar_tareas():
    """
    Muestra las tareas ordenadas por prioridad (menor primero)
    """
    print("\nTareas pendientes (ordenadas por prioridad):")
    # Ordenamiento simple tipo burbuja para no usar librerías
    ordenadas = tareas.copy()
    n = len(ordenadas)
    for i in range(n):
        for j in range(0, n-i-1):
            if ordenadas[j]["prioridad"] > ordenadas[j+1]["prioridad"]:
                ordenadas[j], ordenadas[j+1] = ordenadas[j+1], ordenadas[j]
    for t in ordenadas:
        print(f"- {t['descripcion']} (Prioridad: {t['prioridad']})")

def completar_tarea():
    """
    Completa la tarea de mayor prioridad (menor número)
    """
    if not tareas:
        print("No hay tareas pendientes.")
        return
    # Encontrar la tarea con menor prioridad
    min_idx = 0
    for i in range(1, len(tareas)):
        if tareas[i]["prioridad"] < tareas[min_idx]["prioridad"]:
            min_idx = i
    tarea = tareas.pop(min_idx)
    print(f"Tarea completada: {tarea['descripcion']}")

# =================================================
# EJEMPLO DE USO
# =================================================
agregar_tarea("Enviar informe", 2)
agregar_tarea("Llamar al cliente", 1)
agregar_tarea("Revisar correo", 3)

mostrar_tareas()
completar_tarea()
mostrar_tareas()
