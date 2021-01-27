class Pokemon:
    nome: str
    hp_max: int
    hp_atual: int
    ataque: int
    defesa: int

    def __init__(self, nome, hp_max, hp_atual, ataque, defesa):
        self.nome = nome
        self.hp_max = hp_max
        self.hp_atual = hp_atual
        self.ataque = ataque
        self.defesa = defesa