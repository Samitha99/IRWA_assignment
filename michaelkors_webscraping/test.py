import requests
from bs4 import BeautifulSoup

try:
    soures = requests.get('https://www.michaelkors.com/sale/men/_/N-28au')
    soures.raise_for_status

    soup = BeautifulSoup(soures.text, 'html.parser')
    products = soup.find_all('li', class_="product-tile left small-6 medium-3")
    print(len(products))

    n = 1
    for product in products:
        productNumber = n
        productName = product.find('li', class_="product-name-container").a.text.strip()
        productPrice = product.find('div', class_="salePrice").find('span', class_="ada-link visually-hidden").text.strip()
        productOldPrice = product.find('div', class_="listPrice").find('span', class_="ada-link visually-hidden").text.strip()
        print(productNumber, productName, productPrice, productOldPrice)
        n+=1


except Exception as e:
    print(e)
    exit()