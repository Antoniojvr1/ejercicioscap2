from simplestack import Stack
  # Asegúrate de que Stack está en SimpleStack.py

def es_palindromo(cadena):
    # Filtrar la cadena: ignorar espacios, dígitos, puntuación y pasar a minúsculas
    cadena_filtrada = ''.join([letra.lower() for letra in cadena if letra.isalpha()])

    # Crear una pila
    stack = Stack(len(cadena_filtrada) // 2)

    # Insertar la primera mitad de las letras en la pila
    for i in range(len(cadena_filtrada) // 2):
        stack.push(cadena_filtrada[i])

    # Determinar el punto de inicio de la comparación para la segunda mitad
    inicio_segunda_mitad = len(cadena_filtrada) // 2
    if len(cadena_filtrada) % 2 != 0:
        inicio_segunda_mitad += 1  # Saltar el carácter del medio si la longitud es impar

    # Comparar la segunda mitad de la cadena con el contenido de la pila
    es_palindromo = True
    for i in range(inicio_segunda_mitad, len(cadena_filtrada)):
        if stack.pop() != cadena_filtrada[i]:
            es_palindromo = False
            break

    return es_palindromo

# Programa de prueba
cadena_prueba =  "A man, a plan, a canal, Panama"
if es_palindromo(cadena_prueba):
    print(f'"{cadena_prueba}" es un palindromo.')
else:
    print(f'"{cadena_prueba}" no es un palindromo.')



def test_stack():
    stack = Stack(5)  # Crear una pila con un tamaño máximo de 5

    print("Apilando elementos:")
    for i in range(5):
        stack.push(i)
        print(f"Pushed: {i}, Stack: {stack}")

    try:
        print("Intentando apilar un elemento mas: ")
        stack.push(5)  # Esto debería lanzar una excepción
    except Exception as e:
        print(e)

    print("\nDesapilando elementos:")
    while not stack.isEmpty():  # Usar isEmpty() en lugar de is_empty()
        popped_item = stack.pop()
        print(f"Popped: {popped_item}, Stack: {stack}")

    try:
        print("Intentando desapilar de una pila vacia: ")
        stack.pop()  # Esto debería lanzar una excepción
    except Exception as e:
        print(e)

if __name__ == "__main__":
    test_stack()

