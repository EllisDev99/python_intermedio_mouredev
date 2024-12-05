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