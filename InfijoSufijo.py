def extraer_operadores(pila_operadores):
    operadores_extraidos = []
    while pila_operadores[-1] != '(':
        operador = pila_operadores.pop()
        operadores_extraidos.append(operador)
    pila_operadores.pop()  # Eliminar el paréntesis izquierdo correspondiente
    return operadores_extraidos

def extraer_operadores_hasta_izquierda(simbolo, pila_operadores, salida):
    if simbolo == ')':
        operadores_extraidos = extraer_operadores(pila_operadores)
        salida.extend(operadores_extraidos[::-1])  # Agregar los operadores extraídos al final de la lista de salida en orden inverso

def prioridad_operador(a):
    if a in '*/':
        return 3
    if a in '+-':
        return 2
    else:
        return 1


# Ejemplo de uso:
expresion = "A*B+C*D"
pila_operadores = []
salida = []

for simbolo in expresion:
    if simbolo in '()+-*/':
        if simbolo == '(':
            pila_operadores.append(simbolo)
        elif simbolo == ')':
            extraer_operadores_hasta_izquierda(simbolo, pila_operadores, salida)
        else:
            while (len(pila_operadores) != 0 and pila_operadores[-1] != '(' and prioridad_operador(pila_operadores[-1]) >= prioridad_operador(simbolo)):
                salida.append(pila_operadores.pop())
            pila_operadores.append(simbolo)
    else:
        salida.append(simbolo)

# Extraer los operadores restantes de la pila (si los hay)
while len(pila_operadores) != 0:
    salida.append(pila_operadores.pop())

print("Expresión de salida:", ''.join(salida))
