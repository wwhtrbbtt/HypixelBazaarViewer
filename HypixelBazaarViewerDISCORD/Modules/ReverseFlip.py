global sortedtoplist
import json
import requests
from natsort import humansorted
import sys
from SmallDefs import *

sys.path.insert(1, 'Modules')

NPCPrices = NPCPrices()

def ReverseFlip():
    JSON = JSONData()
    toplist = []
    #LOOP THROUGH ALL PRODUCTS
    print("test2")
    for x in (NPCPrices["productIds"]):  
        Product = x
        #print(x)
        NormalPName = Product
        #npc data, local
        try:
            NPCSellPrice = float((NPCPrices["productIds"][Product]["MerchantSellPrice"]))
            NPCBuyPrice = (NPCPrices["productIds"][Product]["MerchantBuyPrice"])
            Merchant = (NPCPrices["productIds"][Product]["Merchant"])
            Product = (NPCPrices["productIds"][Product]["NormalName"])          
        except KeyError as ke:
            print("KeyError lol, but not really. idk")
        #bazaar data

        sellPrice = float(JSON[Product]['quick_status']['sellPrice'])
        buyPrice = float(JSON[Product]['quick_status']['buyPrice'])
        #npcdata
            #round up the prices
        rSellPrice = round(sellPrice, 2)
        rBuyPrice = round(buyPrice, 2)
            #make the prices to strings
        frSellPrice = str(rSellPrice)  # float -> str
        frBuyPrice = str(rBuyPrice)  # float -> str            
            #Can you even buy that item?
        if NPCBuyPrice == "CantBuyThat":
           a = 0
        else:
                #Do you make Profit?
            Profit = NPCSellPrice - buyPrice

            rProfit = round(Profit, 2)
            srProfit = str(rProfit)
            frProfit = float(rProfit)
                #would you make profit?
            if frProfit > 0:
                toplist.append(srProfit + "$ by selling " + NormalPName + " to a NPC, after you bought it at the bazaar.")

    #print the stuff
    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
