class Token ():
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def __str__(self):
        return f"Valor: {self.valor} Tipo: {self.tipo}"