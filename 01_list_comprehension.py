### List Comprehension ###
# Se útilizan principalmente cuando requieres hacer operaciónes a la vez que las generas, modificando su valor antes de guaradar

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
my_list = [i for i in range(7 + 1)]
my_range = range(8)

print(my_original_list)
print(my_list)
print(list(my_range))

my_list = [i ** 2 for i in range(11)] # Generamos una lista en donde cada n del rango será elevado a la potencia de 2
print(my_list)

def sum_five(n):
    return n + 5

my_list = [sum_five(i) for i in range(8)] # Se genera una lista en donde cada n del rango se le aplica sum_five
print(my_list)