class Funcionario:
    def __init__(self, n = "",s = "",c = ""):
        self.nome = n
        self.setor = s 
        self.cargo = c

    def __getstate__(self):
        return f"ola, eu sou {self.nome} e sou {self.cargo} no setor de {self.setor} e trabalho no Itáu!"

c1 = Funcionario("Uanderson", "TI", "Desenvolvedor")
print(c1.__getstate__()) 