class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __find(self, key, shallow=False):
        def find_deepest(node, key):
            result = None
            while node:
                if node.key == key:
                    result = node
                    if shallow:
                        break
                node = node.right if key > node.key else node.left
            return result

        return find_deepest(self.root, key)

    def insert(self, key, value=None):
        if not self.root:
            self.root = Node(key, value)
            return

        node = self.__find(key)
        if node and node.key == key:
            # Insertar como hijo izquierdo vacío
            new_node = Node(key, value)
            while node.left:
                node = node.left
            node.left = new_node
            new_node.parent = node
        else:
            # Insertar normalmente en el árbol
            self._insert(self.root, key, value)

    def insert(self, key, value=None):
        if not self.root:
            self.root = Node(key, value)
            print("Nodo raiz insertado:", self.root.key)
            return
            node = self.__find(key)
        if node and node.key == key:
        # Insertar como hijo izquierdo vacío
            new_node = Node(key, value)
        while node.left:
            node = node.left
            node.left = new_node
            new_node.parent = node
            print(f"Nodo duplicado insertado debajo de {node.key}: {new_node.key}")
        else:
        # Insertar normalmente en el árbol
            self._insert(self.root, key, value)
            print(f"Nodo {key} insertado normalmente.")


    def delete(self, key):
        node = self.__find(key)
        if not node:
            print("Clave no encontrada")
            return

        if node.left or node.right:
            # Encontrar sucesor si tiene hijos
            successor = self._find_successor(node)
            if successor:
                node.key, node.value = successor.key, successor.value
                node = successor

        # Eliminar nodo (sin hijos o sucesor ya procesado)
        if node.parent:
            if node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None
        else:
            self.root = None  # Nodo raíz eliminado

    def _find_successor(self, node):
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        return None

    def traverse(self, node=None, visited=None):
        if node is None:
            node = self.root
        if visited is None:
            visited = set()

        if node and node not in visited:
            visited.add(node)
            self.traverse(node.left, visited)
            print(f"Key: {node.key}, Value: {node.value}")
            self.traverse(node.right, visited)

# Crear el arbol
bst = BinarySearchTree()
bst.insert(10, "A")
bst.insert(10, "B")
bst.insert(10, "C")
bst.insert(5, "D")
bst.insert(15, "E")

# Mostrar el arbol
print("arbol despues de inserciones:")
bst.traverse()

# Eliminar duplicados
print("\nEliminando claves duplicadas:")
bst.delete(10)  # Debería eliminar "C"
bst.traverse()

bst.delete(10)  # Debería eliminar "B"
bst.traverse()

bst.delete(10)  # Debería eliminar "A"
bst.traverse()
