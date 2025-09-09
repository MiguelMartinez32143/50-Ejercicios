# Programa que clasifica la nota de un estudiante

# Se pide la nota al usuario
nota = float(input("Ingresa tu calificación: "))

# Diccionario que asocia clasificaciones y mensajes
if nota >= 9.0:
    clasificacion, mensaje = ("Excelente", "¡Felicidades! Sigue así")
elif nota >= 7.0:
    clasificacion, mensaje = ("Buena", "Buen trabajo, puedes mejorar")
else:
    clasificacion, mensaje = ("Necesita mejorar", "Estudia más para la próxima")

# Se muestran los resultados
print(f"Tu nota es: {nota}")
print(f"Clasificación: {clasificacion}")
print(f"Comentario: {mensaje}")
