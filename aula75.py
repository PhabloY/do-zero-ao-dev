# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('Chamou upper')
#         retorno = super(MinhaString, self).upper()
#         print('Depois do upper')
#         return retorno
    
# string = MinhaString('Phablo')
# print(string.upper())

class A(object):
    atributo_a = 'AAAAA'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'BBBBB'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'CCCCC'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('Olá')

    def metodo(self):
        # super().metodo()
        # super(B, self).metodo()
        # super(A, self).metodo()
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer coisa')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()