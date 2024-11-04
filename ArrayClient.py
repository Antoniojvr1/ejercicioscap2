import random
class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado
        self.__nItems = 0  # Sin items inicialmente

    def __len__(self):  # Función especial para len()
        return self.__nItems  # Devuelve el número de elementos

    def get(self, n):  # Retorna el valor en el índice n
        if 0 <= n < self.__nItems:  # Chequea si n está dentro de los límites
            return self.__a[n]

    def set(self, n, value):  # Setea el valor en el índice n
        if 0 <= n < self.__nItems:
            self.__a[n] = value

    def insert(self, item):  # Inserta el elemento al final
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):  # Busca el índice de un elemento
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):  # Busca y retorna el elemento
        return self.get(self.find(item))

    def delete(self, item):  # Elimina la primera ocurrencia de un elemento
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
        return False

    def traverse(self, function=print):  # Recorre todos los elementos
        for j in range(self.__nItems):
            function(self.__a[j])

    def getMaxNum(self):  # Encuentra el valor más alto numérico
        max_num = None
        for x in self.__a[:self.__nItems]:  # Solo recorre los elementos activos
            if isinstance(x, (int, float)):  # Si es numérico
                if max_num is None or x > max_num:
                    max_num = x
        return max_num
    
    def getAverageNum(self):
        total_num = 0 
        count = 0 
        for x in self.__a[:self.__nItems]:
            if isinstance(x, (int, float)):
                total_num += x
                count += 1 
        if count == 0:
            return None  
        return total_num / count 

    def deleteMaxNum(self):
            max_num = self.getMaxNum()  # Encuentra el numero mas alto
            if max_num is not None:
                self.__a.remove(max_num) # Elimina el numero mas alto
                self.__nItems -= 1 # esta funcion reduce la cantidad de elementos que hay en el arreglo
            return max_num  # Devuelve el numero mas alto eliminado


# Ejemplo de uso (ArrayClient)
arr = Array(10)  # Crear objeto array
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array contiene", len(arr), "elementos")
arr.traverse()

print("El numero mas grande es:", arr.getMaxNum())
average = arr.getAverageNum()
print("El promedio es: ", average)

print("Arreglo antes de eliminar el numero maximo: ")
arr.traverse()

arr.deleteMaxNum() 

print("Arreglo despues de eliminar el numero maximo: ") 
arr.traverse()

# Genera una lista de 100 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(100)]

# Función para extraer números pares en forma de pila
def extraer_pares_pila(numeros):
    return [num for num in reversed(numeros) if num % 2 == 0]

# Función para extraer números impares en forma de pila
def extraer_impares_pila(numeros):
    return [num for num in reversed(numeros) if num % 2 != 0]

# Función para extraer números pares en forma de cola
def extraer_pares_cola(numeros):
    return [num for num in numeros if num % 2 == 0]

# Función para extraer números impares en forma de cola
def extraer_impares_cola(numeros):
    return [num for num in numeros if num % 2 != 0]

# Función para calcular el promedio de una lista de números
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# Ejemplo de uso de las funciones
print("Lista inicial de numeros:", numeros)

# Extracción en forma de pila y cálculo de cantidad y promedio
pares_extraidos_pila = extraer_pares_pila(numeros)
cantidad_pares_pila = len(pares_extraidos_pila)
promedio_pares_pila = calcular_promedio(pares_extraidos_pila)
print("\nNumeros pares extraidos en forma de pila:", pares_extraidos_pila)
print("Cantidad de numeros pares extraidos en forma de pila:", cantidad_pares_pila)
print("Promedio de numeros pares extraidos en forma de pila:", promedio_pares_pila)

impares_extraidos_pila = extraer_impares_pila(numeros)
cantidad_impares_pila = len(impares_extraidos_pila)
promedio_impares_pila = calcular_promedio(impares_extraidos_pila)
print("\nNumeros impares extraidos en forma de pila:", impares_extraidos_pila)
print("Cantidad de numeuos impares extraidos en forma de pila:", cantidad_impares_pila)
print("Promedio de numeros impares extraidos en forma de pila:", promedio_impares_pila)

# Extracción en forma de cola y cálculo de cantidad y promedio
pares_extraidos_cola = extraer_pares_cola(numeros)
cantidad_pares_cola = len(pares_extraidos_cola)
promedio_pares_cola = calcular_promedio(pares_extraidos_cola)
print("\nNumeros pares extraidos en forma de cola:", pares_extraidos_cola)
print("Cantidad de numeros pares extraidos en forma de cola:", cantidad_pares_cola)
print("Promedio de numeros pares extraidos en forma de cola:", promedio_pares_cola)

impares_extraidos_cola = extraer_impares_cola(numeros)
cantidad_impares_cola = len(impares_extraidos_cola)
promedio_impares_cola = calcular_promedio(impares_extraidos_cola)
print("\nNumeros impares extraidos en forma de cola:", impares_extraidos_cola)
print("Cantidad de numeros impares extraidos en forma de cola:", cantidad_impares_cola)
print("Promedio de numeros impares extraidos en forma de cola:", promedio_impares_cola)



