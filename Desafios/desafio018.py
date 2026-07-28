class Churrasco:
    def __init__(self, t = "", p = ""):
        self.titulo = t
        self.QuantPessoas = p

    def Calculo (self):
        if self.QuantPessoas >= 5:
            return f"Com {self.QuantPessoas}"