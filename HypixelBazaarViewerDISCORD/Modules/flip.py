global sortedtoplist
import json
import requests
from natsort import humansorted
import sys
from SmallDefs import *

sys.path.insert(1, 'Modules')

NPCPrices = NPCPrices()

def flip(Product):
    JSON = JSONData()
    Send = []

    NormalPName = Product
    #npc data
    try:
        NPCBuyPrice = NPCPrices["productIds"][Product]["MerchantBuyPrice"]
        NPCSellPrice = NPCPrices["productIds"][Product]["MerchantSellPrice"]
        Merchant = (NPCPrices["productIds"][Product]["Merchant"])
        
        if NPCBuyPrice == "CantBuyThat":
            Send.append("You cant buy this item, but you can sell it for " + NPCSellPrice + "$ to a NPC.")
        else:
   
            Send.append("You can sell " + NormalPName +'" for ' + NPCSellPrice + "$ to an NPC, and buy it for " + NPCBuyPrice + "$ from the " + Merchant + "merchant.")
    except KeyError as ke:


        Send.append("Coudnt find this item. Request it with $request")

        #realtime bazaar data
    #we dont want an keyerror to crash our programm, so we use try:
    try:
        Product = NPCPrices["productIds"][Product]["NormalName"] 

        buyPrice = JSON[Product]['quick_status']['buyPrice']
        sellPrice = JSON[Product]['quick_status']['sellPrice']
            #round up the prices
        rSellPrice = round(sellPrice, 2)
        rBuyPrice = round(buyPrice, 2)
            #make the prices to strings
        FrSellPrice = str(rSellPrice)  # float -> str
        FrBuyPrice = str(rBuyPrice)  # float -> str
            #print the prices
     

        Send.append('You can sell "' + NormalPName +  '" to the bazaar for ' + FrSellPrice + '$ and buy it from the bazaar for ' + FrBuyPrice + '$')
            #Do you make Profit?

        if NPCBuyPrice == "CantBuyThat":

            Send.append("You cant resell this item, because no merchant sells it.")

        else:
            fffNPCBuyPrice = float(NPCBuyPrice)
            Profit = rSellPrice - fffNPCBuyPrice
            rProfit = round(Profit, 2)
            srProfit = str(rProfit)

            fTotalProfit = rProfit*640
            RoundedfTotalProfit = round(fTotalProfit)
            strTotalProfit = str(RoundedfTotalProfit)
            if srProfit > "0":
               
                 Send.append("You are making " + srProfit + "$ with this, do it! If you flip 640, you can even make " + strTotalProfit + "$. Out of thin air!") 
            else:
                 Send.append("You are losing money, ("+ srProfit + "$) dont do it!")

    except KeyError as ke:
            print("someone inserted a wrong item name LMAO")


    return Send
