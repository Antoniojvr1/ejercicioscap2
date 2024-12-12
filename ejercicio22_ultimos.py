from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def recorrido_por_niveles(raiz):
    if raiz is None:
        return []
    
    # Usamos una cola (deque) para realizar el recorrido por niveles
    cola = deque([raiz])
    resultado = []  # Lista para almacenar los valores de los nodos

    while cola:
        # Extraemos el primer nodo de la cola
        nodo_actual = cola.popleft()
        
        # Agregamos el valor del nodo actual a la lista de resultados
        resultado.append(nodo_actual.valor)
        
        # Si tiene hijo izquierdo, lo agregamos a la cola
        if nodo_actual.izquierda:
            cola.append(nodo_actual.izquierda)
        
        # Si tiene hijo derecho, lo agregamos a la cola
        if nodo_actual.derecha:
            cola.append(nodo_actual.derecha)
    
    return resultado

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

# Imprimir el mensaje y la salida del recorrido por niveles
print("La salida es:", *recorrido_por_niveles(raiz))
