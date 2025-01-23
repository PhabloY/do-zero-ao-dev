"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = int(input('Digite a hora aqui '))
minutos = int(input('Digite os minutos aqui '))
checagem_horas = horas < 0 or horas > 23
checagem_minutos = minutos < 0 or minutos > 59
checagem_dia = horas <= 11
checagem_tarde = 12 <= horas <= 17
checagem_noite = horas > 17

if checagem_horas:
    print('Digite um horário válido entre 0 e 23')
 
if checagem_minutos:
    print('Digite um minuto válido entre 0 e 59')

if checagem_dia:
    saudacao = 'Bom dia'
elif checagem_tarde:
    saudacao = 'Boa tarde'
elif checagem_noite:
    saudacao = 'Boa noite'

print(f"{saudacao}! agora são {horas}:{minutos:02}.")

entrada = input('Escreva um número inteiro ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço esse número')
except:
    print('Por favor digite apenas número inteiros')
