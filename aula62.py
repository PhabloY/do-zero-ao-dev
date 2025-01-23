

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

dados = {'nome': 'Phablo', 'idade': 35,}
p1 = Pessoa(**dados)
# p1.nome = 'Eita'
# print(p1.nome)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Phablo'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)