from abc import ABC, abstractclassmethod #Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, n = "", i = "0"):
        self.nome = n
        self.idade = i

    def fazer_aniversario(self):
        self.idade += 1

    @abstractclassmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
      super().__init__(nome, idade)
      self.turma = turma
      self.curso = curso

    def fazer_matricula(self):
        print(f'\n\033[34m{self.nome} acabou de fazer a matricula.\033[0m')

    def estudar(self):
            pass


class Professor(Pessoa):
    def __init__(self, nome, idade, espe, nivel):
        super().__init__(nome, idade)
        self.especializacao = espe
        self.nivel = nivel

    def dar_aula(self):
        print(f'\nProfessor {self.nome}, começou a dar aula.')

    def estudar(self):
            pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'\n{self.nome}, acabou de bater o ponto.')

    def estudar(self):
            pass