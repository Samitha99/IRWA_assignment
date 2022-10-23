# using urllib

# from urllib.request import urlopen 

# html = urlopen('https://www.imdb.com/chart/top/')
# print(html.read())

from urllib import response
import requests
from bs4 import BeautifulSoup

try:
    response = requests.get('https://www.imdb.com/chart/top3245245/')
    response.raise_for_status()
    print(response.text)

except Exception as e:
    print(e)
    exit()