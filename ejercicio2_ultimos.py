def encontrar_max_min(arreglo):
    if not arreglo:  # Verificar si el arreglo está vacío
        return None, None
    
    maximo = minimo = arreglo[0]  # Inicializar con el primer elemento del arreglo
    
    for numero in arreglo:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    return maximo, minimo

arreglo_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
maximo, minimo = encontrar_max_min(arreglo_numeros)
print(f"El valor maximo es: {maximo}")
print(f"El valor manimo es: {minimo}")
