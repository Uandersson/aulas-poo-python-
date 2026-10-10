class Caneta:
    def __init__(self, cor ="azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "\033[94m"
            case "vermelho":
                escolha = "\033[91m"
            case "verde":
                escolha = "\033[92m"
            case _:
                escolha = "\033[97m"
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f"Está proibido: A{self.cor}\033[0m caneta está tampada")
        else:
            print(f"{self.cor}{msg}\033[0m", end ="" )

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd, end="")

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta("verde")
c2 = Caneta("azul")
c3 = Caneta("vermelho")

c1.destampar()
c2.destampar()


c1.escrever("Olá mundo")
c1.quebrar_linha(2)
c2.escrever("Olá mundo")
c2.quebrar_linha(2)
c3.escrever("Olá mundo")