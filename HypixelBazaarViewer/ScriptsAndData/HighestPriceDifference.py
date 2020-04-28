import requests
import json
import sys
from natsort import humansorted


toplist = []
sys.path.insert(1, 'ScriptsAndData')

print()

    #Getting the ApiKey (Your ApiKey will not be sended anywhere! Read the code!)
with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()
#print(ApiKey)

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

print()

print("Top 1: There is a " + sortedtoplist[0] + ". Easy flip!")
print()

print("Top 2: There is a " + sortedtoplist[1] + ". Nice!")
print()

print("Top 3: There is a " + sortedtoplist[2])
print()

print("Top 4: There is a " + sortedtoplist[3])
print()

print("Top 5: There is a " + sortedtoplist[4])

print()
print()
print("=====================")
print("Buy me VIP, IGN: flimmerkraft")
print("=====================")
print()
print()
