import requests, json
from natsort import humansorted
import sys
from discord_webhook import DiscordWebhook

sys.path.insert(1, 'Modules')
def ApiIsDown():
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/732189603586637885/3hL2lAoDpZMhrT_xcTdrWXJ3KHULgCWEOg_bfmEQqrB54N8C0kZeyYAnd7MDE-mIIBCU', content='The slothpixel api I use is down. Please try again later. Proof:\nhttps://api.slothpixel.me/api/skyblock/items')
    response = webhook.execute()

def NPCPrices():
        with open('Prices.json', 'r') as prices:
            data=prices.read()
            # parse file
        NPCPrices = json.loads(data)
        return NPCPrices

def Request(Product):           
        file = open('ItemsToAdd.txt', 'a')
        file.write("You have to add: " + Product + ".")
        file.write("\n")
        file.close()
        
def JSONData():
    try:
        r = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/', timeout=3)
        return r.json()
    except:
        ApiIsDown()
        return
def percent(a, b) : 
  
    result = int(((b - a) * 100) / a) 
  
    return result 
    
def NormalName(Product):
    with open('Prices.json', 'r') as prices:
            data=prices.read()
            # parse file
    NPCPrices = json.loads(data)
    try:
        NormalName = NPCPrices["productIds"][Product]["NormalName"]
        return NormalName
    except:
        return "error"

def PrettyNumbers(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def PrettyItem(item):
        try:
            r = requests.get('https://api.slothpixel.me/api/skyblock/items/', timeout=3)
            if r.status_code != 200:
                ApiIsDown()
                return
            elif r.status_code == 200:
                return r.json()
            return r.json()[item]["name"]
        except:
                print("WRONG ITEM")

def Readable(item):
    r = requests.get('https://api.slothpixel.me/api/skyblock/items', timeout=3)
    if r.status_code != 200:
        ApiIsDown()
        return
    elif r.status_code == 200:
        return r.json()[item]["name"]

def AllItems():
    with open('ItemNames.json', 'r') as prices:
        data=prices.read()
    # parse file
    jsonData = json.loads(data)
    return jsonData

def ItemId(item):
    with open('ItemNames.json', 'r') as prices:
        data=prices.read()
    # parse file
    jsonData = json.loads(data)
    try:
        for x in jsonData["items"]:
            if x["CleanName"] == item:
                  return x["Name"]
    except: 
        return item

