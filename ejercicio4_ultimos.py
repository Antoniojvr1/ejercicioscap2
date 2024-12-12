def numero_presente(arreglo, numero):
    for elemento in arreglo:
        if elemento == numero:
            return True
    return False

arreglo = [10, 20, 30, 40, 50]
numero_a_buscar = 30

if numero_presente(arreglo, numero_a_buscar):
    print(f"El numero {numero_a_buscar} esta presente en el arreglo.")
else:
    print(f"El numero {numero_a_buscar} no esta presente en el arreglo.")
