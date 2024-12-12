class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nodo al final de la lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        """Convierte la lista enlazada a una lista Python."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Fusiona dos listas enlazadas ordenadas en una nueva lista enlazada ordenada."""
        dummy = Node(0)  # Nodo ficticio
        current = dummy
        
        p1 = list1.head
        p2 = list2.head

        while p1 and p2:
            if p1.data < p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Agrega los nodos restantes
        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = LinkedList.merge_sorted_lists(list1, list2)
print("Lista combinada:", merged_list.to_list())
