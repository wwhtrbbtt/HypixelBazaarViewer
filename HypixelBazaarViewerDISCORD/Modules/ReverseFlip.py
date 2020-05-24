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
    for x in (NPCPrices["productIds"]):  
        Product = x
        NormalPName = Product
        #npc data, local
        try:
            sellPrice = float(NPCPrices["productIds"][Product]["MerchantSellPrice"])
            Product = (NPCPrices["productIds"][Product]["NormalName"])          
        except KeyError as ke:
            a = 0
        try:
            buyPrice = float(JSON[Product]['quick_status']['buyPrice'])
        except:
            a = 0

        if sellPrice > buyPrice:

            Profit = sellPrice - buyPrice
            rProfit = round(Profit, 2)
            strProfit = str(rProfit)
            toplist.append("You can make " + strProfit + "$ by selling **" + NormalPName + "** to a NPC, after you bought it at the bazaar.")

        else:
            a = 0

    #print the stuff
    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
