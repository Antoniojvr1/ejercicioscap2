def calcular(expresion):
    pila = []
    operadores = { '+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for token in expresion:
        if token in operadores:
            if len(pila) < 2:
                raise ValueError("Expresión inválida: no hay suficientes operandos")
            operando2 = pila.pop()
            operando1 = pila.pop()
            resultado = operadores[token](operando1, operando2)
            pila.append(resultado)
        else:
            try:
                pila.append(float(token))
            except ValueError:
                raise ValueError("Expresión inválida: token no válido")

    if len(pila) != 1:
        raise ValueError("Expresión inválida: pila no vacía al final")

    return pila.pop()

# Ejemplo de uso:
expresion = [3, 4, '*']  # Corregido el orden de los elementos
try:
    resultado = calcular(expresion)
    print("El resultado es:", resultado)
except ValueError as e:
    print("Error:", e)