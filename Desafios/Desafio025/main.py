from classes import *

def main():
    dist = 10

    entrega = Drone(dist)
    print(f"\nFrete de {type(entrega).__name__} em {dist} Km = {entrega.calc_frete()}\n")

if __name__ == "__main__":
    main()