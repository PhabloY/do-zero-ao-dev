"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = float(input('Digite um número inteiro '))
impar = entrada % 2 == 0

if entrada.is_integer():
    print('O número é inteiro')
else:
    print('esse número não é valido')

try:
    if impar:
        print('Esse número é par')
    else:
        print('Esse número é impar')
except:   
    print('esse não é um número valido.')
