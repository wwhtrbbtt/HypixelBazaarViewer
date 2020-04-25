import requests
import json

#every Bazaar product: https://api.hypixel.net/skyblock/bazaar/products?key=39eda60a-3b7c-4ecb-bc17-4d86d2e39af0 

print("""  ______ _      _____ __  __ __  __ ______ _____   _____ 
 |  ____| |    |_   _|  \/  |  \/  |  ____|  __ \ / ____|
 | |__  | |      | | | \  / | \  / | |__  | |__) | (___  
 |  __| | |      | | | |\/| | |\/| |  __| |  _  / \___ \ 
 | |    | |____ _| |_| |  | | |  | | |____| | \ \ ____) |
 |_|__  |______|_____|_|  |_|_|  |_|______|_|__\_\_____/ 
 |  _ \   /\    |___  /   /\        /\   |  __ \         
 | |_) | /  \      / /   /  \      /  \  | |__) |        
 |  _ < / /\ \    / /   / /\ \    / /\ \ |  _  /         
 | |_) / ____ \  / /__ / ____ \  / ____ \| | \ \         
 |____/_/____\_\/_____/_/    \_\/_/____\_\_|__\_\        
 \ \    / /_   _|  ____\ \        / /  ____|  __ \       
  \ \  / /  | | | |__   \ \  /\  / /| |__  | |__) |      
   \ \/ /   | | |  __|   \ \/  \/ / |  __| |  _  /       
    \  /   _| |_| |____   \  /\  /  | |____| | \ \       
  ___\/  _|_____|______|   \/  \/   |______|_|  \_\      
 |___ \ / _ \ / _ \/_ |                                  
   __) | | | | | | || |                                  
  |__ <| | | | | | || |                                  
  ___) | |_| | |_| || |                                  
 |____/ \___/ \___/ |_|                                  
                                                         
                               """)

 ########YOUR API KEY HERE!!##########
ApiKey = "39eda60a-3b7c-4ecb-bc17-4d86d2e39af0"


#Product you wanna see?
print()
print()
Product = input("Product you want to see? For example: Wheat (Every word has to be capitalized cause i cant programm)\n")
print("Ok, you want to see the product " + Product)
#ApiKey = input("Your ApiKey?\n")
#print("Ok, your ApiKey is:  " + ApiKey)

NormalPName = Product
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

print("You can buy " + NormalPName + " from an NPC for " + fNPCBuyPrice + "$ and sell it for " + fNPCSellPrice + "$")

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


#get  the prices
sellPrice = (JSONData["product_info"]['quick_status']['buyPrice'])
buyPrice = (JSONData['product_info']['quick_status']['sellPrice'])


#round up the prices
rSellPrice = round(sellPrice, 2)
rBuyPrice = round(buyPrice, 2)

#make the prices to floats
FrSellPrice = str(rSellPrice)  # float -> str
FrBuyPrice = str(rBuyPrice)  # float -> str

#print the prices
print("You can buy " + NormalPName + " from the bazaar for " + FrBuyPrice + "$ and sell it for " + FrSellPrice + "$")


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
print("You are making " + srProfit + "$ with this, do it!")
#if FrSellPrice < fNPCBuyPrice:  print("You are losing money with this flip, dont do it!!")

