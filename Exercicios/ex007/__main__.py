from Exercicios.ex007.classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno('jose', 15, 'ADS', 'turma 2')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    print(a1.__dict__)

    p = Professor('Gabriel', 32, 'Tecnologia da Informação', 'Doutorado')
    p.dar_aula()
    print(p.__dict__)

    f = Funcionario('Maria Julia', 19, 'Secretaria', 'Secretaria')
    f.bater_ponto()
    print(f.__dict__)

if __name__ == "__main__":
    main()