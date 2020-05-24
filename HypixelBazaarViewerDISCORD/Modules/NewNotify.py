import json
import sys
from SmallDefs import *
import os
from CheckingProducts import CheckProducts

sys.path.insert(1, 'Modules')

NPCPrices = NPCPrices()

def NewNotify(Product, Person, Price, buysell):
	#checking if file exists, creating if it doesnt
	if not os.path.exists('ToCheck.json'):
		with open('ToCheck.json', "w"): pass

	Product = NPCPrices["productIds"][Product]["NormalName"]
	print(Product)
	data = {}
	data[Product] = []
	data[Product].append({
	     'DiscordTag': Person,
	     'Price': Price,
	     'buysell': buysell
	     	})

	print(data)
	with open('ToCheck.json', 'a') as f:  # writing JSON object
		json.dump(data, f)

	#CheckProducts()
