class ControleRemoto:
    #Atributo de classe!
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 6

    #Atibutos de instância
    def __init__(self, canal = 1, volume = 1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    #Métodos de instância
    def liga_desliga(self):
        self.ligado = not self.ligado

    def mostrar_tv(self):
        print("I----------[\033[32mTV\033[0m]----------I")
        if self.ligado == False:
            print("A TV está desligada!")
        else:
            print(f"\033[31;48;5;231mCANAL\033[0m = ", end="")
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    print(f"\033[35m{canal}\033[0m", end = " ")
                else:
                    print(f"{canal}", end = " ")

            print(f"\n\033[31;48;5;231mVOLUME\033[0m = ", end = "")
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    print(f"\033[31;48;5;92m{volume}\033[0m", end = "")
                else:
                    print(f"{volume}", end = "")

             

c = ControleRemoto(3,5)
c.liga_desliga()
c.mostrar_tv()