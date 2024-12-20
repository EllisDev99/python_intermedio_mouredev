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

"""
 Busca una coincidencia solo al principio de la cadena. Si el patrón no coincide con el 
 inicio de la cadena, re.match() devuelve None.
"""
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

"""
 Busca una coincidencia en cualquier parte de la cadena. Si el patrón se encuentra en 
 cualquier posición dentro de la cadena, re.search() devuelve un objeto de coincidencia; 
 de lo contrario, devuelve None.
"""

search = re.search('lección', my_string, re.I)
print(search)

start, end = search.span()
print(my_string[start:end])

footer()


# findall
title('findall')

"""
Encuentra todas las coincidencias no superpuestas de un patrón en una cadena y las 
devuelve como una lista de cadenas.

re.findall(patron, cadena, flags=0)

patron: La expresión regular que se va a buscar.
cadena: La cadena en la que se realiza la búsqueda.
flags: Flags opcionales que modifican el comportamiento de la búsqueda (ej. re.I para 
ignorar mayúsculas/minúsculas).
"""

findall = re.findall('lección', my_string, re.I)
print(findall)

footer()

# split
title('split')

"""
Divide una cadena en subcadenas usando un patrón como delimitador. Devuelve una lista de 
las subcadenas.

re.split(patron, cadena, maxsplit=0, flags=0)

patron: La expresión regular que se utiliza como delimitador.
cadena: La cadena que se va a dividir.
maxsplit: Un entero opcional que especifica el número máximo de divisiones. Si es 0 (el 
valor predeterminado), se realizan todas las divisiones posibles.
flags: Flags opcionales.
"""

print(re.split(':',my_string))

footer()

# sub
title('sub')

"""
Reemplaza todas las ocurrencias de un patrón en una cadena con una cadena de reemplazo.

re.sub(patron, reemplazo, cadena, count=0, flags=0)

patron: La expresión regular que se va a buscar.
reemplazo: La cadena con la que se van a reemplazar las coincidencias.
cadena: La cadena en la que se realiza el reemplazo.
count: Un entero opcional que especifica el número máximo de reemplazos. Si es 0 (el 
valor predeterminado), se reemplazan todas las ocurrencias.
flags: Flags opcionales.
"""

print(re.sub('6', 'VI', my_string))
print(re.sub('lección|Lección', 'clase', my_string))

footer()


# Patterns
title('Patrones')

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.search(pattern, my_string))

# r'[\d]' Toma en cuenta solo los digitos
# r'[\D]' Toma en cuenta solo las letras

pattern = r'[l].'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

email_1 = 'emailtest@gmail.com'
email_2 = 'emailtest2024@gmail.com'
email_3 = 'emailtest2024@outlock.com'
email_4 = 'emailtest2024@proton.me'

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

print(re.match(pattern, email_1))
print(re.match(pattern, email_2))
print(re.match(pattern, email_3))
print(re.match(pattern, email_4))

footer()