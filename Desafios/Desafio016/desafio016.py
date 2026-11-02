class Funcionario:
    #Atributo de classe
    empresa = "Itau"

    def __init__(self, n="", s="", c=""):
        self.nome = n
        self.setor = s
        self.cargo = c

    def apresentacao(self) -> str:
        return f"ola, eu sou {self.nome} e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}!"


    def __init__(self, nome = "",setor = "",cargo = "", salario = 0,): 
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.salario = salario

    def apresentacao(self):
        return f"ola, eu sou {self.nome} e sou {self.cargo} no setor de {self.setor} e trabalho no Itáu!"

    def aumentar_salario(self, aumento):
        self.salario += aumento
        return f"Salário atualizado: {self.salario}"        

    def __str__(self):
        return f"Funcionario: {self.nome}, Setor: {self.setor}, Cargo: {self.cargo}, Salário: {self.salario}"  
    

c1 = Funcionario("Uanderson", "TI", "Desenvolvedor", 5000)
c1.aumentar_salario(500)
print(c1.apresentacao())

print(c1)
