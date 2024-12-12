def invertir_cadena(cadena):
  """Invierte una cadena de texto utilizando una pila.

  Args:
    cadena: La cadena de texto a invertir.

  Returns:
    str: La cadena invertida.
  """

  pila = []
  for caracter in cadena:
    pila.append(caracter)

  cadena_invertida = ""
  while pila:
    cadena_invertida += pila.pop()

  return cadena_invertida

cadena_original = "Hola, mundo!"
print("la cadena original es: ", cadena_original)
cadena_invertida = invertir_cadena(cadena_original)
print("la cadea invertida es: ", cadena_invertida) 

cadena_original2 = "soy antonio josue"
print("la cadena original 2 es: ", cadena_original2)
cadena_invertida2 = invertir_cadena(cadena_original2)
print("la ccadena invertida2 es: ", cadena_invertida2) 