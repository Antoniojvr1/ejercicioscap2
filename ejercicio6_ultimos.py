class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            print("La pila esta vacia. No se puede realizar 'pop'.")
            return None

    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            print("La pila esta vacia. No se puede realizar 'peek'.")
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        print("Contenido de la pila: ", self.elementos)

mi_pila = Pila()


mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)
print("Despues de agregar elementos: ")
mi_pila.mostrar()

cima = mi_pila.peek()
print(f"Elemento en la cima: {cima}")

print("Quitando elementos de la pila: ")
print(f"Elemento eliminado: {mi_pila.pop()}")
print(f"Elemento eliminado: {mi_pila.pop()}")
print(f"Elemento eliminado: {mi_pila.pop()}")
print(f"Elemento eliminado: {mi_pila.pop()}")  # Intento con pila vacía

mi_pila.mostrar()
