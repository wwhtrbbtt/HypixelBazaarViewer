from natsort import humansorted
import sys
from SmallDefs import *
sys.path.insert(1, 'Modules')
Items = AllItems()
def PriceDifference():
    print("answered to $pricedifference")
    JSON = JSONData()
    toplist = []
         
    for x in Items["items"]:          
        Product = x["Name"]
        readableName = x["CleanName"]
        try:
        #BAZAAR PRICES
            buyPrice = JSON[Product]['buy_summary'][0]["pricePerUnit"]
            sellPrice = JSON[Product]['sell_summary'][0]["pricePerUnit"]
            buyVolume = JSON[Product]['quick_status']['buyVolume']
            sellVolume = JSON[Product]['quick_status']['sellVolume']
        except:
            xyz = 0
        #round up the prices
        rSellPrice = round(sellPrice, 2)
        rBuyPrice = round(buyPrice, 2)
        #make the prices to string
        frSellPrice = str(rSellPrice)  # float -> str
        frBuyPrice = str(rBuyPrice)  # float -> str
        #how big is the absolut difference?
        Increase = buyPrice - sellPrice
        rIncrease = round(Increase, 2)
        strIncrease = str(rIncrease) # 1
        Difference = percent(sellPrice, buyPrice)
        rDifference = round(Difference)
        strDifference = str(rDifference)

        strSellVolume = PrettyNumbers(sellVolume)
        strBuyVolume = PrettyNumbers(buyVolume)

        #storing the difference and the product
        if Difference > 0:
            #add the value to a list
            toplist.append("*("+PrettyNumbers(Difference)+"% difference)* You make a buy-offer for 1 **" + readableName + "**, and when its filled, you make a sell-offer. \nThis makes $" + strIncrease + "!\n=======\n*(BuyVolume: " + strBuyVolume + " SellVolume: " + strSellVolume + " buy price: " + frBuyPrice + " sell price: " + frSellPrice + ")*.")      


    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
