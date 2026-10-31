class Pessoa:
    def __init__(self, n = "", i = "0"):
        self.nome = n
        self.idade = i

    def fazer_aniversario(self):
        self.idade += 1