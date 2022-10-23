import requests
from bs4 import BeautifulSoup
import openpyxl
import urllib.request
from urllib.request import Request, urlopen

excel = openpyxl.Workbook()
excelSheet = excel.active
excelSheet.append(["Product Number" ,"Product Name" ,"New Price" ,"Old Price"])

try:
    req = Request(
        url='https://www.michaelkors.com/sale/men/_/N-28au', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    # print(webpage)
    soup = BeautifulSoup(webpage, 'html.parser')
    # print(soup)
    products = soup.find_all('li', class_="product-tile left small-6 medium-3")
    # print(len(products))

    n = 1
    for product in products:
        productNumber = n
        productName = product.find('li', class_="product-name-container").a.text.strip()
        productPrice = product.find('div', class_="salePrice").find('span', class_="ada-link visually-hidden").text.strip()
        productOldPrice = product.find('div', class_="listPrice").find('span', class_="ada-link visually-hidden").text.strip()
        excelSheet.append([productNumber ,productName ,productPrice ,productOldPrice ])
        n+=1
        
except urllib.error.HTTPError as e:
    body = e.read().decode() 

excel.save(filename = 'Product Detail.xlsx')