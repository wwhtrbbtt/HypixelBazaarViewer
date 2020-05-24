import requests
from natsort import humansorted
import sys
import json

sys.path.insert(1, 'Modules')

#APIKEY


def NPCPrices():
        with open('Prices.json', 'r') as prices:
            data=prices.read()
            # parse file
        NPCPrices = json.loads(data)
        return NPCPrices

def Request(Product):           
        file = open('ItemsToAdd.txt', 'a')
        file.write("You have to add: " + Product + ".")
        file.write("\n")
        file.close()
def JSONData():
    r = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/')
    JSONData = (r.json())
    return JSONData
    
def percent(a, b) : 
  
    result = int(((b - a) * 100) / a) 
  
    return result 
    
def NormalName(Product):
    with open('Prices.json', 'r') as prices:
            data=prices.read()
            # parse file
    NPCPrices = json.loads(data)
    try:
        NormalName = NPCPrices["productIds"][Product]["NormalName"]
        return NormalName
    except:
        return "error"

def PrettyNumbers(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


