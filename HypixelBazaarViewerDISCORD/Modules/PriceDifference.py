global sortedtoplist
import json
import requests
from natsort import humansorted
import sys

sys.path.insert(1, 'Modules')

with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()

with open('Prices.json', 'r') as prices:
    data=prices.read()
    # parse file
NPCPrices = json.loads(data)

def PriceDifference():
    toplist = []
    print(ApiKey)   
         
    for x in (NPCPrices["productIds"]):          
        Product = x
       
        readableName = Product
        Product = (NPCPrices["productIds"][Product]["NormalName"])

        #BAZAAR PRICES
        #getting the data
        payload = {'key': ApiKey, "productId": Product}
        r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
        JSONData = (r.json())
        result = str(JSONData)
        #get the prices
        sellPrice = JSONData["product_info"]['quick_status']['buyPrice']
        buyPrice = JSONData['product_info']['quick_status']['sellPrice']
        #round up the prices
        rSellPrice = round(sellPrice, 2)
        rBuyPrice = round(buyPrice, 2)
        #make the prices to string
        frSellPrice = str(rSellPrice)  # float -> str
        frBuyPrice = str(rBuyPrice)  # float -> str
        #how big is the absolut difference?
        AbsoluteDifference = buyPrice - sellPrice
        rAbsoluteDifference = round(AbsoluteDifference, 2)
        strAbsoluteDifference = str(rAbsoluteDifference)
        #whats the average between the two numbers?
        AverageDifference = (sellPrice + buyPrice)/2   
        #Divide the difference by the average:
        Difference = (AbsoluteDifference / AverageDifference)*100
        rDifference = round(Difference, 1)
        strDifference = str(rDifference)
        #storing the difference and the product
        if Difference > 0:
            #add the value to a list
            toplist.append("There is a " + strDifference + "% difference between the sell and buy price of " + readableName + ", or " + strAbsoluteDifference + "$.")      


    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
