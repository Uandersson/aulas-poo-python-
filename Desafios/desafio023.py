from abc import ABC, abstractclassmethod #Abstract Base Classes

class Poligono(ABC):
    def __init__(self, qtd):
        self.qtd_lados = qtd

    @abstractclassmethod
    def perimetro(self):
        pass

    @abstractclassmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, qtd, ld):
        super().__init__(qtd)
        self.lado = ld

    def perimetro(self):
        resultado = self.lado * 4
        return resultado

    def area(self):
        pass


w1 = Quadrado(4, 12)
w1.perimetro()
w1.area()