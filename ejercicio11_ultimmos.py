class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)

    def ver_primero(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.items[0]

mi_cola = Cola()
mi_cola.encolar(10)
mi_cola.encolar(5)
mi_cola.encolar(3)

print(mi_cola.ver_primero())  # Imprime: 10
print(mi_cola.desencolar())   # Imprime: 10
print(mi_cola.esta_vacia())   # Imprime: False