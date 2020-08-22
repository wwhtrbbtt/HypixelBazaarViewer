from natsort import humansorted
import sys
from SmallDefs import *
sys.path.insert(1, 'Modules')
NPCPrices = NPCPrices()
def MerchantFlip():

    JSON = JSONData()
    #print("working!")
    
    AllProfit = 0
    toplist = []
    print("replied to a message!")
    #LOOP THROUGH ALL PRODUCTS
    for x in (NPCPrices["productIds"]):  
        #print(x)
        Product = x
        NormalPName = Product

        #npc data, local
        try:

            NPCSellPrice = (NPCPrices["productIds"][Product]["MerchantSellPrice"])
            NPCBuyPrice = (NPCPrices["productIds"][Product]["MerchantBuyPrice"])
            Merchant = (NPCPrices["productIds"][Product]["Merchant"])
            Product = (NPCPrices["productIds"][Product]["NormalName"]) 
            #print(Product)
            #print(NPCPrices)
            #print(NPCPrices["productIds"][Product]["MerchantSellPrice"])
            
            
            
        except KeyError as ke:
            a = 0

        #bazaar data
        sellPrice = JSON[Product]['quick_status']['sellPrice']
        buyPrice = JSON[Product]['quick_status']['buyPrice']


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
            fffNPCBuyPrice = float(NPCBuyPrice)

            Profit = rSellPrice - fffNPCBuyPrice

            rProfit = round(Profit, 2)
            srProfit = str(rProfit)
            frProfit = float(rProfit)
                #would you make profit?
            if frProfit > 0:
             #add the Profit value to a list
                #calculate total profit
                fTotalProfit = frProfit*640
                RoundedfTotalProfit = round(fTotalProfit)
                strTotalProfit = str(RoundedfTotalProfit)
                AllProfit = AllProfit + RoundedfTotalProfit
                toplist.append("You can make " + srProfit + "$ by selling **" + NormalPName + "** to the bazaar, or " + strTotalProfit + "$ if you flip 640, after you bought it from the " + Merchant + "-merchant.")
                strAllProfit = str(AllProfit)


    #print the stuff
    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
