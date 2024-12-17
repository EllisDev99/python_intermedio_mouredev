### Error Types ###

# SyntaxError
#print('Hola' # Descomentar para error
print('¡Hola undo!')

# NameError
language = 'Spanish' # Comentar para error
print(language)

# IndexError
my_list = ['Python', 'Rust', 'Kotlin']
#print(my_list[4]) # Descomentar para error

# ModuleNotFoundError
#import maths # Descomentar para error
import math

# AttributeError
#print(math.PI) # Descomentar para error
print(math.pi)

# KeyError
my_dict = {
    'Nombre':'Brayan',
    'Apellido':'Medina',
    'Edad':25,
}
print(my_dict['Edad'])
#print(my_dict['Nombr']) # Descomentar para error
print(my_dict['Nombre'])

# TypeError
#print(my_list['Rust']) # Descomentar para error

# ImportError
#from math import PI # Descomentar para error
from math import pi

# ValueError
my_int = int('10')
my_int2 = int('10 años')
#print(type(my_int2)) # Descomentar para error

# ZeroDivisionError
# No se puede dividir entre 0
