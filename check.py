import requests
from bs4 import BeautifulSoup
import os
import requests

URL = os.getenv("https://store.steampowered.com/sale/steamdeckrefurbished/")
KEYWORD = "Nicht vorrätig"

html = requests.get(URL).text
if KEYWORD not in html:
    requests.post(os.getenv("WEBHOOK_URL"), json={"content": "Produkt ist wieder verfügbar!"})
