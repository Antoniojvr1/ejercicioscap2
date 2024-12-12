def es_balanceada(cadena):
    pila = []
    parentesis_abiertos = {'(', '{', '['}
    parentesis_cerrados = {')', '}', ']'}
    parejas = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in parentesis_abiertos:
            pila.append(caracter)
        elif caracter in parentesis_cerrados:
            if not pila or pila.pop() != parejas[caracter]:
                return False

    return len(pila) == 0

print(es_balanceada("()"))  
print(es_balanceada("(){}[]"))  
print(es_balanceada("([)]"))  
print(es_balanceada("{[()]}"))  

cadena = "{[()]}("
if es_balanceada(cadena):
    print("la cadena es: ", cadena)
    print("La cadena esta balanceada")
else:
    print("la cadena es: ", cadena)
    print("La cadena no esta balanceada")