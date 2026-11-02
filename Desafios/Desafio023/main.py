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
        self.lado * 4
        return f"O perímetro do quadrado é {self.lado * 4}."
    
    def area(self):
        self.lado * self.lado
        return f"Essa a área do quadrado, {self.lado * self.lado} "


class Circulo(Poligono):
    def __init__(self, qtd, r):
        super().__init__(qtd)
        self.raio = r

    def perimetro(self):
        return f"Esse é o perimetro do circulo, {2 * self.raio * 3.14159:.2f}"

    def area(self):
        a = 3.14159 * self.raio ** 2
        return f"Essa é área do circulo, {a:.2f}"


w1 = Quadrado(8, 14)
print(w1.perimetro())
print(w1.area())


w = Circulo(8, 14)
print(w.perimetro())
print(w.area())
