class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            return None  # O puedes lanzar una excepción
        return self.items.pop(0)

    def ver_primero(self):
        if self.esta_vacia():
            return None  # O puedes lanzar una excepción
        return self.items[0]

def reorganizar_cola(cola):
    pares = Cola()
    impares = Cola()

    while not cola.esta_vacia():
        elemento = cola.desencolar()
        if elemento % 2 == 0:
            pares.encolar(elemento)
        else:
            impares.encolar(elemento)

    while not pares.esta_vacia():
        cola.encolar(pares.desencolar())

    while not impares.esta_vacia():
        cola.encolar(impares.desencolar())

# Ejemplo de uso:
cola = Cola()
cola.encolar(3)
cola.encolar(2)
cola.encolar(5)
cola.encolar(4)
cola.encolar(1)
cola.encolar(8)
cola.encolar(6)
cola.encolar(7)
cola.encolar(9)
cola.encolar(10)

reorganizar_cola(cola)

# Imprimir la cola reorganizada (para verificar)
while not cola.esta_vacia():
    print(cola.desencolar())