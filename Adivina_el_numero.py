import random
numero_a_adivinar = random.randint(1, 10)
respuesta_jugador = int(input("Adivina, adivinador. En qué numero estoy pensando yo?  -> "))
if numero_a_adivinar == respuesta_jugador:
    print("Felicidades!! Tienes talento de adivino")
if numero_a_adivinar != respuesta_jugador:
    print("Numero equivocado, lo siento :(")
print("Numero ganador: {}".format(numero_a_adivinar))
print("Gracias por jugar")