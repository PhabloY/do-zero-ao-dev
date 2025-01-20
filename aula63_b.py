import json

from aula63_a import CAMINHO_ARQUIVO, Pessoa, salvar

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     @classmethod
#     def from_dict(self, dados):
#         return self(dados['nome'], dados['idade'])
    

# with open('classe.json', 'r') as arquivo:
#     dados = json.load(arquivo)

# pessoas = [Pessoa.from_dict(dado) for dado in dados]

# for pessoa in pessoas:
#     print(pessoa.nome, pessoa.idade)

salvar()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

print(__name__)