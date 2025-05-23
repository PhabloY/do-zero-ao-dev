# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
# from pytz import timezone

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1738700251.161277))
# data_str = '2025/02/04 13:26:39'
# data_str = '04/02/2025'
# data_str_fmt = '%d/%m/%Y'
# data = datetime(2025, 2, 4, 17, 14, 39, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str, data_str_fmt)
