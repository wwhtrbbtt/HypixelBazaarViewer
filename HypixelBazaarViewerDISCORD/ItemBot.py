DiscordBotToken = "<bot-token-here>" #    <--- Your Discord Bot token.

##############################################

import discord
from discord.utils import get
import sys
import random
import time
import subprocess
import os
sys.path.insert(1, 'Modules')

from os import system, name 
# for windows 
if name == 'nt': 
    _ = system('cls') 
# for mac and linux(here, os.name is 'posix') 
else: 
    _ = system('clear') 
    
    

#########   modules
from eFlip import eFlip
from BestLog import BestLogs
from MerchantFlip import MerchantFlip
from ReverseFlip import ReverseFlip
from PriceDifference import PriceDifference
from flip import flip
from SmallDefs import *
from formular import Score
from watchdog import Watchdog


client = discord.Client()


@client.event

async def on_ready():

    activity = discord.Game(name="$commands")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

################################################
#           Modules start here!

    if message.content.startswith('$flip '):

        print("replied to a message, $flip")
        Product = message.content[6:].lower()
        
        Send = flip(Product)
        
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="$flip " + Product, color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        
        i = 0
        for x in Send:
            embed.add_field(name="#"+str(i + 1) +":", value=Send[i], inline=False)
            i += 1
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)    

    elif message.content.startswith('$commands'):
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Every command", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        embed.add_field(name="$commands", value="Show every command.", inline=False)
        embed.add_field(name="$flip (item)", value="This will give you information about one item, like the NPC buy and sell price, and also the bazaar prices.", inline=False)
        embed.add_field(name="$merchantflip", value="Shows the top products to flip.", inline=False)
        embed.add_field(name="$everymerchantflip", value="Sends you a DM with every products to flip.", inline=False)
        embed.add_field(name="$pricedifference", value="This will give you the items from the bazaar with the biggest buy-sell gap.", inline=False)
        embed.add_field(name="$request (item)", value="If a item isnt supported yet, do this.", inline=False)
        embed.add_field(name="$notify", value="Using these two commands, you can toggle your notifications for events.", inline=False)
        embed.add_field(name="$eflip", value="This will show you the top 5 items, you can buy from the bazaar, craft to the enchanted versions and resell them.", inline=False)
        embed.add_field(name="$bestlog", value="Shows the woodtype, thats worth the most atm.", inline=False)
        #embed.add_field(name="$minions", value="You type in the details, and I say you how much you would make with that minion setup **code by e56, ported to a discord-bot by me.**", inline=False)
        embed.add_field(name="$skyscore", value="(BETA) That shows you the SkyScore of a product. The score gets calculated from the money you can make flipping it, and the buy/sell volume.", inline=False)
        embed.add_field(name="$reverseflip", value="This shows you items, that you can buy at the Bazaar and sell to an NPC for profit. Not much, but easy.", inline=False)
        embed.add_field(name="$watchdog", value="Everyone loves the watchdog message, right? Now you can get it on discord!", inline=False)
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)
        print("answered to $commands")

    elif message.content.startswith('$merchantflip'):
        print("replied to a message, $merchantflip!")

        sortedtoplist = MerchantFlip()
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="How much can you make?", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        i = 0
        for x in sortedtoplist:
            embed.add_field(name="#"+str(i + 1) +":", value=sortedtoplist[i], inline=False)
            i += 1
            if i == 4:
                break
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)

        sortedtoplist = []
        AllProfit = 0

    elif message.content.startswith('$request'):
        Product = message.content[9:].lower()
        Request(Product)
        await message.channel.send("Ok, <@585935919224324117> has to add this. I wrote it to a text file.")

    elif message.content.startswith('$eflip'):
       
        sortedtoplist = eFlip()
        #I love try and except
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Nice!", description="Look up first, if you have the right collection!", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        
        try:
            embed.add_field(name="#1:", value=sortedtoplist[0], inline=False)
            try:
                embed.add_field(name="#2:", value=sortedtoplist[1], inline=False)
                try:
                    embed.add_field(name="#3:", value=sortedtoplist[2], inline=False)
                    try:
                        embed.add_field(name="#4:", value=sortedtoplist[3], inline=False)
                        try:
                            embed.add_field(name="#5:", value=sortedtoplist[4], inline=False)
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

        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)
        print("replied to a message, e-flip!")
        toplist = []

    elif message.content.startswith('$reverseflip'):

        print("replied to a message!")
        sortedtoplist = ReverseFlip()
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Gettin that cash", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        i = 0
        for x in sortedtoplist:
            embed.add_field(name="#" + str(i+1)+ ":", value=sortedtoplist[i], inline=False)
            if i == 4:
                break
            i += 1
            
        await message.channel.send(embed=embed)
     
    elif message.content.startswith('$bestlog'):
        print("answered to BestLogs")

        #print(BestLogs())
        sortedtoplist = BestLogs()
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="For how much can you sell each log?", description="You can sell every log for 2$ to the NPC.", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        i = 0
        for x in sortedtoplist:
            embed.add_field(name="#"+str(i + 1) +":", value=sortedtoplist[i], inline=False)
            i += 1
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)
        sortedtoplist = []

    elif message.content.startswith("$pricedifference"):

        sortedtoplist = PriceDifference()
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Dont lose your money!", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        i = 0
        for x in sortedtoplist:
            embed.add_field(name="#"+str(i + 1) +":", value=sortedtoplist[i], inline=False)
            if i == 4:
                break
            i += 1
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)
        
        toplist = []
        sortedtoplist = []

    elif message.content.startswith('$everymerchantflip'):
        sortedtoplist = MerchantFlip()
        a = 1
        b = 0
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Gettin that cash", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        i = 0
        for x in sortedtoplist:
            embed.add_field(name="#"+str(i + 1) +":", value=sortedtoplist[i], inline=False)
            i += 1
        member = message.author
        channel = await member.create_dm()
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await channel.send(embed=embed)
        await message.channel.send("Ok, you should have gotten a DM with the prices.")

    elif message.content.startswith('$notifyme '):

        print("replied to a message, $notifyme")
        ############getting the product and the sender
        Person = message.author.id
        Product = message.content[10:].lower()
        #is this a existing product?
        if NormalName(Product) == "error":
            await message.channel.send("Couldnt find the item " + Product + ". If you think it should be added, request it with $request " + Product + ".")
            #it is!
        else:
            time.sleep(1)
            #getting the buy/sell data:
            await message.channel.send("Do you want to wait for the sell or buy price of the product to be a specific number? Enter buy or sell. You have 20 seconds.")
            buysell = await client.wait_for('message', timeout=20)
            if buysell.content == "sell" or buysell.content == "buy":
                buysell = buysell.content.lower()
                #nice!
                # when do you want to be notified?
                await message.channel.send("Ok, when do you want to be notified for the product " + Product + "? Please enter just a number. You have 20 seconds.")
                msg = await client.wait_for('message', timeout=20)
                try:
                    time.sleep(1)
                    Price = float(msg.content)
                    strPrice = str(Price)
                    await message.channel.send('Ok, you will be notified if the ' + buysell + ' price of ' + Product + " is under " + strPrice + "$.")
                    NewNotify(Product, Person, Price, buysell)
                except:
                    await message.channel.send("ERROR: Pleace just enter a number")
                    NewNotify(Product, Person, Price, buysell)

            else:
                await message.channel.send("ERROR: Please just say buy or sell.")

    elif message.content.startswith('$skyscore'):
        sortedtoplist = Score()
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Double check everything, still beta", color=color)
        embed.set_author(name="BazaarViewer", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
        i = 0
        for x in sortedtoplist:
            embed.add_field(name="#"+str(i + 1) +":", value=sortedtoplist[i], inline=False)
            if i == 4:
                break
            i += 1
        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)

    elif message.content.startswith('$watchdog'):
        await message.channel.send(Watchdog())







#make the session happen
client.run(DiscordBotToken)
