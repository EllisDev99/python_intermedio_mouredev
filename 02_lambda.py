### Lambdas o Funciones anónimas ###

# Simple
# Sumar dos números
sumar = lambda x, y: x + y
print(sumar(5, 5)) # 10

# Usando lambda con map
# Multiplicar cada elemento de una lista por 2
n = [1, 2, 3, 4]
resultado = list(map(lambda x: x * 2, n))
print(resultado) # [2, 4, 6, 8]

# Usando lambda con filter
# Filtrar números pares de una lista 
resultado2 = list(filter(lambda x: x % 2 == 0, n))
print(resultado2) # [2, 4]

# Usando lambda con sorted
# Ordenar una lista de tuplas por el segundo elemento
personas = [('Brayan', 25), ('Kevin', 22), ('Alicia', 17)]
resultado3 = sorted(personas, key=lambda x: x[1])
print(resultado3) # [('Alicia', 17), ('Kevin', 22), ('Brayan', 25)]

"""
* map: Aplica una función a cada elemento de un iterable (como una lista) y devuelve un nuevo iterable con los resultados.

* filter: Filtra los elementos de un iterable según una condición. Devuelve un nuevo iterable con los elementos que cumplen la condición.

* sorted: Ordena los elementos de un iterable. El argumento key especifica la función que se utilizará para determinar el orden.
"""