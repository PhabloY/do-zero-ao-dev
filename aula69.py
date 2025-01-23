# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'Isso está protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'Metodo publico'
        

    def _metodo_protected(self):
        print('metodo protected')
        return 'Metodo protected'
    

    def __metodo_private(self):
        print('metodo private')
        return 'Metodo private'


f = Foo()
# print(f.public)
print(f.metodo_publico())
print(f._Foo__metodo_private())