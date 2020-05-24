
import sys
import json


#DOESNT HAS ANY FUNCTION YET!
from SmallDefs import *

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
