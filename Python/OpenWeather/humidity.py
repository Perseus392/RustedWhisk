import sys
import requests

def main(args):
    city = 'Delhi'
    apikey = '4f9243cae71d455b452f3e84f50be078'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city, apikey)
    res = requests.get(url)
    data = res.json()
    humidity= data['main']['humidity']
    hum ='{}'.format(humidity)
    return {"humidity": hum }