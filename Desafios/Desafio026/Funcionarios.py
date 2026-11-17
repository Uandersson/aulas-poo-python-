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
        base = self.salario / Funcionario.sal_min
        print (f"O salário de {self.nome} {self.__class__.__name__} é de R${self.salario:.2f} e corresponde a {base:.1f} salários minimos")

    @abstractmethod
    def calc_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self, name, valor = 7.37, hora = 220):
        super().__init__(name) 
        self.valor_hora = valor
        self.hora_trab = hora
        self.bruto = self.valor_hora * self.hora_trab

    def calc_sal(self):
        self.salario = self.bruto - (self.bruto * Funcionario.inss / 100)

class Mensalista(Funcionario):
    def __init__(self, name, bruto):
        super().__init__(name, bruto)

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100) 