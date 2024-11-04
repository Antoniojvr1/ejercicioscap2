#listado 4-1

class Stack(object):
    def __init__(self, max):  # Constructor
        self.__stackList = [None] * max  # La pila se almacena en una lista
        self.__top = -1  # Sin elementos inicialmente
    
    def push(self, item):  # Insertar un elemento en la pila
        if self.isFull():
            raise Exception("Error: La pila esta llena. No se puede insertar.")
        self.__top += 1  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento
    
    def pop(self):  # Eliminar el elemento superior de la pila
        if self.isEmpty():
            raise Exception("Error: La pila esta vacia. No se puede extraer.")
        top = self.__stackList[self.__top]  # Obtener el elemento superior
        self.__stackList[self.__top] = None  # Eliminar la referencia al elemento
        self.__top -= 1  # Reducir el puntero
        return top  # Devolver el elemento superior
    
    def peek(self):  # Obtener el elemento superior sin eliminarlo
        if not self.isEmpty():
            return self.__stackList[self.__top]
    
    def isEmpty(self):  # Verificar si la pila está vacía
        return self.__top < 0
    
    def isFull(self):  # Verificar si la pila está llena
        return self.__top >= len(self.__stackList) - 1
    
    def __len__(self):  # Devolver la cantidad de elementos en la pila
        return self.__top + 1
    
    def __str__(self):  # Convertir la pila en una cadena
        ans = "["
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__stackList[i])
        ans += "]"
        return ans


# luego se hace el programa de prueba 

def test_stack():
    stack_size = 3
    stack = Stack(stack_size)
    
    # Intentamos llenar la pila
    try:
        print("Insertando elementos en la pila:")
        for i in range(stack_size):
            stack.push(i)
            print(f"Pila despues de push({i}): {stack}")
        
        # Intentamos insertar un elemento adicional
        print("Intentando insertar un elemento adicional...")
        stack.push(99)  # Esto debe lanzar una excepción
    except Exception as e:
        print(e)

    # Intentamos vaciar la pila
    try:
        print("\nExtrayendo elementos de la pila:")
        while not stack.isEmpty():
            item = stack.pop()
            print(f"Pila despues de pop(): {stack}")
        
        # Intentamos extraer un elemento de una pila vacía
        print("Intentando extraer de una pila vacia...")
        stack.pop()  # Esto debe lanzar una excepción
    except Exception as e:
        print(e)

# Llamar a la prueba
test_stack()


from pila_palindromo import *
stack = Stack(100) # Create a stack to hold letters

word = input("Word to reverse: ")
for letter in word: # Loop over letters in word
    if not stack.isFull(): # Push letters on stack if not full
        stack.push(letter)
        reverse = '' # Build the reversed version
while not stack.isEmpty(): # by popping the stack until empty
    reverse += stack.pop()
    print('The reverse of', word, 'is', reverse)