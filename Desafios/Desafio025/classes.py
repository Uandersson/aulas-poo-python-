from abc import ABC, abstractmethod

class Transporte:
    def __init__(self, dis, fre = 0):
        self.distancia = dis
        self.frete = fre

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, dis):
        super().__init__(dis)

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f"R$ {self.frete:.2f}"


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, dis):
        super().__init__(dis)

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * self.fator
            return f"R$ {self.frete:.2f}"
        else:
            return "Não aceitamos fretes abaixo de 50 Km, obrigado!"


class Drone(Transporte):
    fator = 9.50

    def __init__(self, dis):
        super().__init__(dis)

    def calc_frete(self):
        if self.distancia <= 10:
           self.frete = self.distancia * self.fator
           return f"R$ {self.frete:.2f}"
        else:
            return "Não aceitamos fretes acima de 10 Km, obrigado!"