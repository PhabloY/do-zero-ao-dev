# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2025, 2, 5, 13, 11, 59)
data = datetime.strptime('2025-02-05 13:14:59', '%Y-%m-%d %H:%M:%S')

print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
