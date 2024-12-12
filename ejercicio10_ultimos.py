class HistorialNavegacion:
    def __init__(self):
        self.historial = []

    def agregar_pagina(self, pagina):
        self.historial.append(pagina)

    def ir_atras(self):
        if not self.historial:
            print("No hay paginas anteriores en el historial.")
            return
        self.historial.pop()
        if self.historial:
            print("Pagina actual:", self.historial[-1])
        else:
            print("Estas en la primera pagina.")

historial = HistorialNavegacion()
historial.agregar_pagina("https://translate.google.com/?sl=en&tl=es&text=could%20not%20convert%20string%20to%20float%3A%20%27%2B%27&op=translate")
historial.agregar_pagina("https://translate.google.com/?sl=en&tl=es&text=could%20not%20convert%20string%20to%20float%3A%20%27%2B%27&op=translate")
historial.ir_atras()  # Imprime: Página actual: https://www.example.com
historial.ir_atras()  # Imprime: Estás en la primera página.
historial.ir_atras()  # Imprime: No hay páginas anteriores en el historial.