titulo = "Pon a prueba tu afinidad por el queso"
print("\n\t\t" + titulo + "\n\t\t" + "-" * len(titulo))
puntuacion = 0
opcion = input("""
        Pregunta 1: ¿Qué haces cuando ves una tabla de quesos?
        A.- Salgo corriendo
        B.- Pruebo uno de los quesos o varios
        C.- No puedo evitar devorarla
""")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Debes elegir entre A, B y C")
    exit("Lo siento")

opcion = input("""
        Pregunta 2: ¿Cómo te gusta la hamburguesa?
        A.- Sin queso
        B.- Con queso
        C.- Doble queso
""")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Debes elegir entre A, B y C")
    exit("Lo siento")

opcion = input("""
        Pregunta 3: ¿Eres intolerante a la lactosa?
        A.- Si
        B.- Emveces
        C.- No 
""")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Debes elegir entre A, B y C")
    exit("Lo siento")

if puntuacion >= 25:
    print("Eres un entusiasta del queso")
elif puntuacion >= 15:
    print("Eres un queso-casual")
else:
    print("El queso y tú NO son almas gemelas")


