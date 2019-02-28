import requests
import bs4
def coin_name():
        coin_name == str(input('what currency would you like the latest price of?'))

coin_call = coin_name	
res = requests.get('https://coinmarketcap.com/currencies/'+ str(coin_name))
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('#quote_price')
for item in soup.select('#quote_price'):
        print(coin_call.upper() +' Current Price:')
        print(item.text)
   
while coin_name == False:
        print('please pice a diffrent coin or check spelling')
