def invertir_arreglo(arreglo):
    arreglo_invertido = []
    for i in range(len(arreglo) - 1, -1, -1):  # Recorre el arreglo de atrás hacia adelante
        arreglo_invertido.append(arreglo[i])
    return arreglo_invertido

arreglo_original = [1, 2, 3, 4, 5]
arreglo_invertido = invertir_arreglo(arreglo_original)
print(f"Arreglo original: {arreglo_original}")
print(f"Arreglo invertido: {arreglo_invertido}")
