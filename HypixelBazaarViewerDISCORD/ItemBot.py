
DiscordBotToken = "BotTokenHere" #    <--- Your Discord Bot token.

global sortedtoplist

##############################################

import discord
from discord.utils import get
import json
import requests
from natsort import humansorted
import sys

sys.path.insert(1, 'Modules')


#########   modules
from eFlip import eFlip
from BestLog import BestLogs
from MerchantFlip import MerchantFlip
from ReverseFlip import ReverseFlip
from PriceDifference import PriceDifference

# HAVE TO CHANGE THIS, BY MAKING IT TOO A FUNKTION IN A DIFFERENT FILE.
#from flip import flip

######  apikey
with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()

toplist = []
AllProfit = 0


### The NPC prices:
    # read file
with open('Prices.json', 'r') as prices:
    data=prices.read()
    # parse file
NPCPrices = json.loads(data)



#creating a session
client = discord.Client()


@client.event

async def on_ready():

    activity = discord.Game(name="Hypixel")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(client))


with open('Prices.json', 'r') as prices:
    data=prices.read()
    # parse file
NPCPrices = json.loads(data)


@client.event
async def on_message(message):
    if message.author == client.user:
        return



################################################
#           Modules start here!


    if message.content.startswith('$flip '):

        print("replied to a message, $flip")
        Product = message.content[6:].lower()
        #flip()
        NormalPName = Product
        embed = discord.Embed(title="Information:", description="beep boop beep", color=000000)
        #npc data
        try:
            NPCBuyPrice = NPCPrices["productIds"][Product]["MerchantBuyPrice"]
            NPCSellPrice = NPCPrices["productIds"][Product]["MerchantSellPrice"]
            Merchant = (NPCPrices["productIds"][Product]["Merchant"])
            
            if NPCBuyPrice == "CantBuyThat":
                embed.add_field(name="You cant buy that :/", value="You cant buy this item, but you can sell it for " + NPCSellPrice + "$ to a NPC.", inline=False)

            else:
              
                embed.add_field(name="NPC Prices:", value="Hello! You can sell " + NormalPName +'" for ' + NPCSellPrice + "$ to an NPC, and buy it for " + NPCBuyPrice + "$ from the " + Merchant + "merchant.", inline=False)
        except KeyError as ke:

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
                    embed.add_field("You are losing money, ("+ srProfit + "$) dont do it!")
        except KeyError as ke:
               # await message.channel.send("I could find this item:" + NormalPName)
                print("someone inserted a wrong item name LMAO")
                #$COMMANDS ################

        await message.channel.send(embed=embed)        

    elif message.content.startswith('$commands'):
        embed = discord.Embed(title="Every command", description="beep boop beep", color=000000)
        embed.add_field(name="$commands", value="Show every command.", inline=False)
        embed.add_field(name="$flip (item)", value="This will give you information about one item, like the NPC buy and sell price, and also the bazaar prices.", inline=False)
        embed.add_field(name="$merchantflip", value="Shows the top products to flip.", inline=False)
        embed.add_field(name="$pricedifference", value="This will give you the items from the bazaar with the biggest buy-sell gap.", inline=False)
        embed.add_field(name="$request (item)", value="If a item isnt supported yet, do this.", inline=False)
        embed.add_field(name="$notifications on/off", value="Using these two commands, you can toggle your notifications.", inline=False)
        embed.add_field(name="$eflip", value="This will show you the top 5 items, you can buy from the bazaar, craft to the enchanted versions and resell them.", inline=False)
        embed.add_field(name="$bestlog", value="Shows the woodtype, thats worth the most atm.", inline=False)
        embed.add_field(name="$reverseflip", value="This shows you items, that you can buy at the Bazaar and sell to an NPC for profit. Not much, but easy.", inline=False)
        await message.channel.send(embed=embed)
        print("answered to $commands")

    elif message.content.startswith('$merchantflip'):
        await message.channel.send("Ok, checking through all products. This can take a minute. In this time, i cant answer any other requests.")
        print("replied to a message, $merchantflip!")

        sortedtoplist = MerchantFlip()
        
        embed = discord.Embed(title="How much can you make?", description="Beeep bup", color=000000)
        embed.add_field(name="#1:", value=sortedtoplist[0], inline=False)
        embed.add_field(name="#2:", value=sortedtoplist[1], inline=False)
        embed.add_field(name="#3:", value=sortedtoplist[2], inline=False)
        embed.add_field(name="#4:", value=sortedtoplist[3], inline=False)
        embed.add_field(name="#5:", value=sortedtoplist[4], inline=False)
        await message.channel.send(embed=embed)

        sortedtoplist = []
        AllProfit = 0

    elif message.content.startswith("$pricedifference"):
        print("replied to a message, $pricedifference")
        await message.channel.send("Ok, checking through all products. This can take a minute. In this time, i cant answer any other requests.")

        sortedtoplist = PriceDifference()
        
        embed = discord.Embed(title="Dont lose your money!", description="This function is a bit broken atm, tbh", color=000000)
        embed.add_field(name="#1:", value="There is a " + sortedtoplist[0], inline=False)
        embed.add_field(name="#2:", value="There is a " + sortedtoplist[1], inline=False)
        embed.add_field(name="#3:", value="There is a " + sortedtoplist[2], inline=False)
        embed.add_field(name="#4:", value="There is a " + sortedtoplist[3], inline=False)
        embed.add_field(name="#5:", value="There is a " + sortedtoplist[4], inline=False)
        await message.channel.send(embed=embed)
        
        toplist = []
        sortedtoplist = []

    elif message.content.startswith('$request'):
        Product = message.content[9:].lower()
        file = open('ItemsToAdd.txt', 'a')
        file.write("You have to add: " + Product + ".")
        file.write("\n")
        file.close()
        await message.channel.send("Ok, @p337#1980 has to add this. I wrote it to a text file.")

    elif message.content.startswith('$notifications on'):
        member = message.author
        print(message.author)
        ROLE = "🔔"
        role = get(member.guild.roles, name=ROLE)
        await member.add_roles(role)
        await message.channel.send("Ok, You now will be notified when a event happens. Gotta get that candy")
        print("added role 🔔 to someome")

    elif message.content.startswith('$notifications off'):
        member = message.author
        print(message.author)
        ROLE = "🔔"
        role = get(member.guild.roles, name=ROLE)
        await member.remove_roles(role)
        await message.channel.send("Ok, You now wont be notified anymore")
        print("removed role 🔔 from someome")

    elif message.content.startswith('$events'):
        print("ehh")       
    elif message.content.startswith('$eflip'):
        await message.channel.send("This can take 1-2min, because its checking every item.")
       
        sortedtoplist = eFlip()
        #I love try and except

        embed = discord.Embed(title="Nice!", description="Look up first, if you have the right collection!", color=000000)
        
        try:
            embed.add_field(name="#1:", value="You can make " + sortedtoplist[0], inline=False)
            try:
                embed.add_field(name="#2:", value="You can make " + sortedtoplist[1], inline=False)
                try:
                    embed.add_field(name="#3:", value="You can make " + sortedtoplist[2], inline=False)
                    try:
                        embed.add_field(name="#4:", value="You can make " + sortedtoplist[3], inline=False)
                        try:
                            embed.add_field(name="#5:", value="You can make " + sortedtoplist[4], inline=False)
                        except:
                            a = 0
                    except:
                        a = 0
                except:
                    a = 0
            except:
                a = 0
        except:
        	embed.add_field(name="No items found", value="Cant find any items :/", inline=False)

        await message.channel.send(embed=embed)
        print("replied to a message, e-flip!")
        toplist = []

    elif message.content.startswith('$reverseflip'):
        await message.channel.send("Ok, checking through all products. This can take a minute. In this time, i cant answer any other requests.")

        print("replied to a message!")
        sortedtoplist = ReverseFlip()
        embed = discord.Embed(title="Nice!", description="It Aint much, but its honest work", color=000000)
        
        try:
            embed.add_field(name="#1:", value="You can make " + sortedtoplist[0], inline=False)
            try:
                embed.add_field(name="#2:", value="You can make " + sortedtoplist[1], inline=False)
                try:
                    embed.add_field(name="#3:", value="You can make " + sortedtoplist[2], inline=False)
                    try:
                        embed.add_field(name="#4:", value="You can make " + sortedtoplist[3], inline=False)
                        try:
                            embed.add_field(name="#5:", value="You can make " + sortedtoplist[4], inline=False)
                        except:
                            a = 0
                    except:
                        a = 0
                except:
                    a = 0
            except:
                a = 0
        except:
            embed.add_field(name="No items found", value="You cant resell any items.", inline=False)
        await message.channel.send(embed=embed)
     
    elif message.content.startswith('$bestlog'):
        print("answered to BestLogs")

        #print(BestLogs())
        sortedtoplist = BestLogs()

        embed = discord.Embed(title="For how much can you sell each log?", description="You can sell every log for 2$ to the NPC.", color=000000)
        embed.add_field(name="#1:", value=sortedtoplist[0], inline=False)
        embed.add_field(name="#2:", value=sortedtoplist[1], inline=False)
        embed.add_field(name="#3:", value=sortedtoplist[2], inline=False)
        embed.add_field(name="#4:", value=sortedtoplist[3], inline=False)
        embed.add_field(name="#5:", value=sortedtoplist[4], inline=False)
        await message.channel.send(embed=embed)
        sortedtoplist = []







#make the session happen
client.run(DiscordBotToken)
