# def duplicar(numero):
#     return numero * 2
# def quadriplicar(numero):
#     return numero * 4
# def triplicar(numero):
#     return numero * 3
        
# numero_duplicado = duplicar(2)
# numero_triplicado = triplicar(2)
# numero_quadruplicado = quadriplicar(2)
# print(numero_duplicado)
# print(numero_triplicado)
# print(numero_quadruplicado)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
