def erro_divide_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você estã tentando dividir por 0')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n,(float, int)):
        raise TypeError(
            f'{n} deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
            )
    return True
def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    erro_divide_por_zero(d)
    return n / d
  
print(divide(8, 0))