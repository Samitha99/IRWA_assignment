from urllib.request import Request, urlopen



req = Request(
    url='https://www.guessfactory.com/us/en/sale/women/view-all',
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'lxml')