entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite sua senha:')
senha_permitida = '12345'

if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
