class Produto:
    def __init__(self, n="", p=""):
        self.nome = n
        self.preço = p

    def etiqueta(self):
        return f"{self.nome} custa R${self.preço:,.2f}"


c1 = Produto("Samsung S26 Ultra", 11.784)
print(c1)
