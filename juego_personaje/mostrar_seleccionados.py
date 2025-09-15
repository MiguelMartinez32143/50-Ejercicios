from datos import personaje, objetos, historial
# Función para mostrar los objetos seleccionados y el historial
def mostrar_seleccionados():
    print("\n--- Personaje actual ---")
    print(f"Nombre: {personaje['nombre']}")
    print(f"Arma actual: {personaje['arma']} -> {objetos['armas'].get(personaje['arma'], {})}")
    print(f"Armadura actual: {personaje['armadura']} -> {objetos['armaduras'].get(personaje['armadura'], {})}")
    print(f"Accesorio actual: {personaje['accesorio']} -> {objetos['accesorios'].get(personaje['accesorio'], {})}")
# Mostrar historial de selecciones de toda la ejecucion
    print("\n--- Historial de selecciones durante la ejecución ---")
    armas_hist = ", ".join(historial["armas"]) if historial["armas"] else "—"
    armaduras_hist = ", ".join(historial["armaduras"]) if historial["armaduras"] else "—"
    accesorios_hist = ", ".join(historial["accesorios"]) if historial["accesorios"] else "—"
    print(f"Armas elegidas: {armas_hist}")
    print(f"Armaduras elegidas: {armaduras_hist}")
    print(f"Accesorios elegidos: {accesorios_hist}")
