global sortedtoplist
import json
import requests
from natsort import humansorted
import sys

sys.path.insert(1, 'Modules')

with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()


def BestLogs():
    print("working")

    toplist = []
    sortedtoplist = []


    with open('Prices.json', 'r') as prices:
        data=prices.read()
        # parse file
    NPCPrices = json.loads(data)

    LogsToCheck = ["oak log", "dark oak log", "jungle log", "spruce log", "birch log", "acacia log"]
    #print("checking " + LogsToCheck)
    print("replied to a message, $merchantflip")
    for x in LogsToCheck:
        #print(x)
        Product = x
        NormalName = x
        Product = NPCPrices["productIds"][Product]["NormalName"] 
        #api request
        payload = {'key': ApiKey, "productId": Product}
        r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
        JSONData = (r.json())
        result = str(JSONData)

        sellPrice = JSONData["product_info"]['quick_status']['buyPrice']


        rSellPrice = round(sellPrice, 1)
        strSellPrice = str(rSellPrice)
        toplist.append("You can make " + strSellPrice + "$ per log if you sell " + NormalName + " to the bazaar.")

    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()


    return sortedtoplist

