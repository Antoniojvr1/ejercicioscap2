class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print(" -> ".join(map(str, elementos)))

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente  # Almacenar la referencia al siguiente nodo
            actual.siguiente = anterior   # Invertir la dirección del enlace
            anterior = actual             # Mover `anterior` al nodo actual
            actual = siguiente            # Mover `actual` al siguiente nodo
        self.cabeza = anterior            # Actualizar la cabeza de la lista

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

print("Lista original:")
lista.mostrar()

lista.invertir()

print("Lista invertida:")
lista.mostrar()