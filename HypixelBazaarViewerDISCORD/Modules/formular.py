import sys
sys.path.insert(1, 'Modules')
from natsort import humansorted
from SmallDefs import *
import json

Items = AllItems()

def Score():
    print("answered to $skyscore")
    toplist = []
    JSON = JSONData()
    for x in Items["items"]: 
        readableName = x["CleanName"]
        x = x["Name"]
        try:
            buyVolume = JSON[x]["quick_status"]["buyVolume"]
            sellVolume = JSON[x]["quick_status"]["sellVolume"]
            buyPrice = JSON[x]['buy_summary'][0]["pricePerUnit"]
            sellPrice = JSON[x]['sell_summary'][0]["pricePerUnit"]
        except:
            xyz = 0
        if sellPrice == 0:
            print()
        else:
            #Diff = (buyPrice - sellPrice)*2
            Diff = percent(sellPrice, buyPrice) / 8
            RAWDiff = buyPrice - sellPrice

            buyScore = buyVolume/50000
            sellScore = sellVolume/50000
            SBScore = (sellScore * buyScore)/200
            
            Score = (Diff + SBScore) / 2
            #if Diff > 0 and Score > 0:
            toplist.append("The score is " + str(round(Score)) + " from the poduct: **" + readableName + "**. *(Buy price: " + str(round(buyPrice, 1)) + ". Sell price: " + str(round(sellPrice, 1)) + ". Buy volume: " + PrettyNumbers(buyVolume) + " Sell volume: " + PrettyNumbers(sellVolume) + ", Diff: " + str(round(RAWDiff)) + ")*")


    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
