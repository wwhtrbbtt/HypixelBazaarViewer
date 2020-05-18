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




