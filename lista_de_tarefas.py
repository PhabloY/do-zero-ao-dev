# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando ')

#     if tarefa == 'listar':
#         tarefa_listada = input('Digite a tarefa ')
#         tarefas.append(tarefa_listada)
    
#     elif tarefa == 'desfazer':
#         desfazer = tarefas.pop(-1)
#         tarefas_refazer.append(desfazer)
    
#     elif tarefa == 'refazer':
#         refazer = tarefas_refazer.pop(-1)
#         tarefas.append(refazer)
    
#     elif tarefa == 'q':
#         break
#     else:
#         print('Digite uma tarefa')
   
#     for acoes in tarefas:
#             print(acoes) 

import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista.')
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista.')
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    print(f'{tarefa=} adicionada na lista.')
    tarefas.append(tarefa)
    print()

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'q':
        break

    elif tarefa == 'clear':
        os.system('cls')
        continue

    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)

    