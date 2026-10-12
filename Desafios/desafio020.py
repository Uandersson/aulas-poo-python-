class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_fav(self, game):
        self.favoritos.append(game)

    def status(self):
        conteudo = f"\033[33mNome real:\033[0m \033[34m{self.nome}\033[0m"
        conteudo1 = f"Jogos favoritos: {self.favoritos}"
        print(
            f"\n\033[95m=-=-=-=-=-=-=\033[0m \033[31mJogador {self.nick}\033[0m \033[95m=-=-=-=-=-=-=\033[0m")
        print(f"{conteudo}")
        print(f"{conteudo1}\n")


Usuario = input("Digite seu nome e: ")
usurio = input("Digite seu nick ")
jogo = input("Digite seu jogo favorito ")
j1 = Gamer(Usuario, usurio)
j1.add_fav(jogo)
j1.status()
