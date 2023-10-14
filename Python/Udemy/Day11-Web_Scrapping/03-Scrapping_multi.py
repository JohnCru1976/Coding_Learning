''' This is an exercise where I try to do scrapping from https://books.toscrape.com/catalogue/page-1.html
This is part of a course from Udemy with the instructor Federico Garay
Goal: to extract the book titles starred with 4 or more stars.

class="product_pod"  -> Class containing the elements
<p class="star-rating One">   -> Number of stars
<a href="tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a>   -> Title 
'''
from os import system
import bs4  # Beautifulsoap
import requests

def get_soap(page_number):
    '''Obtener el soap de cada página'''
    link = f"https://books.toscrape.com/catalogue/page-{page_number}.html"

    response = requests.get(link)
    general_scrapping = None

    if response.status_code == 200:
        general_scrapping = bs4.BeautifulSoup(response.text,"lxml")
    
    return general_scrapping

def scrapping_title_stars(soap):
    books = []
    final_list = []
    if soap is not None:
        books = soap.select(".product_pod")
        for book in books:
            try:
                stars = book.find(lambda tag: tag.name == "p" and tag.get("class","star-rating"))['class'][1]  # type: ignore
                title = book.find(lambda tag: tag.name == "a" and tag.get("title", ""))['title'] # type: ignore
                link = book.find(lambda tag: tag.name == "a" and tag.get("title", ""))['href'] # type: ignore
                if stars == "Four" or stars == "Five":
                    final_list.append((stars, title, link))
            except:
                pass
    return final_list

def lista_final(num_pags):
    lista_return = []
    total = 0
    for num_pag in range(1,num_pags + 1):
        lista = scrapping_title_stars(get_soap(num_pag))
        print(f"Scrapping page {num_pag}")
        for libro in lista:
            lista_return.append(libro)
        print(f"Books found in page {num_pag}: {len(lista)}")
        total += len(lista)
        print(f"Total number of books: {total}")
    return lista_return

if __name__ == "__main__":
    listado = lista_final(50)
    system('cls')
    print(f"LIBROS ENCONTRADOS: {len(listado)}\n")
    n = 0
    for libro in listado:
        n += 1
        print(f"{n} - Título: {libro[1]}")
        if libro[0] == "Four":
            print("\t4 estrellas")
        if libro[0] == "Five":
            print("\t5 estrellas")
        print(f"\tLink: https://books.toscrape.com/catalogue/{libro[2]}")
