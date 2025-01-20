import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "cidade": self.cidade}

    @classmethod
    def from_dict(cls, dados):
        return cls(dados['nome'], dados['idade'])
    

with open('classe.json', 'r') as arquivo:
    dados = json.load(arquivo)


if isinstance(dados, dict):
    pessoa = Pessoa.from_dict(dados)

print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")