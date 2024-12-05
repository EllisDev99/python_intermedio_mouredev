### Dates ###

import datetime

now = datetime.datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


timestamp = now.timestamp()
""" Los timestamp son una secuencia de caracteres que representan una fecha y hora específica en la que ocurrio 
un evento"""
print(timestamp)


### Crear fechas
# .
end_year_2024 = datetime.datetime(2024, 12, 31)
# --------------------------------------------

print_date(end_year_2024)
print_date(now)


### Utilizando el módulo time de datetime
# .
current_time = datetime.time(15, 44, 10)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
# --------------------------------------------


### Utilizando el módulo date de datetime
# .
current_date = datetime.date.today() # con today se toma la fecha actual del sistema
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = datetime.date(2024, 4, 23) # estamos indicando nosotros la fecha
print(current_date.year)
print(current_date.month)
print(current_date.day)
# --------------------------------------------


### Modificar fechas
#.
current_date = datetime.date(current_date.year + 20, current_date.month + 2, current_date.day)
print(current_date)

diff = end_year_2024 - now # restando 2024-12-31 a la fecha actual
print(diff)

diff = current_date - end_year_2024.date() # Mientras sean del mismo tipo se pueden hacer operaciones con ellos
# estamos pasando el end_year_2024 de datetime a date
print(diff)
# --------------------------------------------


### Timedelta
#.
from datetime import timedelta

init_time_delta = timedelta(200, 100, 100, weeks=10)
end_time_delta = timedelta(300, 100, 100, weeks=13)
print(end_time_delta - init_time_delta)
