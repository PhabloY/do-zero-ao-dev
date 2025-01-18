from random import randint

lista_npcs = []

def criar_monstro():
    level = randint(0, 50)
    novo_npc = {
        'nome': f'Monstro #{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
    }
    lista_npcs.append(novo_npc)

criar_monstro()
print(lista_npcs)