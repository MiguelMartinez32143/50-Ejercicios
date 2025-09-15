from personalizar_personaje import personalizar_personaje
from mostrar_objetos import mostrar_objetos
from personalizar_objetos import personalizar_objetos
from mostrar_seleccionados import mostrar_seleccionados
from combatir_enemigos import combatir_enemigos  # <-- Importa tu función de combate

# Función principal con menú
def main():
    while True:
        print("\n====== Menú Principal ======")
        print("1. Personalizar personaje")
        print("2. Mostrar todos los objetos")
        print("3. Personalizar objetos")
        print("4. Mostrar objetos seleccionados")
        print("5. Combatir enemigos")      # <-- Nueva opción de combate
        print("6. Salir")
        opcion = input("Elige una opción: ")

        # Lógica del menú
        if opcion == "1":
            personalizar_personaje()  # Personalizar el personaje
        elif opcion == "2":
            mostrar_objetos()  # Mostrar todos los objetos disponibles
        elif opcion == "3":
            personalizar_objetos()  # Personalizar los objetos del personaje
        elif opcion == "4":
            mostrar_seleccionados()  # Mostrar los objetos seleccionados
        elif opcion == "5":
            # Aquí entramos al combate
            print("\n--- ¡Comienza el combate! ---\n")
            combatir_enemigos()       # <-- Llamada a la función de combate
        elif opcion == "6":
            print(" Saliendo del juego...")
            break
        else:
            print(" Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
