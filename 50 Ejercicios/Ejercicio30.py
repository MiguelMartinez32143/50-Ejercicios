# -----------------------------------------------------------
# SISTEMA DE RECOMENDACIONES (VERSIÓN REESTRUCTURADA RADICAL)
# -----------------------------------------------------------

def medir_similitud(datos_a, datos_b):
    """
    Calcula qué tan parecidos son dos usuarios.
    Devuelve un valor entre 0 y 1.
    """
    total = 0
    coincidencias = 0
    claves = list(datos_a.keys())
    i = 0

    while i < len(claves):
        clave = claves[i]
        if clave in datos_b:
            total += 1
            coincidencias += int(datos_a[clave] == datos_b[clave])
        i += 1

    return round(coincidencias / total, 2) if total > 0 else 0


def buscar_similares(usuario_ref, base, umbral_sim=0.6):
    """
    Devuelve una lista de usuarios similares al usuario de referencia.
    """
    resultados = []
    print(f"\nBuscando usuarios similares a '{usuario_ref}' con umbral {umbral_sim}")
    print("-" * 50)

    datos_ref = base[usuario_ref]
    nombres = list(base.keys())
    idx = 0

    while idx < len(nombres):
        nombre_actual = nombres[idx]
        if nombre_actual != usuario_ref:
            simil = medir_similitud(datos_ref, base[nombre_actual])
            print(f"{nombre_actual}: similitud {simil}")
            if simil >= umbral_sim:
                resultados.append((nombre_actual, simil))
        idx += 1

    # Ordenar de mayor a menor similitud
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados


def generar_sugerencias(usuario_ref, similares, base):
    """
    Genera recomendaciones de contenido basadas en los usuarios similares.
    """
    sugerencias = {}
    gustos_ref = base[usuario_ref]
    idx_sim = 0

    print(f"\nGenerando sugerencias para '{usuario_ref}':")

    while idx_sim < len(similares):
        usuario_sim, simil = similares[idx_sim]
        gustos_sim = base[usuario_sim]

        for categoria, valor in gustos_sim.items():
            if valor and categoria not in gustos_ref:
                if categoria not in sugerencias:
                    sugerencias[categoria] = []
                sugerencias[categoria].append((usuario_sim, simil))
                print(f"  + Recomendar '{categoria}' (le gusta a {usuario_sim})")
        idx_sim += 1

    return sugerencias


# -------------------------------
# BASE DE DATOS DE USUARIOS
# -------------------------------
usuarios_db = {
    "Ana": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": True},
    "Carlos": {"acción": True, "comedia": False, "drama": True, "terror": False, "ciencia_ficción": True},
    "María": {"acción": False, "comedia": True, "drama": True, "terror": True, "ciencia_ficción": False},
    "Pedro": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": False},
    "Laura": {"acción": False, "comedia": True, "drama": True, "terror": False, "ciencia_ficción": True}
}

# -------------------------------
# EJECUCIÓN PRINCIPAL
# -------------------------------
if __name__ == "__main__":
    print("SISTEMA DE RECOMENDACIONES")
    print("=" * 40)

    print("\nUsuarios registrados:")
    for nombre, gustos in usuarios_db.items():
        print(f"{nombre}: {gustos}")

    usuario_obj = "Ana"

    # 1️ Buscar usuarios similares
    similares = buscar_similares(usuario_obj, usuarios_db, umbral_sim=0.4)
    print(f"\nUsuarios similares a {usuario_obj}:")
    idx = 0
    while idx < len(similares):
        nombre, simil = similares[idx]
        print(f"  - {nombre}: {simil*100:.0f}% similar")
        idx += 1

    # 2️ Generar recomendaciones
    recomendaciones = generar_sugerencias(usuario_obj, similares, usuarios_db)

    print("\n" + "=" * 30)
    print("RECOMENDACIONES FINALES")
    print("=" * 30)

    if recomendaciones:
        for categoria, lista in recomendaciones.items():
            print(f"\nCategoría: {categoria}")
            for u, sim in lista:
                print(f"  * Sugerido por {u} (similitud: {sim})")
    else:
        print("No hay recomendaciones disponibles.")
