from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd):
        self.qtd_lados = qtd

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, ld):
        super().__init__(4)
        self.lado = ld

    def perimetro(self):
        self.lado * 4
        return f"Um quadro de lado {self.lado}cm tem perímetro de {self.lado * 4}cm."
    
    def area(self):
        self.lado * self.lado
        return f"Um quadro de lado {self.lado}cm tem área de {self.lado * self.lado}cm."


class Circulo(Poligono):
    def __init__(self, r = 1):
        super().__init__(0)
        self.raio = r

    def perimetro(self):
        return f"Um circulo de raio {self.raio}cm tem perímetro de {2 * self.raio * 3.14159:.2f}cm."

    def area(self):
        a = 3.14159 * self.raio ** 2
        return f"Um circulo de raio {self.raio}cm tem área de {a:.2f}cm."


w1 = Quadrado(20)
print(w1.perimetro())
print(w1.area())


w = Circulo(12)
print(w.perimetro())
print(w.area())
