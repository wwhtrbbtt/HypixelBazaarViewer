url = "https://discordapp.com/api/webhooks/716722593457242123/GyoS587uBLbY5bEJEn-674HVK5egSm2gv5IzUubThzKC0I1CSoT6LZIoMqJiexQQRZHw"

from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
import random
from random import randint
import time
sys.path.insert(1, 'Modules')

from eFlip import eFlip

def SendEflip():
    # create embed object for webhook
    sortedtoplist = eFlip()
    color = random.randint(0, 0xffffff)
    
    webhook = DiscordWebhook(url=url)
    
    embed = DiscordEmbed(title="Flip and enchant:", color=color)
    embed.set_author(name="p337", icon_url="https://cdn.discordapp.com/attachments/703719065977487390/708392264086585364/yeeeeeeeeee.png")
    embed.add_embed_field(name="Best thing to flip and enchant rn:", value=sortedtoplist[0], inline=False)
    embed.set_footer(text="Color: " + str(color))
    embed.set_timestamp()
    webhook.add_embed(embed)
    
    response = webhook.execute()

def here():
    webhook = DiscordWebhook(url=WebHook, content="@here ⬆️")
    response = webhook.execute()
#def SendPriceDifference():
#    # create embed object for webhook
#    sortedtoplist = PriceDifference()
#    webhook = DiscordWebhook(url=WebHook, content=sortedtoplist[randint(3, 6)])
#    response = webhook.execute()


x = 0
while x == 0:
    SendEflip()
    print("worked!")
    #here()
    time.sleep(10)

