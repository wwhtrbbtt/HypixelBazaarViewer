global sortedtoplist
import json
import requests
from natsort import humansorted
import sys

sys.path.insert(1, 'Modules')

with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()
  print(ApiKey)

with open('Prices.json', 'r') as prices:
    data=prices.read()
    # parse file
NPCPrices = json.loads(data)
print(NPCPrices["success"])


def eFlip():
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
            
            #print("Normal name:" + NormalName + ". Enchanted Product:" + enchantedProduct)

            
                            ## Normal Prices
            payload = {'key': ApiKey, "productId": Product}
            r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
            JSONData = (r.json())
            result = str(JSONData)
 
            buyPrice = JSONData['product_info']['quick_status']['sellPrice']
                ##enchanted Prices 

            payload = {'key': ApiKey, "productId": enchantedProduct}
            r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
            JSONData = (r.json())
            result = str(JSONData)

            enchantedSellPrice = JSONData["product_info"]['quick_status']['buyPrice']
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
                
                toplist.append(strProfit + "$ by buying 160 " + NormalName + " for " + strxxProduct + "$, craft it to enchanted " + NormalName + " and then sell it for " + strEnchantedSellPrice + " back to the bazaar. Profit!")
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
