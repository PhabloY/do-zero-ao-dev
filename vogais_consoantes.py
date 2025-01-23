palavra = input('Digite alguma coisa e eu te direi o número de vogais e consoantes ').lower()
vogais = ['a','e','i','o','u']

contador_vogais = 0
contador_consoantes = 0

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
    else:
        contador_consoantes += 1

print(f'o número de vogais na palavra/frase é {contador_vogais}')
print(f'o número de consoantes na palavra/frase é {contador_consoantes}')
