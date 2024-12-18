### File Handling ###

import os

# .txt file

txt_file = open('my_file.txt', 'r+') # Leer y escribir
#print(txt_file.read()) # Muestra por consola el contenido
#print(txt_file.read(10)) # Muestra los primeros 10 caracteres
#print(txt_file.readline()) # Muestra la primera línea
#print(txt_file.readlines()) # Muestra todas las líneas dentro de una lista


txt_file = open('my_file.txt', 'a') # Abre el archivo para agregar al final de todo
txt_file.write('\nAunque también me interesa Rust')

# .json