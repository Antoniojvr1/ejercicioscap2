class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def altura(arbol):
    # Caso base: si el árbol está vacío
    if arbol is None:
        return 0
    else:
        # Calcular la altura de los subárboles izquierdo y derecho
        altura_izquierda = altura(arbol.izquierda)
        altura_derecha = altura(arbol.derecha)

        # La altura es el máximo de las alturas de los subárboles más 1 (para el nodo actual)
        return max(altura_izquierda, altura_derecha) + 1

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

# Calcular la altura del árbol
print(altura(raiz))  # Salida: 3
