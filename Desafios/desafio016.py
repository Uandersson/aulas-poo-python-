class Funcionario:
    #Atributo de classe
    empresa = "Itau"

    def __init__(self, n="", s="", c=""):
        self.nome = n
        self.setor = s
        self.cargo = c

    def apresentacao(self) -> str:
        return f"ola, eu sou {self.nome} e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}!"


c1 = Funcionario("Uanderson", "TI", "Desenvolvedor")
print(c1.apresentacao())
