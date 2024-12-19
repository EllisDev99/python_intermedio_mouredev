### Regular Expressions ###
import re

def title(title):
    print()
    print(f"{f'  {title.upper()}  ':=^70}")

def footer():
    print('_' * 70)


# match
title('match')

my_string = 'Esta es la lección número 6: \nLección llamada Expresiones regulares'
my_other_string = 'Esta no es la lección número 6: Manejo de ficheros'

# re.match busca el patrón al principio de la cadena, en caso de no estar retorna None
# re.I hace que la busqueda ingnore entre mayúsculas y minúsculas
match = re.match('Esta es la lección', my_string, re.I)
print(match) # Imprime un objecto de coincidencia

# match.span() Este método devuelve una tupla que contiene el índice de inicio y el índice de fin de la coincidencia encontrada.
start, end = match.span()
print(my_string[start:end])

match = re.match('Esta no es la lección', my_other_string)
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

footer()


# search
title('search')

search = re.search('lección', my_string, re.I)
print(search)

start, end = search.span()
print(my_string[start:end])

footer()


# findall
title('findall')


findall = re.findall('lección', my_string, re.I)
print(findall)

footer()

# split
title('split')

print(re.split(':',my_string))

footer()

# sub
title('sub')

print(re.sub('6', 'VI', my_string))
print(re.sub('lección|Lección', 'clase', my_string))

footer()