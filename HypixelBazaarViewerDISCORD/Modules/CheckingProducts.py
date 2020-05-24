#import discord
#from discord.utils import get
import sys
import json
from SmallDefs import *
#import random
#import time
#DiscordBotToken = "NzA1MTQ4MDI4ODYzOTA1OTAy.XsQI2w.PjgDpn2ZuCYDF7sWP-hL6f_4Yx0" # 

def CheckProducts():

    with open('ToCheck.json', 'r') as handle:
        ToCheck = json.load(handle)
    print(ToCheck)


    a = 0
    while a == 0:
            JSON = JSONData()
            for x in ToCheck:
                Product = x
                print(x)

                buyPrice = JSON[Product]['quick_status']['buyPrice']
                requestedPrice = ToCheck[x][Price]
                print("========")
                print(ToCheck[x])
                if buyPrice > requestedPrice:
                    user = ToCheck[x][DiscordTag]
                 #   await message.channel.send
                    print("<" + user + ">, you can buy " + x + " for under " + requestedPrice + ". The current price is " + buyPrice + ".")


    time.sleep(3)
