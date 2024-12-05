"""
* Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
* - Url de ejemplo:
*   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
* - Por ratio hacemos referencia por ejemplo a los "16:9" de una
*   imagen de 1920*1080px.
"""
import requests
import tempfile
from PIL import Image

# Creamos la constante con la dirección y extraemos sus datos
URL = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
response = requests.get(URL)

# Si la conexión es correcta creamos un archivo temporal
if response:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(response.content) # Se escriben los datos de la img en el archivo temp
        img = Image.open(temp_file.name) # Se abre la imagen

        # Cáculamos el aspect ratio de la img y formateamos la salida
        aspect_ratio = img.size[0] / img.size[1]
        aspect_ratio_format = str(aspect_ratio).replace('.', ':')

        # Imprimimos por pantalla los datos
        print('='*40)
        print(f'Tamaño de la imagen: {img.size}')
        print(f'Aspect Ratio: {aspect_ratio_format}')
        print('='*40)
else:
    # Si la conexión falla salta una excepción con su estatus
    raise Exception(f'Non-success status code: {response.status_code}')