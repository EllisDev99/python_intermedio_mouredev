### Funciones de orden superior ###
### Higher Order Functions ###

from functools import reduce

"""En pocas palabras una función de orden superior es aquella que puede hacer cosas con
otras funciones"""

def sum_one(value):
    """Suma 1 al valor dado.

    Args:
        value: El valor al que se le sumará 1.

    Returns:
        El resultado de la suma.
    """
    return value + 1


def sum_five(value):
    """Suma 1 al valor dado.

    Args:
        value: El valor al que se le sumará 1.

    Returns:
        El resultado de la suma.
    """
    return value + 5


def sum_two_values_and_value(first_value, second_value, f_sum):
    """Suma dos valores y luego aplica una función de suma.

    Args:
        first_value: El primer valor a sumar.
        second_value: El segundo valor a sumar.
        f_sum: Una función que toma un valor y devuelve el resultado de una suma.

    Returns:
        El resultado de aplicar la función f_sum a la suma de los dos valores.
    """
    return f_sum(first_value + second_value)



print(sum_two_values_and_value(5, 2, sum_one))
print(sum_two_values_and_value(5, 2, sum_five))

### Closures ###
"""
Un closure es una función interna que tiene acceso a las variables locales de la 
función externa, incluso después de que la función externa haya 
terminado de ejecutarse.
"""

def sum_ten():
    """Crea una función que suma 10 a un valor dado.

    Esta función utiliza un closure para recordar el valor 10, incluso después de que
    la función externa haya terminado de ejecutarse.

    Returns:
        Una función que toma un valor y le suma 10.
    """
    def add(value):
        return value + 10
    return add


add_closures = sum_ten()
print(add_closures(5))
######################


def sum_ten_2(original_value):
    """Crea una función que suma un valor dado a 10 y a un valor original.

    Esta función utiliza un closure para recordar el valor original, incluso después de 
    que la función externa haya terminado de ejecutarse. El valor original se suma al 
    resultado de la suma entre el valor pasado como argumento y 10.

    Args:
        original_value: El valor original que se sumará al resultado final.

    Returns:
        Una función que toma un valor y le suma 10 y el valor original.
    """
    def add(value):
        return value + 10 + original_value
    return add


add_closures_2 = sum_ten_2(1)
print(add_closures(5))
######################

print(sum_ten_2(5)(2))


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
    return number * 2

def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

# Map
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
"""
La función reduce() es una herramienta poderosa en Python que te permite aplicar una 
función a una secuencia (como una lista, tupla o cualquier otro iterable) y reducirla a 
un único valor. Es decir, toma múltiples elementos y los combina de forma iterativa para 
obtener un resultado final.
"""
print(reduce(sum_two_values, numbers))
print(f"El resultado de la reducción es: {reduce(lambda x, y: x + y, numbers)}")