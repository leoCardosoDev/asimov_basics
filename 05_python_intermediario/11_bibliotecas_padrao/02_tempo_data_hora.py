# Trabalahando com tempo, datas e horas

import datetime
data = datetime.date(2024, 7, 11)
print(data)
hora = datetime.time(17, 6, 55)
print(hora)
full_date_hora = datetime.datetime(2024, 7, 11, 17, 8, 55)
print(full_date_hora)
print(full_date_hora.strftime('Dia %d/%M/%Y, %H:%m:%S'))
print(full_date_hora.strftime('[%Y-%m-%d --- %H:%M:%S]'))
texto = '2024-07-11T08:45:30'
data2 = datetime.datetime.strptime(texto, '%Y-%m-%dT%H:%M:%S')
print(data2)