from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, espe, nivel):
        super().__init__(nome, idade)
        self.especializacao = espe
        self.nivel = nivel

    def dar_aula(self):
        print(f'\nProfessor {self.nome}, começou a dar aula.')
