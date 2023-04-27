from pprint import pprint

import requests
from bs4 import BeautifulSoup

from constants import URL
from utils import get_all_categories, get_pages_url_from_books, parse_html, save_to_csv_file


def scrap_books_data() : 
# Récupèration de l'ensemble des informations des livres dans une liste de dictionnaires
    list_books = []

    categories_names = get_all_categories()

    for category in categories_names :
        if category == "Travel":
            url_books = get_pages_url_from_books(categories_names.get(category))
            pprint(f"Catégorie en cours... : {category}")
            for url_book in url_books :
                response = requests.get(url_book)
                soup = parse_html(response)
                list_books.append({
                    "category": category,
                    "title": scrap_book_title(soup),
                    "picture": scrap_book_url_picture(soup),
                    "description": scrap_book_description(soup),
                    "price": scrap_book_price(soup),
                })
        else:
            break
    save_to_csv_file(list_books)

def scrap_book_title(soup: BeautifulSoup) -> str :
# Extraction du titre d'un livre
    h1 = soup.find("div", class_="product_main").find("h1")
    return h1.text

def scrap_book_url_picture(soup: BeautifulSoup) -> str :
# Extraction de l'url de l'image d'un livre
    img_url = soup.find("div", id="product_gallery").find("img")["src"]
    return img_url.replace("../..", URL)

def scrap_book_description(soup: BeautifulSoup) -> str :
# Extraction de la description d'un livre
    p = soup.find("div", id="product_description").find_next("p")
    return p.text
    
def scrap_book_price(soup: BeautifulSoup) -> str :
# Extraction du prix d'un livre
    p = soup.find("div", class_="product_main").find("p", class_="price_color")
    return p.text.replace("£", "")
    
scrap_books_data()