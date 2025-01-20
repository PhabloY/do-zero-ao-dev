class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('anônima', idade)


p1 = Pessoa('Phablo', 24)
p2 = Pessoa.criar_com_50_anos('Phablo')
p3 = Pessoa('anônima', 23)
p4 = Pessoa.criar_sem_nome(23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
