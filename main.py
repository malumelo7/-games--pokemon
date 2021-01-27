from pokemon import Pokemon
from combate import Combate

def main():
    bombassauro = Pokemon('bombassauro', 10, 10, 6, 6)
    pikachu = Pokemon('pikachu', 10, 10, 7, 5)


    combate = Combate()
    combate.atacar(bombassauro,pikachu)
    print(pikachu.hp_atual)
    combate.curar(bombassauro)
    print(bombassauro.hp_atual)
    
if __name__ == "__main__":
    main()


