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



toplist = []
sys.path.insert(1, 'ScriptsAndData')

print()

with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()

    # read file
with open('Prices.json', 'r') as prices:
    data=prices.read()

    # parse file
NPCPrices = json.loads(data)

	# loop
for x in (NPCPrices["productIds"]):  

    Product = x
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

    #make the prices to string
    frSellPrice = str(rSellPrice)  # float -> str
    frBuyPrice = str(rBuyPrice)  # float -> str

    #how big is the absolut difference?
    AbsoluteDifference = buyPrice - sellPrice
  #  print(AbsoluteDifference)
    #whats the average between the two numbers?
    AverageDifference = (sellPrice + buyPrice)/2
  #  print(AverageDifference)
    
    #Divide the difference by the average:
    Difference = (AbsoluteDifference / AverageDifference)*100

    rDifference = round(Difference, 1)
    strDifference = str(rDifference)

            #wstoring the difference and the product
    if Difference > 0:
    #add the value to a list
        toplist.append(strDifference + "% difference between the sell and buy price of " + readableName)      
        #print("appended")
        print("--------------------------------------")
    else:
        print("--------------------------------------")


#TupleTopList.sort(key = operator.itemgetter(0))
#toplist.sort(reverse=True)
sortedtoplist = humansorted(toplist)
sortedtoplist.reverse()


window = Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.title("Here are the results:")

def quit():
    window.destroy()

text = Text(window, height=20, width=100)
text.insert(INSERT, "Top 1: There is a " + sortedtoplist[0] + ". Easy flip!\n\nTop 2: There is a " + sortedtoplist[1] + ". Nice!\n\nTop 3: There is a " + sortedtoplist[2] + ".\n\nTop 4: There is a " + sortedtoplist[3] + ".\n\nTop 5: There is a " + sortedtoplist[4] + ".\n\nTop 6: There is a " + sortedtoplist[5] + ".\n\nTop 7: There is a " + sortedtoplist[6] + ".\n\nTop 8: There is a " + sortedtoplist[7] + ".\n\nTop 9: There is a " + sortedtoplist[8] + ".\n\nTop 10: There is a " + sortedtoplist[2] + ".")
text.pack()
text.config(state="disabled")
quit = Button(window, text="ok", command=quit).pack()




#print()

#print("Top 1: There is a " + sortedtoplist[0] + ". Easy flip!")
#print()

#print("Top 2: There is a " + sortedtoplist[1] + ". Nice!")
#print()

#print("Top 3: There is a " + sortedtoplist[2])
#print()

#print("Top 4: There is a " + sortedtoplist[3])
#print()

#print("Top 5: There is a " + sortedtoplist[4])#

#print()
#print()
#print("=====================")
#print("Buy me VIP, IGN: flimmerkraft")
#print("=====================")
#print()
#print()
