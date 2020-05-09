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

def ReverseFlip():
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
        payload = {'key': ApiKey, "productId": Product}
        r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
        JSONData = (r.json())
        result = str(JSONData)

        sellPrice = JSONData["product_info"]['quick_status']['buyPrice']
        buyPrice = float(JSONData['product_info']['quick_status']['sellPrice'])
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
