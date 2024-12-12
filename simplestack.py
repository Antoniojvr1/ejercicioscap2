class Stack(object):
    def __init__(self, max):
        self.__stackList = [None] * max
        self.__top = -1

    def push(self, item):
        if self.isFull():
            raise Exception("Error: La pila está llena. No se puede insertar.")
        self.__top += 1
        self.__stackList[self.__top] = item

    def pop(self):
        if self.isEmpty():
            raise Exception("Error: La pila está vacía. No se puede extraer.")
        top = self.__stackList[self.__top]
        self.__stackList[self.__top] = None
        self.__top -= 1
        return top

    def isEmpty(self):
        return self.__top < 0

    def isFull(self):
        return self.__top >= len(self.__stackList) - 1

class Deque:
    def __init__(self, max_size):
        self.dequeList = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = 0
        self.size = 0

    def addFront(self, item):
        if self.size == self.max_size:
            raise Exception("Deque is full")
        self.front = (self.front - 1) % self.max_size
        self.dequeList[self.front] = item
        self.size += 1

    def removeFront(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        item = self.dequeList[self.front]
        self.dequeList[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

class Stack:
    def __init__(self, max_size):  # Constructor
        self.deque = Deque(max_size)

    def push(self, item):  # Insert item at top of stack
        self.deque.addFront(item)  # Use deque’s addFront for stack push

    def pop(self):  # Remove top item from stack
        return self.deque.removeFront()  # Use deque’s removeFront for stack pop

    def peek(self):  # Return top item
        if not self.isEmpty():
            return self.deque.dequeList[self.deque.front]
        return None

    def isEmpty(self):  # Check if stack is empty
        return self.deque.isEmpty()

    def isFull(self):  # Check if stack is full
        return len(self.deque) == self.deque.max_size

    def __len__(self):  # Return number of items on stack
        return len(self.deque)

    def __str__(self):  # Convert stack to string
        items = []
        index = self.deque.front
        for _ in range(len(self.deque)):
            items.append(str(self.deque.dequeList[index]))
            index = (index + 1) % self.deque.max_size
        return "[" + ", ".join(items) + "]"
