from datos import personaje, objetos, historial
# Función para personalizar el personaje
def personalizar_personaje():
    print("\n--- Personalizar Personaje ---")
# Elegir arma
    print("Elige un arma:")
    armas = list(objetos["armas"].keys())
    for i, arma in enumerate(armas, 1):
        print(f"{i}. {arma}")
    eleccion = input("Número de arma: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(armas):
        personaje["arma"] = armas[int(eleccion)-1]
        historial["armas"].append(personaje["arma"])
# Continuar con armaduras y accesorios
    print("\nElige una armadura:")
    armaduras = list(objetos["armaduras"].keys())
    for i, armadura in enumerate(armaduras, 1):
        print(f"{i}. {armadura}")
    eleccion = input("Número de armadura: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(armaduras):
        personaje["armadura"] = armaduras[int(eleccion)-1]
        historial["armaduras"].append(personaje["armadura"])

    print("\nElige un accesorio:")
    accesorios = list(objetos["accesorios"].keys())
    for i, acc in enumerate(accesorios, 1):
        print(f"{i}. {acc}")
    eleccion = input("Número de accesorio: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(accesorios):
        personaje["accesorio"] = accesorios[int(eleccion)-1]
        historial["accesorios"].append(personaje["accesorio"])

    print("\n✅ Personalización completa!\n")
