import sys
sys.path.insert(1, 'Modules')
from natsort import humansorted
from SmallDefs import *
import json

NPCPrices = NPCPrices()

def Score():
    toplist = []
    JSON = JSONData()
    for Product in (NPCPrices["productIds"]):
        
        x = (NPCPrices["productIds"][Product]["NormalName"])

        
        buyVolume = JSON[x]["quick_status"]["buyVolume"]
        sellVolume = JSON[x]["quick_status"]["sellVolume"]
        buyPrice = JSON[x]["quick_status"]["buyPrice"]
        sellPrice = JSON[x]["quick_status"]["sellPrice"]
        if sellPrice == 0:
            print()
        else:
            #Diff = (buyPrice - sellPrice)*2
            Diff = percent(sellPrice, buyPrice)/100
            buyScore = buyVolume/10000
            sellScore = sellVolume/10000
            SBScore = (sellScore + buyScore)


            Score = (SBScore + Diff) / 10
            #if Diff > 0 and Score > 0:
            toplist.append("The score is " + str(round(Score)) + " from the poduct: **" + Product + "**. *(Buy price: " + str(round(buyPrice)) + ". Sell price: " + str(round(sellPrice)) + ". Buy volume: " + PrettyNumbers(buyVolume) + " Sell volume: " + PrettyNumbers(sellVolume) + ")*")

    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
