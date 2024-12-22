palavra = input('Digite uma palavra pra verificar se ela é um palindromo: ').lower().replace(' ', '')

if palavra == palavra[::-1]:
    print('Essa palavra é um palindromo')
else:
    print('Print essa palavra não é um palindromo')
