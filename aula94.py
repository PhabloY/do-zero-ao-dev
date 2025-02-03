# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple

# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'valor'
    naipe: str = 'naipe'


# Carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['VALOR', 'NAIPE'])
as_espadas = Carta('A', 'Espadas')

print(as_espadas._asdict())
# print(as_espadas)
# print(as_espadas[0])
# print(as_espadas.naipe)
# print(as_espadas.valor)
# print()
# print(as_espadas._fields)
# print(as_espadas._field_defaults)
