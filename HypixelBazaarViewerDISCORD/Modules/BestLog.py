global sortedtoplist
import json
import requests
from natsort import humansorted
import sys
from SmallDefs import *

sys.path.insert(1, 'Modules')

NPCPrices = NPCPrices()

def BestLogs():
    JSON = JSONData()
    print("working")

    toplist = []
    sortedtoplist = []

    LogsToCheck = ["oak log", "dark oak log", "jungle log", "spruce log", "birch log", "acacia log"]
    #print("checking " + LogsToCheck)
    print("replied to a message, $merchantflip")
    for x in LogsToCheck:
            NormalName = x
            Product = NPCPrices["productIds"][x]["NormalName"] 
            #api request
            sellPrice = (JSON[Product]["quick_status"]["sellPrice"])


            rSellPrice = round(sellPrice, 1)
            strSellPrice = str(rSellPrice)
            toplist.append("You can make " + strSellPrice + "$ per log if you sell " + NormalName + " to the bazaar.")

    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()

    return sortedtoplist


