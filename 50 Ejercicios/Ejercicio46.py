# =================================================
# AGENDA DE CONTACTOS (SIN CLASES)
# =================================================

# Lista global de contactos (cada contacto es un diccionario)
contactos = []

def agregar_contacto(nombre, telefono, email):
    """Agrega un contacto a la agenda"""
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print(f"Contacto '{nombre}' agregado.")

def buscar_contacto(nombre_buscar):
    """Busca contactos que contengan el nombre indicado"""
    resultados = []
    for c in contactos:
        if nombre_buscar.lower() in c["nombre"].lower():
            resultados.append(c)
    if resultados:
        print(f"Se encontraron {len(resultados)} contacto(s):")
        for c in resultados:
            print(f" - {c['nombre']}: {c['telefono']}, {c['email']}")
    else:
        print("No se encontró ningún contacto.")
    return resultados

# =================================================
# EJEMPLO DE USO
# =================================================
agregar_contacto("Ana López", "123456789", "ana@mail.com")
agregar_contacto("Carlos Pérez", "987654321", "carlos@mail.com")
agregar_contacto("María González", "555666777", "maria@mail.com")

print("\nBuscando 'ana':")
buscar_contacto("ana")

print("\nBuscando 'perez':")
buscar_contacto("perez")
