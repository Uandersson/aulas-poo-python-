from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
      super().__init__(nome, idade)
      self.turma = turma
      self.curso = curso

    def fazer_matricula(self):
        print(f'\n\033[34m{self.nome} acabou de fazer a matricula.\033[0m')