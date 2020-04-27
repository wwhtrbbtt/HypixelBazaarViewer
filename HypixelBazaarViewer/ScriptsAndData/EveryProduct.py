#every Bazaar product: https://api.hypixel.net/skyblock/bazaar/products?key=YourApiKey

#Thanks to ThisIsMyPassword for this spreadsheet

#And thanks for every Betatester

##nice spreadsheet with prices: https://docs.google.com/spreadsheets/d/1_ej-xLzpVEvrGmp3JOXRFC5B_gHwJPMpB3SYMC3dDDY/edit#gid=0




import requests
import json
import string
import sys
sys.path.insert(1, 'ScriptsAndData')

toplist = []
margins_listProfit = []
margins_listProduct = []


readableName = "0"
Profit = "0"

print()



    #Getting the ApiKey (Your ApiKey will not be sended anywhere! Read the code!)
with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()
       

    # read file
with open('Prices.json', 'r') as prices:
    data=prices.read()

    # parse file
NPCPrices = json.loads(data)

#loop
for x in (NPCPrices["productIds"]): 
 
    Product = x
    FileReadSuccses = (NPCPrices["success"])


    #getting the NPC prices
    NPCSellPrice = (NPCPrices["productIds"][Product]["MerchantSellPrice"])
    NPCBuyPrice = (NPCPrices["productIds"][Product]["MerchantBuyPrice"])

    #getting the merchnat that sells that stuff

    Merchant = (NPCPrices["productIds"][Product]["Merchant"])
#   NPCBuyPrice = NPCPrices["productIds"][Product] if "Product" in NPCPrices["productIds"] else "This Product doesnt exist in my database /: Please contact me"
#   NPCBuyPrice = NPCPrices["productIds"][Product] if "Product" in NPCPrices["productIds"] else "This Product doesnt exist in my database /: Please contact me"

    #make the prices to strings
    fNPCBuyPrice = str(NPCBuyPrice)  # float -> str
    fNPCSellPrice = str(NPCSellPrice)  # float -> str

    #printing the prices

 
    print("checking the product " + Product + "...")
    readableName = Product
    Product = (NPCPrices["productIds"][Product]["NormalName"])

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
    frSellPrice = str(rSellPrice)  # float -> str
    frBuyPrice = str(rBuyPrice)  # float -> str


    #Do you make Profit?
    fffNPCBuyPrice = float(NPCBuyPrice)
#rSellPrice = float(rSellPrice)
    Profit = rSellPrice - fffNPCBuyPrice
#Profit = float(Profit)
    rProfit = round(Profit, 2)
    srProfit = str(rProfit)
    frProfit = float(rProfit)

    
        #would you make profit?
    if frProfit > 0:
                 #add the Profit value to a list
 #      margins_listProfit.append(frProfit)
 #      margins_listProduct.append(CoolProductNameLmaoTheseNamings)
        #calculate total profit
        fTotalProfit = frProfit*640
        RoundedfTotalProfit = round(fTotalProfit)
        strTotalProfit = str(RoundedfTotalProfit)
        toplist.append(srProfit + "$ by selling " + readableName + " to the bazaar, or " + strTotalProfit + " if you flip 640, after you bought it from the " + Merchant + "merchant")
        print("--------------------------------------")
    else:
        print("--------------------------------------")
    
        
print("========================================")

#reversing and sorting lists
            #top5 products, this code is shit god damnit                Ill fix it later, or if someone reads this: Make it better please :)   


toplist.sort()
toplist.reverse()




#List of the best things to sell
                       
print()

print("Top 1: you can make " + toplist[0] + "after you bought it from the merchant. Nice!")
print()

print("Top 2: you can make " + toplist[1] + "after you bought it from the merchant. Free Money!")
print()

print("Top 3: you can make " + toplist[2] + "after you bought it from the merchant.")
print()

print("Top 4: you can make " + toplist[3] + "after you bought it from the merchant.")
print()

print("Top 5: you can make " + toplist[4] + "after you bought it from the merchant.")

#print(margins_listProfit)
#print(margins_listProduct)
print()
print()
print("=====================")
print("Buy me VIP, IGN: flimmerkraft")
print("=====================")
print()
print()
