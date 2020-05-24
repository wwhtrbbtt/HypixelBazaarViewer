global sortedtoplist
import json
import requests
from natsort import humansorted
import sys
from SmallDefs import *

sys.path.insert(1, 'Modules')


NPCPrices = NPCPrices()

def eFlip():
    JSON = JSONData()
    toplist = []
        
    for x in (NPCPrices["productIds"]):  
        #print(x)
        Product = x
        #print(Product)
        NormalName = Product
        
        r160Product = 0

        #npc data, local
        try:

            Product = (NPCPrices["productIds"][NormalName]["NormalName"])

            enchantedProduct = (NPCPrices["productIds"][NormalName]["Enchanted"])
 
            buyPrice = JSON[Product]['quick_status']['buyPrice']
                ##enchanted Prices 

            enchantedSellPrice = JSON[enchantedProduct]['quick_status']['sellPrice']
            #ROUND THE PRICE
            rEnchantedSellPrice = round(enchantedSellPrice)
            strEnchantedSellPrice = str(rEnchantedSellPrice)

            #Is it really +160?
            try:
                CraftNumber = float((NPCPrices["productIds"][NormalName]["SpecialCase"]))
            except:
                CraftNumber = 160

            xxProduct = buyPrice * CraftNumber
            rxxProduct = round(xxProduct)
            strxxProduct = str(rxxProduct)

            if xxProduct < enchantedSellPrice:
                Profit = rEnchantedSellPrice - rxxProduct
                #print(rEnchantedSellPrice)
                #print(rxxProduct)
                strProfit = str(Profit)
                #print(Profit)
                strCraftNumber = str(CraftNumber)
                toplist.append("You can make " + strProfit + "$ by buying " + strCraftNumber + " **" + NormalName + "** for " + strxxProduct + "$, craft it to enchanted " + NormalName + " and then sell it for " + strEnchantedSellPrice + "$ back to the bazaar. Profit!")
                #print("appended")
                #await message.channel.send("You can make " + toplist[0])
                #print(toplist)
            else:
                a = 0

        except KeyError as ke:
            #print("fuck, keyerror for " + Product)
            a = 0


    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
