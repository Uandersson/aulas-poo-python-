class Churrasco:
    #atributos de classe.
    consumo_padrao = 0.400
    preco_kg = 43.50

    #Atributos de instância
    def __init__(self, t = "", p = ""):
        self.titulo = t
        self.QuantPessoas = p

    def Calculo (self):
            return f"Esse é o {self.titulo} com {self.QuantPessoas} pessoas participando!"

    def analisando(self):
        conteudo = f"Analisando {self.titulo} com {self.QuantPessoas}"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        print(conteudo)

        
c1 = Churrasco("Churras dos crias", 15)
print(c1.Calculo())
print(c1.analisando())
