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

def flip(Product):
    print("replied to a message, $merchantflip")
    Product = message.content[6:].lower()
    NormalPName = Product
    embed = discord.Embed(title="Information:", description="beep boop beep", color=000000)
    #npc data
    try:
        NPCBuyPrice = NPCPrices["productIds"][Product]["MerchantBuyPrice"]
        NPCSellPrice = NPCPrices["productIds"][Product]["MerchantSellPrice"]
        Merchant = (NPCPrices["productIds"][Product]["Merchant"])
        
        if NPCBuyPrice == "CantBuyThat":
            #await message.channel.send("You cant buy this item, but you can sell it for " + NPCSellPrice + "$ to a NPC.")
            embed.add_field(name="You cant buy that :/", value="You cant buy this item, but you can sell it for " + NPCSellPrice + "$ to a NPC.", inline=False)

        else:
            #await message.channel.send('Hello! You can sell "' + NormalPName +'" for ' + NPCSellPrice + "$ to an NPC, and buy it for " + NPCBuyPrice + "$ from the " + Merchant + "merchant."  )
            embed.add_field(name="NPC Prices:", value="Hello! You can sell " + NormalPName +'" for ' + NPCSellPrice + "$ to an NPC, and buy it for " + NPCBuyPrice + "$ from the " + Merchant + "merchant.", inline=False)
    except KeyError as ke:
         #await message.channel.send("I couldnt find this item: " + NormalPName + ". Maybe its not added yet, or its a typo /:")
         embed.add_field(name="Error:", value="Coudnt find this item. Request it with $request", inline=False)

        #realtime bazaar data
    #we dont want an keyerror to crash our programm, so we use try:
    try:
        Product = NPCPrices["productIds"][Product]["NormalName"] 
        payload = {'key': ApiKey, "productId": Product}
        r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
        JSONData = (r.json())
        result = str(JSONData)
        sellPrice = JSONData["product_info"]['quick_status']['buyPrice']
        buyPrice = JSONData['product_info']['quick_status']['sellPrice']
            #round up the prices
        rSellPrice = round(sellPrice, 2)
        rBuyPrice = round(buyPrice, 2)
            #make the prices to strings
        FrSellPrice = str(rSellPrice)  # float -> str
        FrBuyPrice = str(rBuyPrice)  # float -> str
            #print the prices
     
        embed.add_field(name="Bazaar prices:", value='You can sell "' + NormalPName +  '" to the bazaar for ' + FrSellPrice + '$ and buy it from the bazaar for ' + FrBuyPrice + '$', inline=False)
            #Do you make Profit?

        if NPCBuyPrice == "CantBuyThat":
            embed.add_field(name="Nope,", value="You cant resell this item, because no merchant sells it.", inline=False)

        else:
            fffNPCBuyPrice = float(NPCBuyPrice)
            Profit = rSellPrice - fffNPCBuyPrice
            rProfit = round(Profit, 2)
            srProfit = str(rProfit)

            fTotalProfit = rProfit*640
            RoundedfTotalProfit = round(fTotalProfit)
            strTotalProfit = str(RoundedfTotalProfit)
            if srProfit > "0":
               
                embed.add_field(name="Profit:", value="You are making " + srProfit + "$ with this, do it! If you flip 640, you can even make " + strTotalProfit + "$. Out of thin air!", inline=False)
            else:
                 embed.add_field(name=":/", value="You are losing money, ("+ srProfit + "$) dont do it!", inline=False)

    except KeyError as ke:
            print("someone inserted a wrong item name LMAO")


    return ThingsToSend
