import requests
import bs4


#class CoinScrape():
#        def __init__(self,coin_name):
#                self.coin_name = coin_name
coin_name = str(input('what currency would you like the latest price of?'))
coin_call = coin_name.upper()	

res = requests.get('https://coinmarketcap.com/currencies/'+coin_name.lower())
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('#quote_price')
for item in soup.select('#quote_price'):
	print(coin_name +' Current Price:')
	print(item.text)
    
