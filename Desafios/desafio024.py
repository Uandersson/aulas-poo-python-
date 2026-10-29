from abc import ABC,abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        pass

    def ferver_agua(self):
        return "Fervendo água a 100 graus celsius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self, a):
        self.agua = a

    def misturar(self):
        return f"Passando água pressurizada pelo café moido"
        

class Cha(BebidaQuente):
    def __init__(self):
        pass

class Leite(BebidaQuente):
    def __init__(self):
        pass


c1 = BebidaQuente()
print(c1.ferver_agua())
