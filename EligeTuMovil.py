tipo_de_sistema = input("¿Qué tipo de sistema operativo quieres? ")
tiene_dinero = input("¿Tienes dinero? ")
if tipo_de_sistema == "android":
    if not tiene_dinero == "si":
        print("Deberias elegir un Android chino")
    else:
        importa_la_camara = input("Te importa la camara del movil? ")
        if importa_la_camara == "si":
            print("Deberias elegir un Google Pixel Supercamara")
        else:
            print("Lo mejor para ti, sería un Android calidad-precio")

elif tipo_de_sistema == "ios":
    if not tiene_dinero == "si":
        print("Puedes adquirir un iPhone de segunda mano")
    else:
        print("Lo tuyo es un iPhone Ultra Pro Max")
