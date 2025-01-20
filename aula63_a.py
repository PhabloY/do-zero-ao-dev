import json

# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome 
#         self.idade = idade
        
#     def get_ano_nascimento(self):
#         return Pessoa.ano_atual - self.idade
    
#     def to_json(self):
#         with open('classe.json', 'w', encoding='utf-8') as arquivo:
#             return json.dump(self.__dict__, arquivo, ensure_ascii=False, indent=2,)


# dados = {'nome': 'Phablo', 'idade': 24,}
# p1 = Pessoa(**dados)


# p1.to_json()

CAMINHO_ARQUIVO = 'classe.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

p1 = Pessoa('Costa', 24)
p2 = Pessoa('Yuri', 24)
p3 = Pessoa('Phablo', 24)

bd = [vars(p1), p2.__dict__, vars(p3)]

def salvar():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Ele é o __main')
    salvar()


    