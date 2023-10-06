import time
import os
import random
respuesta_adivino = input("UNA VOZ DESCONOCIDA: ¿Estás lista? ")
if not respuesta_adivino == "si":
    exit("UNA VOZ DESCONOCIDA: Tal vez era muy pronto")
print("UNA VOZ DESCONOCIDA: Ya veo, seguramente nos encontremos en un futuro")
time.sleep(1.4)
os.system("cls")
print("""
Te despiertas en un lecho muy cómodo, no recuerdas nada de la noche anterior ni de tu vida hasta ese momento
¿Qué haces?
1: Investigar la habitación
2: Buscar pistas personales
3: Salir de la habitación
""")
respuesta = int(input("->"))
tener_foto = False
numero_a_multiplicar = random.randint(1, 10)
clave_caja_fuerte = 13 * numero_a_multiplicar
if respuesta == 1:
    print("""
          Decides investigar la habitación en busca de pistas sobre tu identidad. 
          Observas cuidadosamente los detalles: una ventana con cortinas cerradas, una mesita de noche con un reloj antiguo, y un armario. 
          ¿Qué haces a continuación?
          1. Examinar la ventana con cortinas cerradas.
          2. Observar el reloj antiguo en la mesita de noche.
          3. Abrir el armario.
          """)
    respuesta = int(input("->"))
    if respuesta == 1:
        print("""
        Decides examinar la ventana con cortinas cerradas. 
        Al abrir las cortinas, descubres que estás en lo alto de una torre con vistas a un bosque terrorífico. 
        Esto confirma que estás en un lugar extraño, pero no proporciona información sobre tu identidad.
        """)
    elif respuesta == 2:
        print("""
        Observas el reloj antiguo en la mesita de noche y encuentras una nota detrás de él. 
        En ella, está escrita una dirección y un nombre que no reconoces. 
        Parece una pista prometedora.
        """)
    elif respuesta == 3:
        print("""
        Decides abrir el armario. 
        Encuentras una maleta con ropa que te parece familiar, lo que sugiere que has estado en este lugar antes.
        También encuentras una caja con un candado muy pesado.
        """)
        respuesta = input("Quieres abrir la caja? ")
        if not respuesta.lower() == "si":
            exit("Tal vez había algo importante ahí")
        else:
            print("""
            Al parecer la clave es la respuesta de una operacion matematica
            ¿Cuánto es 13 por {} 
            """.format(numero_a_multiplicar))
            respuesta = int(input("= "))
            if respuesta == clave_caja_fuerte:
                print("""
                Abres la caja fuerte.
                Está vacía.
                """)
elif respuesta == 2:
    print("""
    Decides buscar en tus bolsillos o en la habitación alguna pista sobre tu identidad. 
    Encuentras una cartera en la mesita de noche con un tipo de identificación que muestra lo que podría ser tu nombre. 
    ¿Quieres investigar más sobre esta información?
    """)
    respuesta = input("->")
    if not respuesta == "si":
        exit("Alguien te golpea por la espalda, parece que es tu fin")
    print("""
            Revisas la identificación en la cartera y descubres que te llamas Sarah y que vives en una ciudad que no te suena familiar. 
            Aún te sientes perdida.
            Además del papel, encuentras algunas dibujos y una fotografía de una persona que parece ser un amigo o familiar. 
            La foto tiene una fecha escrita en el reverso, pero no puedes recordar quién es la persona ni por qué tenías esta foto.
            """)
    respuesta = input("Quieres guardar la foto? ")
    if not respuesta.lower() == "si":
        print("Dejas la foto en la mesita de noche")
    else:
        print("Vuelves a guardar la foto en tu bolsillo")
        tener_foto = True

elif respuesta == 3:
    print("""
    Optas por salir de la habitación en busca de respuestas. 
    Abres la puerta y entras en un pasillo desconocido. A tu izquierda, ves una escalera que desciende. 
    A tu derecha, una puerta cerrada. 
    """)
