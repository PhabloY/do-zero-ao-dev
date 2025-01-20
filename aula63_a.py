import json

# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    def to_json(self):
        with open('classe.json', 'w', encoding='utf-8') as arquivo:
            return json.dump(self.__dict__, arquivo, ensure_ascii=False, indent=2,)


dados = {'nome': 'Phablo', 'idade': 24,}
p1 = Pessoa(**dados)


p1.to_json()
# print(p1.__dict__)

