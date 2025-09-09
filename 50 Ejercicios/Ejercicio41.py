# =================================================
# SIMULADOR DE CAJERO AUTOMÁTICO (SIN CLASES)
# =================================================

# Función para crear una cuenta con saldo inicial
def crear_cuenta(saldo_inicial=1000):
    """Crea una cuenta representada como un diccionario"""
    return {"saldo": saldo_inicial}

# Función para consultar saldo
def consultar_saldo(cuenta):
    print(f"Saldo actual: ${cuenta['saldo']}")

# Función para retirar dinero
def retirar_dinero(cuenta, cantidad):
    if cantidad <= cuenta['saldo']:
        cuenta['saldo'] -= cantidad
        print(f"Retiro exitoso: ${cantidad}")
    else:
        print("Saldo insuficiente")

# Función para depositar dinero
def depositar_dinero(cuenta, cantidad):
    cuenta['saldo'] += cantidad
    print(f"Depósito exitoso: ${cantidad}")

# =================================================
# EJEMPLO DE USO
# =================================================
mi_cuenta = crear_cuenta()        # Crear cuenta con saldo por defecto
consultar_saldo(mi_cuenta)        # Consultar saldo
retirar_dinero(mi_cuenta, 200)    # Retirar dinero
depositar_dinero(mi_cuenta, 500)  # Depositar dinero
consultar_saldo(mi_cuenta)        # Consultar saldo actualizado
