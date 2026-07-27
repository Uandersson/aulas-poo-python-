class Gafanhoto:
    def __init__(self):# Metodo construtor.
        #Atributos de instancia.
        self.nome = ""
        self.idade = 0

    #Métodos de instância.
    def Aniversario(self):
        self.idade += 1 


    def Mensagem(self):
        return f"{self.idade} essa é a idade deste gafanhoto, e seu nome é {self.nome}!"


g1 = Gafanhoto()
g1.nome = "Eduardo"
g1.idade = 12
g1.Aniversario
print(g1.Mensagem())