import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5928894328:AAEJyrBTn0rYer7aP4JxIBlxfLcopTA9fC8")

API_ID = int(os.environ.get("API_ID", "23906038"))

API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")

STRING = os.environ.get("STRING", "BQFsxvYAn0pCNhN1DtMfBjJ2UwwX_jGfMCS16-ZmtKNJZQe04sDxV4365jF-arTefuqULGONyRR8lBwESaoXWkANfDEHAOYkA4lvSSbJnkN6aDVFp907xc8veH_0OldQkQ27iTspSzEp9XeY9lLB-BUDNGmtKl2HzEaKqlMB4GJihifzTmxbx_CdstUz4nOOsoSeysSFki2a_i0GLEP1AgA3UqjhkAHV8vrb4516lGJar6te8lOVbM5J-rVTeveRWMTMlnC40f_vb1OIDxt-g7Ro3bOnRlD1Wjg11ZZVRXMAkqA9Iu8u0W_4KEus5ocuAcIn1HKf5PnJerwDRNAKGHy7qL0gkwAAAAFhY794AQ")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()

    # Export the session string for the bot
    session_string = bot.export_session_string()
    print(session_string)

    # Keep the bot running
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
