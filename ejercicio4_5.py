def identity(x):
    return x  # Función de identidad para obtener la prioridad directamente

class PriorityQueue:
    def __init__(self, size, pri=identity):
        self.__maxSize = size
        self.__que = [None] * size  # Arreglo para almacenar la cola
        self.__pri = pri  # Función para determinar la prioridad
        self.__nItems = 0  # Número de elementos en la cola

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        # Inserta directamente en la siguiente posición disponible
        self.__que[self.__nItems] = item
        self.__nItems += 1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        
        # Encontrar el índice del elemento de mayor prioridad
        max_index = 0
        for i in range(1, self.__nItems):
            if self.__pri(self.__que[i]) > self.__pri(self.__que[max_index]):
                max_index = i
        
        # Guardar el elemento de mayor prioridad
        max_item = self.__que[max_index]
        
        # Mover elementos para llenar el espacio dejado por el elemento eliminado
        for j in range(max_index, self.__nItems - 1):
            self.__que[j] = self.__que[j + 1]
        
        # Eliminar referencia y reducir el número de elementos
        self.__que[self.__nItems - 1] = None
        self.__nItems -= 1
        return max_item

    def peek(self):
        if self.isEmpty():
            return None
        max_index = 0
        for i in range(1, self.__nItems):
            if self.__pri(self.__que[i]) > self.__pri(self.__que[max_index]):
                max_index = i
        return self.__que[max_index]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def __len__(self):
        return self.__nItems

    def __str__(self):
        ans = "["  # Comienza con el corchete izquierdo
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__que[i])
        ans += "]"  # Cierra con el corchete derecho
        return ans

def test_priority_queue():
    print("Creando una cola de prioridad con tamaño máximo de 5...")
    pq = PriorityQueue(5)
    
    print("Insertando elementos en la cola de prioridad (orden de prioridad aleatorio):")
    pq.insert(30)
    pq.insert(10)
    pq.insert(40)
    pq.insert(20)
    pq.insert(50)
    
    print("Contenido de la cola de prioridad después de las inserciones:")
    print(pq)

    print("\nEliminando elementos en orden de mayor prioridad:")
    while not pq.isEmpty():
        print(f"Elemento de mayor prioridad eliminado: {pq.remove()}")
        print("Contenido de la cola de prioridad:")
        print(pq)

# Ejecuta la prueba
if __name__ == "__main__":
    test_priority_queue()
