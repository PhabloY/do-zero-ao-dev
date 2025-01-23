import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar ')

    if opcao == 'i':
        os.system('cls')
        valor = input('insira o item: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha um indice para apagar. ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um numero inteiro.')
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para mostrar')

        for i, valor, in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor escolhe i, a ou l')

