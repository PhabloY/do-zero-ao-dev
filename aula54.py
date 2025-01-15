caminho_arquivo = 'C:\\Users\\user\\OneDrive\\Área de Trabalho\\teste\\'
caminho_arquivo += 'aula54.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print('Readlines')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())



with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())