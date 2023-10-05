valor_a_convertir = float(input("Valor a convertir: "))
tipo_de_moneda = input("En qué tipo de moneda quiere el cambio? ")
valor_de_cambio = float(input("Valor de cambio: "))
valor_convertido = valor_a_convertir * valor_de_cambio
print("En {} son: {}".format(tipo_de_moneda, valor_convertido))