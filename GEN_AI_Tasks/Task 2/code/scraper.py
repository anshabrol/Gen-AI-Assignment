import requests
from bs4 import BeautifulSoup

import requests
import random

def fetch_trending_product():
    """
    Fetches a random product from a public e-commerce API
    (FakeStore API – scraping-safe)
    """

    url = "https://fakestoreapi.com/products"
    response = requests.get(url, timeout=10)

    products = response.json()

    if not products:
        raise Exception("No products found")

    product = random.choice(products)

    return {
        "name": product["title"],
        "category": product["category"],
        "description": product["description"]
    }
