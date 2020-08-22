import requests
def Watchdog():
    json = requests.get("https://api.slothpixel.me/api/bans").json()
    return(
    "`[WATCHDOG ANNOUNCEMENT]`\n"
    "I banned `" + str(json["watchdog"]["total"]) +"` players in total.\n"
    "Staff have banned an additional `" + str(json["staff"]["total"]) + "` in total!\n"
    "Banwaves occur every few hours.\n"
    "Blacklisted modifications are a bannable offense!")
