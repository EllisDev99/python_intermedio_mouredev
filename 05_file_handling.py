### File Handling ###

import os

# .txt file

txt_file = open('my_file.txt', 'r+') # Leer y escribir
#print(txt_file.read()) # Muestra por consola el contenido
#print(txt_file.read(10)) # Muestra los primeros 10 caracteres
#print(txt_file.readline()) # Muestra la primera línea
#print(txt_file.readlines()) # Muestra todas las líneas dentro de una lista

txt_file = open('my_file.txt', 'a') # Abre el archivo para agregar al final de todo
#txt_file.write('\nAunque también me interesa Rust')


# .json file

import json

json_file = open('my_file.json', 'w+')

json_test = {
    'name':'Brayan',
    'subname':'Medina',
    'age':25,
    'languages':['Python', 'Rust', 'Kotlin'],
    'email':'emailtest_1@gmail.com'
}

json.dump(json_test, json_file, indent = 4)

json_file.close()


json_dict = json.load(open('my_file.json'))
print(type(json_dict))
print(json_dict)
print(json_dict['languages'])