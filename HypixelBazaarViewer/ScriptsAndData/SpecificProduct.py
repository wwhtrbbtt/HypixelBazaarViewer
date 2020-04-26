import requests
import json
import string
import sys
sys.path.insert(1, 'ScriptsAndData')
#every Bazaar product: https://api.hypixel.net/skyblock/bazaar/products?key=YourApiKey
#Thanks to ThisIsMyPassword for this spreadsheet
#And thanks for every Betatester
##nice spreadsheet with prices: https://docs.google.com/spreadsheets/d/1_ej-xLzpVEvrGmp3JOXRFC5B_gHwJPMpB3SYMC3dDDY/edit#gid=0

    #Getting the ApiKey (Your ApiKey will not be sended anywhere! Read the code!)
with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()
#print(ApiKey)



    #Product you wanna see?
print()
print()
Product = input("Product you want to see? For example: Wheat\n")
print("Ok, you want to see the product " + Product)
#ApiKey = input("Your ApiKey?\n")
#print("Ok, your ApiKey is:  " + ApiKey)
Product = Product.lower()
NormalPName = Product
    #making input lowercase 
Product = Product.lower()
    #MERSHANT PRICES

    # read file
with open('Prices.json', 'r') as myfile:
    data=myfile.read()

    # parse file
NPCPrices = json.loads(data)
#print("succses?: " + str(obj['succses']))

FileReadSuccses = (NPCPrices["success"])
print("Was reading the file a succses? " + FileReadSuccses)


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


    #did it sucsess?
print("Was connecting to the Hypixel API a succses?")
print(JSONData["success"])


    #get the prices
sellPrice = (JSONData["product_info"]['quick_status']['buyPrice'])
buyPrice = (JSONData['product_info']['quick_status']['sellPrice'])


    #round up the prices
rSellPrice = round(sellPrice, 2)
rBuyPrice = round(buyPrice, 2)

    #make the prices to floats
FrSellPrice = str(rSellPrice)  # float -> str
FrBuyPrice = str(rBuyPrice)  # float -> str

    #print the prices
print("You can buy " + NormalPName + " from the bazaar for " + FrBuyPrice + "$ and sell it to the bazaar for " + FrSellPrice + "$")


    #Do you make Profit?
fffNPCBuyPrice = float(NPCBuyPrice)
#rSellPrice = float(rSellPrice)
Profit = rSellPrice - fffNPCBuyPrice
#Profit = float(Profit)
rProfit = round(Profit, 2)
srProfit = str(rProfit)

print()
print()
print()
print("--------------------------------------")

#if FrSellPrice > fNPCBuyPrice:
if srProfit > "0":
    print("You are making " + srProfit + "$ with this, do it!")
else:
    print("You are losing money, ("+ srProfit + "$) dont do it!")

    
        #Print every avaiable Product, remove #
#for x in NPCPrices["productIds"]: print(x)
print()
print()
print()
print("Buy me VIP, IGN: flimmerkraft")
