from pprint import pprint
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from constants import URL

def _get_pages_url_from_category(category: str) -> list: 
# Récupération des urls des pages d'une catégorie
    pprint("Etape 2 : Récupèration des URL des pages catégorie")
    page = 1
    list_pages_url = []

    while True:
        if page == 1:
            page_url = f"{URL}/catalogue/category/books/{category}/index.html"
        else:
            page_url = f"{URL}/catalogue/category/books/{category}/page-{page}.html"

        page += 1

        response = requests.get(page_url)  
        if response.status_code == 200 : 
            list_pages_url.append(page_url)
        else : 
            break
    
    return list_pages_url

def get_pages_url_from_books(category: str) -> list:
# Récupération des urls des pages des livres
    list_url = _get_pages_url_from_category(category)
    list_pages_url = []
    pprint("Etape 3 : Récupèration des urls des pages des livres")
    for url in list_url:
        response = requests.get(url)
        soup = parse_html(response)
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            link = book.find('a')['href']
            link_clean = link.replace("../../../", f"{URL}/catalogue/")
            list_pages_url.append(link_clean)

    return list_pages_url
              
def parse_html(url: requests) -> BeautifulSoup:
    html = url.content
    return BeautifulSoup(html, "html.parser")
    
def get_all_categories() -> list:
# Récupération de toutes les catégories
    pprint("Etape 1 récupération de toutes les catégories")
    categories_names = {}
    response = requests.get(URL)
    soup = parse_html(response)
    categories = soup.find("div", class_="side_categories")
    li_elements = categories.find_all("li")
    li_elements.pop(0)

    for li in li_elements :
        href = li.find("a")["href"]
        category_url_name = href.replace("catalogue/category/books/", "").replace("/index.html", "")
        category_name = li.text.strip(" \n") 
        categories_names[category_name] = category_url_name

    return categories_names

def convert_book_data_to_csv(list_books: list[dict]) -> str:
# Convertion de la liste de dictionnaire de livres en ligne de caractère csv
    pprint("Etape 4 : Convertion de la liste de dictionnaire de livres en ligne de caractère csv")
    lines = ["Catégorie,Titre,Image,Description,Prix"]

    for book in list_books:
        lines.append(",".join([
            book["category"],
            book["title"],
            book["picture"],
            book["description"],
            book["price"]
        ]))
    
    return "\n".join(lines)

def save_to_csv_file(list_books: list[dict]) -> bool:
# Sauvegarde du fichier csv
    category_name = list_books[0]["category"]
    folder_path = Path("data") / category_name
 
    folder_path.mkdir(parents=True, exist_ok=True)
    file_path = folder_path / f"{category_name}.csv"
    
    with open(file_path, "w") as f:
        f.write(convert_book_data_to_csv(list_books))
    pprint("Etape 5 : Sauvegarde du fichier csv")
    return True