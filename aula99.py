# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_inicio = datetime.strptime('20/12/2020', '%d/%m/%Y')
data_final = data_inicio + relativedelta(years=5)
valor_emprestimo = 1000000
meses = 60
valor_parcela = valor_emprestimo / meses
print(meses)
data_atual = data_inicio

while data_atual < data_final:
    print(f'{data_atual.strftime('%d/%m/%Y')} R$ {valor_parcela:,.2f}')
    data_atual += relativedelta(months=1)

print('Você quitou a divida')
