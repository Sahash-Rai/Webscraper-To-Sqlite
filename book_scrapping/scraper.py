import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

def fetch_page(url):
    response = requests.get(url)
    return response.text

def scrape_books():
    url = BASE_URL
    html = fetch_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    books = []
    book_items = soup.select("article.product_pod")
    
    for item in book_items:
        title = item.select_one("h3 a")["title"]
        price = item.select_one("p.price_color").text
        link = BASE_URL + item.select_one("h3 a")["href"]
        
        books.append({"title": title, "price": price, "url": link})
    
    return books
