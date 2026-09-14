import requests
from bs4 import BeautifulSoup

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    results = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        results.append({"title": title, "price": price})

    return results

def fetch_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # raises an error if status isn't 200
    return response.text

if __name__ == "__main__":
    html = fetch_page("https://books.toscrape.com")    
    print(html[:500])  # print first 500 characters to check it worked
    books = parse_books(html)
    for b in books:
        print(b)
