class Gafanhoto:
    def __init__(self, nome = "Vazio", idade = 0):# Metodo construtor.
        #Atributos de instancia.
        self.nome = nome
        self.idade = idade

    #Métodos de instância.
    def Aniversario(self):
        self.idade += 1 


    def __str__(self):
        return f"{self.idade} essa e a idade deste gafanhoto, e seu nome e {self.nome}!"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


#Declaração de objetos
g1 = Gafanhoto("Uanderson", 21)
g1.Aniversario
print(g1)


print(g1.__dict__)#Atributo
print(g1.__getstate__())#metodo
print(g1.__doc__)
print(g1.__class__)