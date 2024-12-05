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
