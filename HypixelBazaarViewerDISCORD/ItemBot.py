
DiscordBotToken = "Your bot token" #    <--- Your Discord Bot token.

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
from flip import flip


#creating a session
client = discord.Client()


@client.event

async def on_ready():

    activity = discord.Game(name="Hypixel")
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
        
            
        embed = discord.Embed(title="$flip " + Product, description="It Aint much, but its honest work", color=000000)
        
        try:
            embed.add_field(name="1:", value=Send[0], inline=False)
            try:
                embed.add_field(name="2:", value=Send[1], inline=False)
                try:
                    embed.add_field(name="3:", value=Send[2], inline=False)
                except:
                    a = 0
            except:
                a = 0
        except:
            embed.add_field(name="Cant find " + Product, value="/:", inline=False)
        await message.channel.send(embed=embed)
     

    elif message.content.startswith('$commands'):
        embed = discord.Embed(title="Every command", description="beep boop beep", color=000000)
        embed.add_field(name="$commands", value="Show every command.", inline=False)
        embed.add_field(name="$flip (item)", value="This will give you information about one item, like the NPC buy and sell price, and also the bazaar prices.", inline=False)
        embed.add_field(name="$merchantflip", value="Shows the top products to flip.", inline=False)
        embed.add_field(name="$pricedifference", value="This will give you the items from the bazaar with the biggest buy-sell gap.", inline=False)
        embed.add_field(name="$request (item)", value="If a item isnt supported yet, do this.", inline=False)
        embed.add_field(name="$notify", value="Using these two commands, you can toggle your notifications for events.", inline=False)
        embed.add_field(name="$eflip", value="This will show you the top 5 items, you can buy from the bazaar, craft to the enchanted versions and resell them.", inline=False)
        embed.add_field(name="$bestlog", value="Shows the woodtype, thats worth the most atm.", inline=False)
        embed.add_field(name="$reverseflip", value="This shows you items, that you can buy at the Bazaar and sell to an NPC for profit. Not much, but easy.", inline=False)
        await message.channel.send(embed=embed)
        print("answered to $commands")

    elif message.content.startswith('$merchantflip'):
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
        print("This doesnt work right now.")
        await message.channel.send("This doesnt work right now.")
        return

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
        Request(Product)
        await message.channel.send("Ok, @p337#1980 has to add this. I wrote it to a text file.")

    elif message.content.startswith('$events'):
        print("ehh")       
    elif message.content.startswith('$eflip'):
       
        sortedtoplist = eFlip()
        #I love try and except

        embed = discord.Embed(title="Nice!", description="Look up first, if you have the right collection!", color=000000)
        
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

        await message.channel.send(embed=embed)
        print("replied to a message, e-flip!")
        toplist = []

    elif message.content.startswith('$reverseflip'):

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
        embed.add_field(name="#6:", value=sortedtoplist[5], inline=False)
        await message.channel.send(embed=embed)
        sortedtoplist = []







#make the session happen
client.run(DiscordBotToken)
