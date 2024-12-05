"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

def area(poligono):
    print('='*40)
    print(f"{poligono['nombre'].upper():^40}")
    print('-'*40)

    if poligono['nombre'].upper() == 'TRIANGULO':
        return f"El área es: {(poligono['base'] * poligono['altura']) / 2}"

    if poligono['nombre'].upper() == 'CUADRADO':
        return f"El área es: {poligono['lados'] ** 2}"

    if poligono['nombre'].upper() == 'RECTANGULO':
        return f'El área es: {poligono["base"] * poligono["altura"]}'


fig1 = {'nombre': 'triangulo', 'base':20, 'altura':15}
fig2 = {'nombre': 'cuadrado', 'lados':20}
fig3 = {'nombre': 'rectangulo', 'base':20, 'altura':15}

print(area(fig1))
print(area(fig2))
print(area(fig3))