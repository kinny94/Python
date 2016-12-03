import requests
from bs4 import *
data = requests.get("http://www.accuweather.com/en/us/san-jose-ca/95110/weather-forecast/347630")
soup = BeautifulSoup(data.text, "html.parser")
data2 = soup.find('div', {'class':'info'})
data3 = data2.find('strong', {'class':'temp'})
data3.content[0]