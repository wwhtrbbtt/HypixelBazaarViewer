BotToken = "NzA5Mzg2MTQ0NTU0NjgwMzYw.Xs1_Dg.AZ0LzmwKQEppZJYXeOJIxVbH69s"

import time
import random
import discord
from discord.utils import get

hour = 3600

client = discord.Client()


@client.event

async def on_ready():

    activity = discord.Game(name="$minions")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$minions'):
        global minion_upgrade
        diamond_spreading = False
        while True:
            try:
                await message.channel.send("Please enter minion's time between actions in seconds.")
                time.sleep(1)
                RAWaction_time = await client.wait_for('message', timeout=20)
                
                action_time = float(RAWaction_time.content)
                check = 1/action_time
                break
            except:
                pass


        while True:
            try:
                await message.channel.send('Please enter the sell price of 1 item.')
                time.sleep(1)
                RAWprice_per = await client.wait_for('message', timeout=20)
                price_per = float(RAWprice_per.content)
                check = 1 / price_per
                break
            except:
                pass

        while True:
            try:
                await message.channel.send("Please enter the amount of items obtained per action.")
                time.sleep(1)
                RAWitems_per_action = await client.wait_for('message', timeout=20)
                items_per_action = float(RAWitems_per_action.content)
                check = 1 / items_per_action
                break
            except:
                pass


        while True:
            try:
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="Please choose your minion fuel. *Fuel duration is not taken into calculation*", color=color)
                embed.add_field(name="1:", value="Coal", inline=False)
                embed.add_field(name="2:", value="Block of coal", inline=False)
                embed.add_field(name="3:", value="E-bread", inline=False)
                embed.add_field(name="4:", value="E-coal", inline=False)
                embed.add_field(name="5:", value="Solar panel", inline=False)
                embed.add_field(name="6:", value="E-lava bucked", inline=False)
                embed.add_field(name="7:", value="Hamster wheel", inline=False)
                embed.add_field(name="8:", value="Foul flesh", inline=False)
                embed.add_field(name="9:", value="E-charcoal", inline=False)
                embed.add_field(name="10:", value="None", inline=False)           
                strColor = str(color)
                embed.set_footer(text="Color: " + strColor)
                await message.channel.send(embed=embed)
                time.sleep(1)
                RAWfuel_answer = await client.wait_for('message', timeout=20)
            
                fuel_answer = float(RAWfuel_answer.content)
                check = 1 / fuel_answer
                break
            except:
                pass


        while True:
            try:
                    color = random.randint(0, 0xffffff)
                    embed = discord.Embed(title="Please choose a minion upgrade.", color=color)
                    embed.add_field(name="1:", value="Diamond spreading", inline=False)
                    embed.add_field(name="2:", value="Flycatcher", inline=False)
                    embed.add_field(name="3:", value="Minion expander", inline=False)
                    embed.add_field(name="4:", value="None", inline=False)
                    strColor = str(color)
                    embed.set_footer(text="Color: " + strColor)
                    await message.channel.send(embed=embed)
                    time.sleep(3)
                    RAWupgrade_answer = await client.wait_for('message', timeout=20)
                    upgrade_answer = int(RAWupgrade_answer.content)
                    check = 1 / upgrade_answer
                    if upgrade_answer == 1:
                        diamond_spreading = True
                        minion_upgrade = 0
                    elif upgrade_answer == 2:
                        minion_upgrade = 0.20
                    elif upgrade_answer == 3:
                        minion_upgrade = 0.05
                    elif upgrade_answer == 4:
                        minion_upgrade = 0
                    break
            except:
                pass

        while True:
            try:
                await message.channel.send('How many minions are you using?')
                time.sleep(1)
                RAWMinion_amount = await client.wait_for('message', timeout=20)
                minion_amount = float(RAWMinion_amount.content)
                check = 1 / minion_amount
                break
            except:
                pass

        if fuel_answer == 1:
            minion_fuel = 1.05          #Coal
        elif fuel_answer == 2:
            minion_fuel = 1.05          #Block of coal
        elif fuel_answer == 3:
            minion_fuel = 1.05          #E bread
        elif fuel_answer == 4:
            minion_fuel = 1.10          #E coal
        elif fuel_answer == 5:
            minion_fuel = 1.25          #Solar Panel
        elif fuel_answer == 6:
            minion_fuel = 1.25          #E lava bucket
        elif fuel_answer == 7:
            minion_fuel = 1.50          #Hamster Wheel
        elif fuel_answer == 8:
            minion_fuel = 1.90          #Foul flesh
        elif fuel_answer == 9:
            minion_fuel = 1.20          #E charcoal
        elif fuel_answer == 10:
            minion_fuel = 1             #None
        else:
            await message.channel.send('I do not understand! Fuel set to None')
            minion_fuel = 1




        fuel_efficency = 1 / minion_fuel
        upgrade_efficiency = 1 / (minion_upgrade + 1)
        action_time = action_time * fuel_efficency * upgrade_efficiency
        actions_per_hour = hour / action_time
        items_per_hour = actions_per_hour * items_per_action
        profit_per_hour = items_per_hour * minion_amount * price_per

        if diamond_spreading == True:
            spreding_money = items_per_hour / 10 * 8 * minion_amount
            profit_per_hour = profit_per_hour + spreding_money





        profit_per_day = profit_per_hour * 24
        profit_per_week = profit_per_day * 7

        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Profit:", color=color)
        embed.add_field(name="Profit per hour:", value="$"+'{:20,.2f}'.format(profit_per_hour).replace(" ", ''), inline=False)
        embed.add_field(name="Profit per day:", value="$"+'{:20,.2f}'.format(profit_per_day).replace(" ", ''), inline=False)
        embed.add_field(name="Profit per week:", value="$"+'{:20,.2f}'.format(profit_per_week).replace(" ", ''), inline=False)

        strColor = str(color)
        embed.set_footer(text="Color: " + strColor)
        await message.channel.send(embed=embed)

client.run(BotToken)
