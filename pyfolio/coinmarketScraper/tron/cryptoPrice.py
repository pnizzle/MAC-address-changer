import requests
import bs4

def coin_call():
    coin_call.lower == coin_name

def coin_name():
        coin_name=self.coin_name
#    coin_name = coin_call.lower
#class Crypto_price():
#   def __init__(self,coin_name):
#      self.coin_name = coin_name
        
res = requests.get('https://coinmarketcap.com/currencies/'+ str(coin_name))
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup.select('div > span'))
for item in soup.select('#data-format-price-crypto'):
    print('crypto currency price:')
    print(item.text)


