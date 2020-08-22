from natsort import humansorted
import sys
from SmallDefs import *
sys.path.insert(1, 'Modules')

NPCPrices = NPCPrices()
Items = AllItems()

def flip(Product):
    Product = Product.lower()
   
    JSON = JSONData()
    Send = []

    NormalPName = Product
    #npc data
    try:
        Product = ItemId(Product)
        print(Product)
        
        NPCBuyPrice = NPCPrices["productIds"][Product]["MerchantBuyPrice"]
        NPCSellPrice = NPCPrices["productIds"][Product]["MerchantSellPrice"]
        Merchant = (NPCPrices["productIds"][Product]["Merchant"])
        
        if NPCBuyPrice == "CantBuyThat":
            Send.append("You cant buy this item, but you can sell it for " + NPCSellPrice + "$ to a NPC.")
        else:
   
            Send.append("You can sell " + NormalPName +' for ' + NPCSellPrice + "$ to an NPC, and buy it for " + NPCBuyPrice + "$ from the " + Merchant + "merchant.")
    except KeyError as ke:
        Send.append("Coudnt find this item. Request it with $request")

        #realtime bazaar data
    #we dont want an keyerror to crash our programm, so we use try:
    try:
        rBuyPrice = round(JSON[Product]['buy_summary'][0]["pricePerUnit"], 2)
        rSellPrice = round(JSON[Product]['sell_summary'][0]["pricePerUnit"], 2)
        Send.append('You can sell ' + NormalPName +  ' to the bazaar for ' + str(rSellPrice) + '$ and buy it from the bazaar for ' + str(rBuyPrice) + '$')
            #Do you make Profit?

        if NPCBuyPrice == "CantBuyThat":

            Send.append("You cant resell this item, because no merchant sells it.")

        else:
            Profit = round(rSellPrice - float(NPCBuyPrice), 2)

            TotalProfit = PrettyNumbers(round(Profit*640))
            if Profit > 0:
               
                 Send.append("You are making $"+str(Profit),"with this, do it! If you flip 640, you can even make $" + str(TotalProfit) + ". Out of thin air!") 
            else:
                 Send.append("You are losing money, ($"+ srProfit + ") dont do it!")

    except KeyError as ke:
            print("someone inserted a wrong item name",Product)
    return Send
