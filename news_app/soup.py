from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.nytimes.com/'
r = requests.get(URL)
soup = bs(r.text, 'html.parser')