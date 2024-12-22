"""
Iterando strings com while
"""
#       012345678910
nome = 'Phablo Yuri'  # Iteráveis
#      1110987654321

indice = 0 
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
print(novo_nome)
