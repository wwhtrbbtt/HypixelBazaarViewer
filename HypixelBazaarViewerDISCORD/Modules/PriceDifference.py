global sortedtoplist
import json
import requests
from natsort import humansorted
import sys
from SmallDefs import *

sys.path.insert(1, 'Modules')

NPCPrices = NPCPrices()

def PriceDifference():
    JSON = JSONData()
    toplist = []
         
    for x in (NPCPrices["productIds"]):          
        Product = x
       
        readableName = Product
        Product = (NPCPrices["productIds"][Product]["NormalName"])

        #BAZAAR PRICES
        buyPrice = JSON[Product]['quick_status']['buyPrice']
        sellPrice = JSON[Product]['quick_status']['sellPrice']
        buyVolume = JSON[Product]['quick_status']['buyVolume']
        sellVolume = JSON[Product]['quick_status']['sellVolume']
        #round up the prices
        rSellPrice = round(sellPrice, 2)
        rBuyPrice = round(buyPrice, 2)
        #make the prices to string
        frSellPrice = str(rSellPrice)  # float -> str
        frBuyPrice = str(rBuyPrice)  # float -> str

        #how big is the absolut difference?
        Increase = buyPrice - sellPrice

        
        rIncrease = round(Increase, 2)
        strIncrease = str(rIncrease) # 1

        #%difference

        Difference = percent(sellPrice, buyPrice)


        rDifference = round(Difference)
        strDifference = str(rDifference)

        strSellVolume = PrettyNumbers(sellVolume)
        strBuyVolume = PrettyNumbers(buyVolume)

        #storing the difference and the product
        if Difference > 0:
            #add the value to a list
            toplist.append("There is a " + strDifference + "% difference between the sell and buy price of **" + readableName + "**, or " + strIncrease + "$ *(BuyVolume: " + strBuyVolume + " SellVolume: " + strSellVolume + ")*.")      


    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
