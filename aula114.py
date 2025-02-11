import sys
argumentos = sys.argv
qnd_argumentos = len(argumentos)

if qnd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos, {argumentos[1:]}')
        print(f'Faça alguma coisa com o argumento 1, {argumentos[1:]}')
        print(f'Faça alguma coisa com o argumento 2, {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
