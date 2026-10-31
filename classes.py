from abc import ABC,abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print("Fervendo água a 100 graus celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("Passando água pressurizada pelo café moido")

    def servir(self):
        print("Servindo em xícara pequena.")
        

class Cha(BebidaQuente):
    def misturar(self):
        print("Servindo na caneca de porcelana com limão")
    
    def servir(self):
        print("Mergulhando o sachê de ervas na água.")
        
            
class Leite(BebidaQuente):
    def misturar(self):
        print("Passando vapor pressurizado pelo bico do leite.")    

    def servir(self):
        print("Servindo na caneca grande, já com café")