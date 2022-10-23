from email.mime import image
import openpyxl
import requests
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
# print(excel.sheetnames)
# create a new sheet
sheet = excel.active
sheet.title = 'IMDB Top 250 Moveis'
# add column names
sheet.append(['Rank', 'Movie Name', 'Released Year', 'IMDB Rating'])

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    
    for movie in movies:
        name = movie.find('td', class_='titleColumn').a.text

        #strip=true means remove all the white spaces
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        
        # //////////////////////////////////
        # method 1 for get year
        # year = movie.find('td', class_='titleColumn').span.text.replace('(','').replace(')','')
        # year = year.replace('(','').replace(')','')

        # method 2 for get year
        # strip can be used for remove something from the string
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        # find image to jpg
        img = movie.find('td', class_='posterColumn').a.img['src']

        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text

        #print all values
        print(img)
        
        #insert data into excel
        sheet.append([rank, name, year, rating])
        break
except Exception as e:
    print(e)
    exit()

#save the excel file
# excel.save('IMDB Top 250 Moveis.xlsx')