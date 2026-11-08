from abc import ABC,abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        mira = alvo
        dano = forca
        

    def receber_dano(self):
        pass

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)

    def curar(self):
        pass

class Mago(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)

    def curar(self):
        pass