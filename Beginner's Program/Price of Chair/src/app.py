__author__ = 'Arjun'

import requests
from bs4 import BeautifulSoup

requests = requests.get("http://www.johnlewis.com/west-elm-saddle-dining-chair-crosshatch-steel/p2139360")
content = requests.content  # to get the html content
soup = BeautifulSoup(content, "html.parser")    # parse the html content
element = soup.find("span", {"itemprop": "price", "class": "now-price"})

string_price = element.text.strip()

priceWithoutSymbol = string_price[1:]
price = float(priceWithoutSymbol)

if price < 200:
    print("Buy the chair!!")
    print("The current price is {}.".format(price))
else:
    print ("Its expensive for you!")
    print("The current price is {}.".format(price))


