class Combate:
    
    def __init__(self):
        pass

    def atacar(self, atacante, defensor):
        dano = atacante.ataque - (defensor.defesa/2)
        defensor.hp_atual = min(0,(defensor.hp_atual - dano))

    def especial(self, atacante):
        dano = atacante.atacante - (defensor.defesa/4)
        defesor.hp_atual = min(0, (defensor.hp_atual - dano))


    def curar(self, atacante):
        atacante.hp_atual =  min(atacante.hp_max,(atacante.hp_atual + 2))



        