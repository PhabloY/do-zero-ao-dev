string = input('Digite alguma coisa ')

num_letras = 0
num_digitos = 0

for char in string:
    if char.isalpha():
        num_letras += 1
    elif char.isdigit():
        num_digitos += 1

print(num_letras)
print(num_digitos)
