import sys
import requests

def main(args):
    city = 'Delhi'
    apikey = args.key
    url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city, apikey)
    res = requests.get(url)
    data = res.json()
    pressure= data['main']['pressure']
    return {"Pressure": pressure}
