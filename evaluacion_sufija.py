def realizar_operacion(x, y, operador):
    if operador == '+':
        return x + y
    elif operador == '-':
        return x - y
    elif operador == '*':
        return x * y
    else:
        return x / y

expresion = "7 8 + 3 2 + /"
pila_operandos = []
numeros = '0123456789'
expresion = expresion.split()

for c in expresion:
    if c in numeros:
        c = int(c)
        pila_operandos.append(c)
    elif c in '+-/*':
        y, x = pila_operandos.pop(), pila_operandos.pop()  # Cambiado para usar pop()
        resultado = realizar_operacion(x, y, c)  # Pasar el operador 'c' en lugar de una lista con un elemento
        pila_operandos.append(resultado)

# El resultado debe ser el único elemento restante en la pila de operandos
resultado_final = pila_operandos[-1] if pila_operandos else None
print("Resultado:", resultado_final)
