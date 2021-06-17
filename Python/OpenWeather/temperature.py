import sys
import requests
from pprint import pprint
city = 'Delhi'
apikey = '4f9243cae71d455b452f3e84f50be078'
url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city, apikey)
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
celsius = temp -273.15 
pprint('Temperature: {}\N{DEGREE SIGN}C'.format(celsius))