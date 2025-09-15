from datos import objetos

def personalizar_objetos():
    print("\n--- Modificar objetos existentes ---")
    categoria = input("¿Qué deseas modificar? (armas/armaduras/accesorios): ")
    if categoria not in objetos:
        print("❌ Categoría no válida")
        return
# Mostrar objetos en la categoría
    print(f"Objetos en {categoria}:")
    for obj in objetos[categoria]:
        print(f"- {obj}")
# Solicitar objeto a modificar
    eleccion = input("¿Cuál deseas modificar?: ")
    if eleccion not in objetos[categoria]:
        print("❌ Objeto no encontrado")
        return
# Modificar atributos del objeto
    print(f"Atributos actuales: {objetos[categoria][eleccion]}")
    for stat in objetos[categoria][eleccion]:
        nuevo_valor = input(f"Nuevo valor para {stat} (deja vacío para no cambiar): ")
        if nuevo_valor.strip() != "":
            objetos[categoria][eleccion][stat] = int(nuevo_valor)

    print("✅ Objeto modificado con éxito!\n")
