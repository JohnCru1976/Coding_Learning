import bs4  # Beautifulsoap
import requests 

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

codigo = resultado.text

sopa = bs4.BeautifulSoup(codigo,"lxml")

titulo = sopa.select("title")[0].get_text()

clase = sopa.select(".sidebar-container div li .label-name")  # Esta es una utilidad de beatifulsoap

for elemento in clase:
    separador = " " + "-" * (25 - len(elemento.get_text())) + "> "
    print(elemento.get_text(), elemento.get_attribute_list("href")[0], sep=separador)
