from abc import ABC, abstractmethod

class Funcionario(ABC):
    #Atributo de classe
    sal_min = 1612
    inss = 7.5

    def __init__(self, name, bruto = 0, sal = 0):
        self.nome = name 
        self.sal_bruto = bruto
        self.salario = sal

    def analisar_sal(self):
        print (f"O salário de {self.nome} Funcionario Horista é de R$ {self.salario:.2f} e corresponde a {self.calc_sal.salario}")

    @abstractmethod
    def calc_sal(self):
        pass


class Horista(Funcionario):
    def __init__(self, name, valor, hora):
        super().__init__(name)
        self.valor_hora = valor
        self.hora_trab = hora

    def calc_sal(self):
        self.bruto = self.valor_hora * self.hora_trab
        self.salario = self.bruto * (Funcionario.inss / 100)
        salario = self.salario / Funcionario.sal_min
        
        return salario

class Mensalista(Funcionario):
    def __init__(self, name, bruto):
        super().__init__(name, bruto)

    def calc_sal(self):
        self.salario = self.sal_bruto * (Funcionario.inss / 100)
        return self.salario