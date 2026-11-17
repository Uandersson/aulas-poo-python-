class ContaBancaria:
    """
    Crie uma conta bancaria, e permita fazer saques e depósitos!
    """

    def __init__(self, nome, ag, cc, senha, NumCard, saldo = 0):
        self.nome = nome
        self.agencia = ag
        self.conta = cc
        self.senha = senha
        self.cartao = NumCard
        self.saldo = saldo

    def __str__(self):
        return f"Essa conta bancária é do nosso cliente, {self.nome} e seu saldo é de R${self.saldo:,.2f}"

    def Depositar(self, valor):
        self.saldo += valor
        print(f"Saque NEGADO de R${valor:.2f} na conta {self.conta} saldo INSUFICIENTE.")

    def Sacar(self, valor):
        self.saldo -= valor
        print(f"Saque de {valor:.2f} autorizado na conta {self.nome}")