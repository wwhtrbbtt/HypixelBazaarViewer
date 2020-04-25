import requests
import json

#ApiKey: INSERT YOUR API KEY HERE
print("This program will spit out every item you can sell/buy at the bazaar.")
print("these are the names for the items, that the programms from Hypixel (and from me) use.")
print("but on the BaazarViewer.py, you can use normal names like `brown pumpkin`")
print("not every item you will see here, is supported ATM.")
print("This tool will need your ApiKey, please insert it below")
ApiKey = input("Your ApiKey?\n")

payload = {'key': ApiKey}
r = requests.get('https://api.hypixel.net/skyblock/bazaar/products?', params=payload)

JSONData = (r.json())
result = str(JSONData)

for x in r.json()["productIds"]: print(x)

    #This is for me, so i can easily insert the json stuff. It will print ### behind every name
#for x in r.json()["productIds"]: print(x + "###")
