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
print()

    #getting the NPC prices
NPCBuyPrice = NPCPrices["productIds"][Product]["MerchantBuyPrice"]
NPCSellPrice = NPCPrices["productIds"][Product]["MerchantSellPrice"]

    #merchant?
Merchant = (NPCPrices["productIds"][Product]["Merchant"])

    #make the prices to floats
fNPCBuyPrice = str(NPCBuyPrice)  # float -> str
fNPCSellPrice = str(NPCSellPrice)  # float -> str

    #printing the prices

print("You can buy " + NormalPName + " from the " + Merchant + " merchant for " + fNPCBuyPrice + "$ and sell it to him for " + fNPCSellPrice + "$")

print()

Product = NPCPrices["productIds"][Product]["NormalName"] 
    #BAZAAR PRICES

    #getting the data
payload = {'key': ApiKey, "productId": Product}
r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
#print("`The Api URL is: " + r.url)
JSONData = (r.json())
result = str(JSONData)


    #get the prices

sellPrice = JSONData["product_info"]['quick_status']['buyPrice']
buyPrice = JSONData['product_info']['quick_status']['sellPrice']

    #round up the prices
rSellPrice = round(sellPrice, 2)
rBuyPrice = round(buyPrice, 2)

    #make the prices to strings
FrSellPrice = str(rSellPrice)  # float -> str
FrBuyPrice = str(rBuyPrice)  # float -> str

    #print the prices
print("You can buy " + NormalPName +  " from the bazaar for " + FrBuyPrice + "$ and sell it to the bazaar for " + FrSellPrice + "$")


    #Do you make Profit?
fffNPCBuyPrice = float(NPCBuyPrice)
Profit = rSellPrice - fffNPCBuyPrice
rProfit = round(Profit, 2)
srProfit = str(rProfit)

fTotalProfit = rProfit*640
RoundedfTotalProfit = round(fTotalProfit)
strTotalProfit = str(RoundedfTotalProfit)

print()
print()
print()
print("--------------------------------------")

#if FrSellPrice > fNPCBuyPrice:
if srProfit > "0":
    print("You are making " + srProfit + "$ with this, do it! If you flip 640, you can even make " + strTotalProfit + "$. Out of thin air!")
else:
    print("You are losing money, ("+ srProfit + "$) dont do it!")

    
        #Print every avaiable Product, remove #
print()
print()
print()
print("Buy me VIP, IGN: flimmerkraft")
