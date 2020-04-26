#every Bazaar product: https://api.hypixel.net/skyblock/bazaar/products?key=YourApiKey

#Thanks to ThisIsMyPassword for this spreadsheet

#And thanks for every Betatester

##nice spreadsheet with prices: https://docs.google.com/spreadsheets/d/1_ej-xLzpVEvrGmp3JOXRFC5B_gHwJPMpB3SYMC3dDDY/edit#gid=0




import requests
import json
import string
import sys
sys.path.insert(1, 'ScriptsAndData')

BestProduct = "none"
HighestProfit = ("0")
HighestProfit = float(HighestProfit)
#print(type(HighestProfit))

    #Getting the ApiKey (Your ApiKey will not be sended anywhere! Read the code!)
with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()
#print(ApiKey)

Profit = "0"
       

    # read file
with open('Prices.json', 'r') as prices:
    data=prices.read()

    # parse file
NPCPrices = json.loads(data)

#loop
for x in (NPCPrices["productIds"]): 

    #making input lowercase 
    Product = x
    NormalPName = Product
    
    FileReadSuccses = (NPCPrices["success"])
    #print("Was reading the file a succses? " + FileReadSuccses)


    #getting the NPC prices
    NPCSellPrice = (NPCPrices["productIds"][Product]["MerchantSellPrice"])
    NPCBuyPrice = (NPCPrices["productIds"][Product]["MerchantBuyPrice"])


    #make the prices to floats
    fNPCBuyPrice = str(NPCBuyPrice)  # float -> str
    fNPCSellPrice = str(NPCSellPrice)  # float -> str

    #printing the prices

    print("You can buy " + NormalPName + " from an NPC for " + fNPCBuyPrice + "$ and sell it to him for " + fNPCSellPrice + "$")

    Product = (NPCPrices["productIds"][Product]["NormalName"])


    #BAZAAR PRICES

    #getting the data
    payload = {'key': ApiKey, "productId": Product}
    r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
    #print("`The Api URL is: " + r.url)
    JSONData = (r.json())
    result = str(JSONData)


    #get the prices
    sellPrice = (JSONData["product_info"]['quick_status']['buyPrice'])
    buyPrice = (JSONData['product_info']['quick_status']['sellPrice'])


    #round up the prices
    rSellPrice = round(sellPrice, 2)
    rBuyPrice = round(buyPrice, 2)

    #make the prices to floats
    frSellPrice = str(rSellPrice)  # float -> str
    frBuyPrice = str(rBuyPrice)  # float -> str

    #FrSellPrice = float(rSellPrice)
    #FrBuyPrice = float(rBuyPrice)

    #print the prices
    #print("You can buy " + NormalPName + " from the bazaar for " + frBuyPrice + "$ and sell it to the bazaar for " + frSellPrice + "$")


    #Do you make Profit?
    fffNPCBuyPrice = float(NPCBuyPrice)
#rSellPrice = float(rSellPrice)
    Profit = rSellPrice - fffNPCBuyPrice
#Profit = float(Profit)
    rProfit = round(Profit, 2)
    srProfit = str(rProfit)
    frProfit = float(rProfit)
    print()
    print("--------------------------------------")


    #if FrSellPrice > fNPCBuyPrice:
    if srProfit > "0":
         print("You are making " + srProfit + "$ with this, do it!")
#        print()
#    else:
         print("You are losing money, ("+ srProfit + "$) dont do it!")
#        print()

    if frProfit > HighestProfit:
        print()
        print("Highest profit margin so far")
        print()
        HighestProfit = frProfit
        BestProduct = NormalPName
        
#    else:
#        print()
        print("Not the highest profit margin so far")
#        print()
strHighestProfit = str(HighestProfit)
print("the highest profit margin is: " + strHighestProfit + "$ with the product " + BestProduct)
print()
print()
print("Buy me VIP, IGN: flimmerkraft")
