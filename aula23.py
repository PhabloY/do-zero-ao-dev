def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicação = multiplicador(1, 2, 3, 6, 8, 9)
print(multiplicação)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'
        
outro_par_impar = par_impar
dois_e_par = outro_par_impar(3)
print(dois_e_par)
print(par_impar is outro_par_impar)
