from Personagem import *


def main():
    p1 = Guerreiro("Rick", 1000)
    p2 = Mago("Harry", 8000)

    p1.atacar(p2, 1004)
    p2.atacar(p1, )

    p1.curar()
    p2.curar()


if __name__ == "__main__":
    main()
