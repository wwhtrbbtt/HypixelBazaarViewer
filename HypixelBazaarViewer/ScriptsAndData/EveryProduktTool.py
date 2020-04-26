import requests
import json
import sys
sys.path.insert(1, 'ScriptsAndData')

with open('ApiKeyInHere.txt', 'r') as KeyTXT:
  ApiKey = KeyTXT.read()

print("This program will spit out every item you can sell/buy at the bazaar.")
print("these are the names for the items, that the programms from Hypixel (and from me) use.")
print("but on the BaazarViewer.py, you can use normal names like `brown pumpkin`")
print("not every item you will see here, is supported ATM.")
print()
print()



#        Every item from the API:

payload = {'key': ApiKey}
r = requests.get('https://api.hypixel.net/skyblock/bazaar/products?', params=payload)

JSONData = (r.json())
result = str(JSONData)

for x in r.json()["productIds"]: print(x)

    #This is for me, so i can easily insert the json stuff. It will print ### behind every name
#for x in r.json()["productIds"]: print(x + "###")


#           Every Item from my list

print()
print("------------------------------------")
print("Every item in MY list (currently supported):")
print()
    # read file
with open('Prices.json', 'r') as prices:
    data=prices.read()

    # parse file
NPCPrices = json.loads(data)

#loop
for x in (NPCPrices["productIds"]): print(x)
