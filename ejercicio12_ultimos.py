import random

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

class Cliente:
    def __init__(self, numero):
        self.numero = numero
        self.tiempo_espera = 0

    def __str__(self):
        return f"Cliente {self.numero}"

class Banco:
    def __init__(self):
        self.cola_espera = Cola()

    def agregar_cliente(self, cliente):
        self.cola_espera.encolar(cliente)
        print(f"Cliente {cliente.numero} agregado a la cola.")

    def atender_siguiente_cliente(self):
        if self.cola_espera.esta_vacia():
            print("No hay clientes esperando.")
            return
        cliente = self.cola_espera.desencolar()
        tiempo_atencion = random.randint(1, 5)  # Tiempo de atención aleatorio
        cliente.tiempo_espera += tiempo_atencion
        print(f"Atendiendo a {cliente} (tiempo de espera: {cliente.tiempo_espera} minutos)")

# Crear una instancia del banco
banco = Banco()

# Agregar clientes a la cola
banco.agregar_cliente(Cliente(1))
banco.agregar_cliente(Cliente(2))
banco.agregar_cliente(Cliente(3))

# Atender a los clientes
banco.atender_siguiente_cliente()
banco.atender_siguiente_cliente()