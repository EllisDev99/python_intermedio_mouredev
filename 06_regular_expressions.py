### Regular Expressions ###
import re

# match

my_string = 'Esta es la lección número 6: sobre Expresiones regulares'
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


# search
search = re.search('Esta es la lección', my_string, re.I)
print(search)