import requests
from bs4 import BeautifulSoup
import openpyxl
import urllib.request
from urllib.request import Request, urlopen


try:
    req = Request(
        url='https://www.guessfactory.com/us/en/sale/women/view-all', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    # print(webpage)
    soup = BeautifulSoup(webpage, 'html.parser')
    # print(soup)
    products = soup.find_all('div', class_="product-grid__column")
    # print(len(products))

    n = 1
    for product in products:
        pNumber = n
        productName = product.find('h3', class_="pdp-link product-tile__pdp-link h3-pdp").a.text.strip()
        productPrice = product.find('span', class_="price__red-color text-nowrap").text.strip().replace('now ', '')
        n+=1
        
        print(productPrice)
        break

except urllib.error.HTTPError as e:
    body = e.read().decode() 