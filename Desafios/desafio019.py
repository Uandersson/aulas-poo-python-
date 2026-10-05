import time

class Livro:
    def __init__(self, titulo, paginas):
        self.total_paginas = paginas
        self.titulo = titulo
        self.pagina_atual = 1

        print(f"\033[34mVocê acabou de abrir o livro\033[0m \033[31m{self.titulo}\033[0m \033[34mque tem\033[0m \033[32m{self.total_paginas} páginas\033[0m \033[34mno total,você agora está na\033[0m \033[33mpágina {self.pagina_atual}\033[0m")

    def avancar_paginas(self, qnt=1):
        cont = 0
        for pg in range(0, qnt, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pag => {self.pagina_atual} ", end='')
                time.sleep(0.2)
                cont += 1
        print(f"Você avançou {cont} páginas e agora está na página {self.pagina_atual}!")
        time.sleep(0.2)
        if self.fim_do_livro():
            print(f"O livro '{self.titulo}' contém apenas {self.total_paginas} páginas e você chegou ao fim, parabéns!") 
            time.sleep(0.2)

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False


l1 = Livro("Em busca da vida", 10)
l1.avancar_paginas(11)
