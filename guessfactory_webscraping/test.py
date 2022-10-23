import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    soures = requests.get('https://www.guessfactory.com/us/en/sale/women/view-all')
    soures.raise_for_status

    soup = BeautifulSoup(soures.text, 'html.parser')
    products = soup.select('row product-grid ')
    print(products)

except Exception as e:
    print(e)
    exit()