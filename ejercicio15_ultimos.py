class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(elemento)

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            print("La cola está vacía. No se puede realizar 'dequeue'.")
            return None

    def peek(self):
        """Devuelve el primer elemento de la cola sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[0]
        else:
            print("La cola está vacía. No se puede realizar 'peek'.")
            return None

    def esta_vacia(self):
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return len(self.elementos) == 0

    def mostrar(self):
        """Muestra los elementos de la cola."""
        print("Contenido de la cola:", self.elementos)


def ordenar_cola(cola):
    cola_ordenada = Cola()

    while not cola.esta_vacia():
        # Extraer el mínimo de la cola
        minimo = float('inf')
        for _ in range(len(cola.elementos)):
            elemento = cola.dequeue()
            if elemento < minimo:
                minimo = elemento
            cola_ordenada.enqueue(elemento)

        # Mover los elementos no mínimos de vuelta a la cola
        while not cola_ordenada.esta_vacia():
            elemento = cola_ordenada.dequeue()
            if elemento != minimo:
                cola.enqueue(elemento)
        
        # Agregar el mínimo a la cola ordenada
        cola.enqueue(minimo)

    return cola


# Ejemplo de uso
mi_cola = Cola()
mi_cola.enqueue(3)
mi_cola.enqueue(1)
mi_cola.enqueue(4)
mi_cola.enqueue(1)
mi_cola.enqueue(5)
mi_cola.enqueue(9)

print("Cola original:")
mi_cola.mostrar()

mi_cola = ordenar_cola(mi_cola)

print("Cola ordenada:")
mi_cola.mostrar()
