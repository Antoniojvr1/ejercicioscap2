class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_hojas(raiz):
    # Caso base: Si el árbol está vacío, no hay hojas
    if raiz is None:
        return 0
    
    # Si el nodo es una hoja (no tiene hijos), contamos 1
    if raiz.izquierda is None and raiz.derecha is None:
        return 1
    
    # Si el nodo tiene hijos, contamos las hojas en los subárboles izquierdo y derecho
    return contar_hojas(raiz.izquierda) + contar_hojas(raiz.derecha)

raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

# Contar las hojas del árbol
print("Numero de hojas:", contar_hojas(raiz))  # Salida: 3
