import requests
import re
import openpyxl
from bs4 import BeautifulSoup

# excel = openpyxl.Workbook()
# excelS = excel.active
# excelS.append(["Product Number" ,"Product Name" ,"New Price" ,"Old Price" ,"discount" ])

try:
  soures = requests.get('https://odel.lk/deal-products')
  soures.raise_for_status

  soup = BeautifulSoup(soures.text, 'html.parser')
  print(soup)
  products = soup.find_all('div', class_="col-sm-6 col-md-4 col-lg-3 p-b-35 product-tile-search")
#   print(products)
  num = 1
  for product in products:
    productNumber = num
    name = product.find("div", class_="block2-txt-child1 flex-col-l").a.text.strip()
    price = product.find("span", class_="stext-105 cl3").text.strip().replace('LKR ', '')
    oldPrice = product.find("del").text.strip().replace('LKR ', '')
    discount = product.find("div", class_="product_tag_discount").text
    num = num + 1
    # excelS.append([productNumber ,name ,price ,oldPrice ,discount ])
    


except Exception as e:
  print(e)
  exit()

# excel.save(filename = 'Product Detailsv1.xlsx')