import sys
import requests

def main(args):
    city = 'Delhi'
    apikey = args.key
    url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city, apikey)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    celsius = temp -273.15 
    temp = '{}\N{DEGREE SIGN}C'.format(celsius)
    return {"Temperature" : temp}
