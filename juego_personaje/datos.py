personaje = {
    "nombre": "Héroe",
    "arma": None,
    "armadura": None,
    "accesorio": None
}
# Definición de los objetos disponibles
objetos = {
    "armas": {
        "espada": {"ataque": 3},
        "arco": {"ataque": 3},
        "hacha": {"ataque": 3},
        "daga": {"ataque": 3},
        "lanza": {"ataque": 3}
    },
    "armaduras": {
        "cuero": {"defensa": 3},
        "hierro": {"defensa": 6},
        "acero": {"defensa": 6},
        "escamas": {"defensa": 3},
        "tela mágica": {"defensa": 6}
    },
    "accesorios": {
        "anillo": {"magia": 3},
        "collar": {"magia": 5},
        "amuletos": {"magia": 7},
        "pulsera": {"magia": 4},
        "capa encantada": {"magia": 10}
    }
}

# Historial de selecciones durante la ejecución
historial = {
    "armas": [],
    "armaduras": [],
    "accesorios": []
}
# Barras de vida para el combate

vidas = {
    "barra1": True,
    "barra2": True,
    "barra3": True,
    "barra4": True,
    "barra5": True,
    "barra6": True
}

enemigos = {
    "enemigo1": {"nombre": "Goblin", "ataque": 1, "vida": 12},
    "enemigo2": {"nombre": "Goblin Gigante", "ataque": 2, "vida": 21},
    "enemigo3": {"nombre": "Troll", "ataque": 1, "vida": 12},
    "enemigo4": {"nombre": "Troll Gigante", "ataque": 2, "vida": 21}
}