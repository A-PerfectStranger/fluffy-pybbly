primer_numero = int(input("Introduce un numero: "))
segundo_numero = int(input("Introduce un segundo numero: "))
tercer_numero = int(input("Introduce un ultimo numero: "))
print("El numero mas grande es {}, y el mas pequeño {}".format(
    max(primer_numero, segundo_numero, tercer_numero),
          min(primer_numero, segundo_numero, tercer_numero)))