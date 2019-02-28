import requests
import bs4
x = 1

while x == 1:
    coin_name = str(input('what currency would you like the latest price of?'))
    coin_call = coin_name.upper()	

    res = requests.get('https://coinmarketcap.com/currencies/'+coin_name.lower())
    soup = bs4.BeautifulSoup(res.text,'lxml')
    soup.select('#quote_price, .h2, .text-grey')
    for item in soup.select('#quote_price,.h2, .text-grey'):
	#print(coin_name +' Current Price:')
            print(item.text)
    
