#every Bazaar product: https://api.hypixel.net/skyblock/bazaar/products?key=YourApiKey

#Thanks to ThisIsMyPassword for this spreadsheet

#And thanks for every Betatester

##nice spreadsheet with prices: https://docs.google.com/spreadsheets/d/1_ej-xLzpVEvrGmp3JOXRFC5B_gHwJPMpB3SYMC3dDDY/edit#gid=0




import requests
import json
import sys
from natsort import humansorted
from tkinter import *
from tkinter import messagebox

#smol messagebox
window = Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.withdraw()
messagebox.showinfo(title="Do you want to proceed?", message="Do you want to proceed? This can take a few minutes")

window.deiconify()
window.destroy()
window.quit()

sys.path.insert(1, 'ScriptsAndData')


toplist = []
AllProfit = 0
#margins_listProfit = []
#margins_listProduct = []


readableName = "0"
Profit = "0"

print()


with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()
       

    # read file
with open('Prices.json', 'r') as prices:
    data=prices.read()

    # parse file
NPCPrices = json.loads(data)

#loop
for x in (NPCPrices["productIds"]): 
 
    Product = x
    FileReadSuccses = (NPCPrices["success"])


    #getting the NPC price
    NPCSellPrice = (NPCPrices["productIds"][Product]["MerchantSellPrice"])
    NPCBuyPrice = (NPCPrices["productIds"][Product]["MerchantBuyPrice"])

    #getting the merchnat that sells that stuff

    Merchant = (NPCPrices["productIds"][Product]["Merchant"])
    #NPCBuyPrice = NPCPrices["productIds"][Product] if "Product" in NPCPrices["productIds"] else "This Product doesnt exist in my database /: Please contact me"
    #NPCBuyPrice = NPCPrices["productIds"][Product] if "Product" in NPCPrices["productIds"] else "This Product doesnt exist in my database /: Please contact me"

    #make the prices to strings
    fNPCBuyPrice = str(NPCBuyPrice)  # float -> str
    fNPCSellPrice = str(NPCSellPrice)  # float -> str

    #printing the prices

    print("checking the product " + Product + "...")
    readableName = Product
    Product = (NPCPrices["productIds"][Product]["NormalName"])

    #BAZAAR PRICES

    #getting the data
    payload = {'key': ApiKey, "productId": Product}
    r = requests.get('https://api.hypixel.net/skyblock/bazaar/product?', params=payload)
    
    #print("`The Api URL is: " + r.url)
    JSONData = (r.json())
    result = str(JSONData)


    #get the prices
    sellPrice = JSONData["product_info"]['quick_status']['buyPrice']
    buyPrice = JSONData['product_info']['quick_status']['sellPrice']

    #round up the prices
    rSellPrice = round(sellPrice, 2)
    rBuyPrice = round(buyPrice, 2)

    #make the prices to strings
    frSellPrice = str(rSellPrice)  # float -> str
    frBuyPrice = str(rBuyPrice)  # float -> str


    #Do you make Profit?
    fffNPCBuyPrice = float(NPCBuyPrice)
    #rSellPrice = float(rSellPrice)
    Profit = rSellPrice - fffNPCBuyPrice
    #Profit = float(Profit)
    rProfit = round(Profit, 2)
    srProfit = str(rProfit)
    frProfit = float(rProfit)
        #would you make profit?
    if frProfit > 0:
        #add the Profit value to a list
        #calculate total profit
        fTotalProfit = frProfit*640
        RoundedfTotalProfit = round(fTotalProfit)
        strTotalProfit = str(RoundedfTotalProfit)
        AllProfit = AllProfit + RoundedfTotalProfit
        #print(AllProfit)
        toplist.append(srProfit + "$ by selling " + readableName + " to the bazaar, or " + strTotalProfit + "$ if you flip 640, after you bought it from the " + Merchant + "merchant")
    #    print("--------------------------------------")
    else:
        print("--------------------------------------")
    
        
#print("========================================")

#reversing
sortedtoplist = humansorted(toplist)
sortedtoplist.reverse()

window = Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.title("Here are the results:")

def quit():
    window.destroy()

text = Text(window, height=30, width=120)
text.insert(INSERT, "Top 1: you can make " + sortedtoplist[0] + ". Nice!\n\nTop 2: you can make " + sortedtoplist[1] + ". Free Money!\n\nTop 3: you can make " + sortedtoplist[2] + ".\n\nTop 4: you can make " + sortedtoplist[3] + ".\n\nTop 5: you can make " + sortedtoplist[4] + ".\n\nTop 6: you can make " + sortedtoplist[5] + ".\n\nTop 7: you can make " + sortedtoplist[6] + ".\n\nTop 8: you can make " + sortedtoplist[7] + ".\n\nTop 9: you can make " + sortedtoplist[8] + ".\n\nTop 10: you can make " + sortedtoplist[2] + ".")
text.pack()
text.config(state="disabled")
quit = Button(window, text="ok", command=quit).pack()


