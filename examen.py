from collections import deque
class ColaEspecial(object):
    def insertar(self, elemento):
        if len(self.cola) == self.tamaño:
            self.cambiar_direccion()

        if self.direccion == 1:
            self.cola.append(elemento)
        else:
            self.cola.appendleft(elemento)

    def cambiar_direccion(self):
        self.direccion *= -1
    def mostrar_cola(self):
        print(list(self.cola))

cola = ColaEspecial()
for i in range(10):
    print(f"Inserción del elemento {i}")
    cola.insertar(i)
    cola.mostrar_cola()
    def _init_(self, tamaño=10):
        self.tamaño = tamaño
        self.cola = deque(maxlen=tamaño)  
        self.direccion = 1 

    def insert(self, item):  # Inserta el elemento al final
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def traverse(self, function=print):  # Recorre todos los elementos
        for j in range(self.__nItems):
            function(self.__a[j])
    
cadena = [ 'a , b , c , d , e , f , g , h , i , j ']  
print("la cadena de numeros es: ", cadena )

print("insertando elementos nuevos...")

print("la cadena con el nuevo elemento es: " , cadena)



