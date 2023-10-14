import bs4  # Beautifulsoap
import requests 
import os
from pathlib import Path

## FUNCIÓN PARA LA DESCARGA DE ENLACES DE FOTOS
def descarga_foto(link):
    request_foto = requests.get(link)
    image_name = ""
    extension = ""
    if request_foto.status_code == 200:
        # Obtiene el nombre del archivo desde la URL
        image_name = os.path.basename(link)
        extension = Path(link).suffix

    # Especifica la ubicación donde deseas guardar la imagen
    save_path = "C:\\Users\\juanb\\OneDrive\\Escritorio\\Prueba\\" + image_name

    # Abre el archivo en modo binario y escribe los datos de la imagen
    if extension != ".svg":
        with open(save_path, 'wb') as file:
            file.write(request_foto.content)  # El content se devuelve en binario

## PRUEBAS

resultado = requests.get("https://blog.hootsuite.com/es/20-paginas-de-fotos-gratuitas/")

sopa = bs4.BeautifulSoup(resultado.text,"lxml")

imagenes = sopa.select("img")

for imagen in imagenes:
    #src = imagen.get("src")  # Forma 1 de hacerlo
    src = imagen['src']       # Forma 2 de hacerlo
    print(src)
    descarga_foto(src)
