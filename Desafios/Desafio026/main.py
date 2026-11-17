from Funcionarios import *


def main():
    f1 = Horista("larissa", 25, 250)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("larissa", 8500)
    f2.calc_sal()
    f2.analisar_sal()


if __name__ == "__main__":
    main()
