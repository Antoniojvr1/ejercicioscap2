class Array(object):
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # The array stored as a
        self.__nItems = 0 # No items in array

def __len__(self): # Special def for len()
    return self.__nItems # Return number of items
def get(self, n): # Return the value at index
    if 0 <= n and n < self.__nItems: # Check if n is in bounds,
        return self.__a[n] # only return item if in

def set(self, n, value): # Set the value at index n
    if 0 <= n and n < self.__nItems: # Check if n is in bounds,
        self.__a[n] = value # only set item if in

def insert(self, item): # Insert item at end
    self.__a[self.__nItems] = item # Item goes at current end
    self.__nItems += 1 # Increment number of items
def find(self, item): # Find index for item
    for j in range(self.__nItems): # Among current items
        if self.__a[j] == item: # If found,
            return j # then return index to item
    return -1 # Not found -> return -1

def search(self, item): # Search for item
    return self.get(self.find(item)) # and return item if found
def delete(self, item): # Delete first occurrence
    for j in range(self.__nItems): # of an item
        if self.__a[j] == item: # Found item
            self.__nItems -= 1 # One fewer at end
    for k in range(j, self.__nItems): # Move items from
        self.__a[k] = self.__a[k+1] # right over 1
    return True # Return success flag
    return False # Made it here, so couldn't find the item
def traverse(self, function=print): # Traverse all items
    for j in range(self.__nItems): # and apply a function
        function(self.__a[j])

def median(self):
        # Método para calcular la mediana
        if self.__nItems == 0:
            return None  # Caso para arreglo vacío

        mid = self.__nItems // 2
        if self.__nItems % 2 == 1:  # Número impar de elementos
            return self.__a[mid]
        else:  # Número par de elementos
            return (self.__a[mid - 1] + self.__a[mid]) / 2