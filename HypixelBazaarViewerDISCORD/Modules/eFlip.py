from natsort import humansorted
import sys
from SmallDefs import *

sys.path.insert(1, 'Modules')
NPCPrices = NPCPrices()

def eFlip():
    JSON = JSONData()
    toplist = []
        
    for Product in (NPCPrices["productIds"]):  #loop though all items
        NormalName = Product
        
        r160Product = 0
        #npc data, local
        try:
            Product = NPCPrices["productIds"][NormalName]["NormalName"]
            enchantedProduct = NPCPrices["productIds"][NormalName]["Enchanted"]
            buyPrice = JSON[Product]['buy_summary'][0]["pricePerUnit"]
                ##enchanted Prices 
            enchantedSellPrice = JSON[enchantedProduct]['sell_summary'][0]["pricePerUnit"]

            enchantedName = Readable(enchantedProduct)
            #ROUND THE PRICE
            rEnchantedSellPrice = round(enchantedSellPrice)
            strEnchantedSellPrice = str(rEnchantedSellPrice)

            #Is it really x160? Sometimes its different
            try:
                CraftNumber = float(NPCPrices["productIds"][NormalName]["SpecialCase"])
            except:
                CraftNumber = 160

            xxProduct = buyPrice * CraftNumber
            rxxProduct = round(xxProduct)
            strxxProduct = str(rxxProduct)

            if xxProduct < enchantedSellPrice:
                Profit = rEnchantedSellPrice - rxxProduct
                strProfit = str(Profit)
                strCraftNumber = str(CraftNumber)
                try:
                    toplist.append("You can make " + strProfit + "$ by buying " + strCraftNumber + " **" + NormalName + "** for " + strxxProduct + "$, craft it to " + enchantedName + " and then sell it for " + strEnchantedSellPrice + "$ back to the bazaar. Profit!")
                except:
                    print("fuck")
            else:
                a = 0

        except KeyError:
            a = 0

    sortedtoplist = humansorted(toplist)
    sortedtoplist.reverse()
    return sortedtoplist
