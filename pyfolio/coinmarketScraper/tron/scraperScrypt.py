import requests
import bs4

res = requests.get('https://coinmarketcap.com/currencies/{}/'.format(input))
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('#quote_price')
for item in soup.select('#quote_price'):
    print('Tron/TRX Current Price:')
    print(item.text)
    
