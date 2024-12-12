def calcular_suma(arreglo):
    suma = 0
    for numero in arreglo:
        suma += numero
    return suma

arreglo_numeros = [1, 2, 3, 4, 5]
resultado = calcular_suma(arreglo_numeros)
print(f"La suma de los elementos del arreglo es: {resultado}")
