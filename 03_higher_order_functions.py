### Funciones de orden superior ###
### Higher Order Functions ###

"""En pocas palabras una función de orden superior es aquella que puede hacer cosas con
otras funciones"""

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_value(5, 2, sum_one))
print(sum_two_values_and_value(5, 2, sum_five))

from functools import reduce

### Closures ###
"""
Función que define a una función y retorna una función
"""

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closures = sum_ten()

print(add_closures(5))


def sum_ten_2(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closures_2 = sum_ten_2(1)

print(add_closures(5))


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

print(reduce(sum_two_values, numbers))