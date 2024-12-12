class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_duplicates(self):
        if not self.head:
            return

        current = self.head
        seen_values = set()  # Usamos un conjunto para rastrear valores ya vistos
        seen_values.add(current.value)

        while current.next:
            if current.next.value in seen_values:
                # Eliminar el nodo duplicado
                current.next = current.next.next
            else:
                seen_values.add(current.next.value)
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(10)
linked_list.append(30)
linked_list.append(20)

print("Lista antes de eliminar duplicados:")
linked_list.display()

linked_list.remove_duplicates()

print("Lista despues de eliminar duplicados:")
linked_list.display()
