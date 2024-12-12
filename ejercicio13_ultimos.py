class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.frente = self.final = -1

    def esta_vacia(self):
        return self.frente == -1

    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def encolar(self, item):
        if self.esta_llena():
            print("La cola está llena")
            return
        if self.frente == -1:
            self.frente = 0
        self.final = (self.final + 1) % self.capacidad
        self.items[self.final] = item

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return
        item = self.items[self.frente]
        if self.frente == self.final:
            self.frente = self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad
        return item

cola = ColaCircular(5)
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.desencolar())  # Imprime: 1
print(cola.desencolar())  # Imprime: 2
cola.encolar(4)
cola.encolar(5)
cola.encolar(6)  # La cola está llena, no se agrega