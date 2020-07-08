url = "https://discordapp.com/api/webhooks/713684844781109298/V3DXYRT7Mm01ht8h9_Uld4kotwW5B7KkM6WjyWwKC830lRTaPSNNrN625Hq59vL0_xsm"

import random
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
sys.path.insert(1, 'Modules')
from formular import Score


while True:
        list = Score()
        item = (list[0].split("**")[1]) # the item
        #score = (list[0].split()[3])
        #print("========")

        time.sleep(60)
        
        list = Score()
        
        newItem = (list[0].split("**")[1]) # the item
        
        if not item == newItem:
            print("NEW BEST ITEM!")
            color = random.randint(0, 0xffffff)

            webhook = DiscordWebhook(url=url)
            
            embed = DiscordEmbed(title="New best item:", color=color)
            embed.set_author(name="p337", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
            embed.add_embed_field(name="New item with the best skyscore is " + newItem, value="<@585935919224324117> The new best item is " + newItem + ". The skyscore is " + list[0].split()[3] + ".", inline=False)
            embed.set_footer(text="Color: " + str(color))
            embed.set_timestamp()
            webhook.add_embed(embed)
            
            response = webhook.execute()
