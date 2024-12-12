def eliminar_duplicados(arreglo):
    arreglo_unico = []
    for elemento in arreglo:
        if elemento not in arreglo_unico:
            arreglo_unico.append(elemento)
    return arreglo_unico

arreglo_original = [1, 2, 2, 3, 4, 4, 5, 6, 6]
arreglo_sin_duplicados = eliminar_duplicados(arreglo_original)
print(f"Arreglo original: {arreglo_original}")
print(f"Arreglo sin duplicados: {arreglo_sin_duplicados}")
