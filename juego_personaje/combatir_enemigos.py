from datos import vidas, enemigos, personaje, objetos

def mostrar_vidas():
    """Muestra cuántas vidas quedan y dibuja las barras."""
    total = 0
    barras = ""
    for estado in vidas.values():
        if estado:
            total += 1
            barras += "❤️ "
        else:
            barras += "🖤 "
    print(f"Tienes {total} vidas")
    print(barras)
# combatit_enemigos.py
def combatir_enemigos():
    """
    Esqueleto básico para combatir contra los enemigos.
    Disminuye vida de enemigo y del personaje mientras ambos estén vivos.
    """
    # Recorremos cada enemigo del diccionario
    for enemigo in enemigos.values():
        print(f"\n¡Comienza el combate contra {enemigo['nombre']}!")
        print(f"Ataque del enemigo: {enemigo['ataque']}, Vida del enemigo: {enemigo['vida']}")

        # Mientras queden vidas y el enemigo siga vivo
        while any(vidas.values()) and enemigo["vida"] > 0:
            # Aquí va la lógica de ataque del personaje
            # (En este esqueleto solo restamos valores fijos para probar)
            enemigo["vida"] -= 3  # daño del personaje (ejemplo)
            print(f"Le has hecho 3 de daño. Vida restante del enemigo: {enemigo['vida']}")

            # Ahora el enemigo te ataca
            quitar_vida(vidas)  # le quita una barra de vida al personaje
            mostrar_vidas()     # mostramos las vidas restantes

            # Rompemos si ya no quedan vidas
            if not any(vidas.values()):
                print("Has perdido todas tus vidas. ¡Fin del juego!")
                return

        if enemigo["vida"] <= 0:
            print(f"Has derrotado a {enemigo['nombre']}")

def quitar_vida(vidas):
    """
    Quita la primera barra de vida True y la convierte en False.
    Esto simula que el enemigo te hace daño.
    """
    for barra in vidas:
        if vidas[barra]:
            vidas[barra] = False
            break
