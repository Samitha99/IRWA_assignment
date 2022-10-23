import requests
from bs4 import BeautifulSoup

soures = requests.get('https://www.michaelkors.com/sale/men/_/N-28au')
soures.raise_for_status
print(soures)
