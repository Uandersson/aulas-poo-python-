class ContaBancaria:
    """
    Crie uma conta bancaria, e permita fazer saques e depósitos!
    """

    def __init__(self, nome, ag, cc, senha, NumCard, saldo=0.0):
        self.nome = nome
        self.agencia = ag
        self.conta = cc
        self.senha = senha
        self.cartao = NumCard
        self.saldo = saldo

    def autenticar(self):
        print(
            f"\n Para ter acesso a conta tem que passar pela autenticação {self.nome}")
        tentativa = input("Digite a senha de 6 digitos: ")

        if tentativa == self.senha:
            print(f"Você acessou a conta de {self.nome}")
            return True

        else:
            print("Senha invalida, tente novamente!")
            return False

    def __str__(self):
        return f"Essa conta bancária é do nosso cliente, {self.nome} e seu saldo é de R${self.saldo:,.2f}"

    def Depositar(self, valor):
        self.saldo += valor

    def Sacar(self, valor):
        self.saldo -= valor


C1 = ContaBancaria("Uanderson", 02547.74, 7487, 147257, 4577.445-44, 10000)
C1.Depositar(500)
C1.Sacar(5698)
print(C1.__str__())
