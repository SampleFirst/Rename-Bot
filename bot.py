import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5928894328:AAEJyrBTn0rYer7aP4JxIBlxfLcopTA9fC8")

API_ID = int(os.environ.get("API_ID", "23906038"))

API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")

STRING = os.environ.get("STRING", "BQFsxvYAcnMtxv-d_Xf4vONOIUj42RpvK02wRKDS9zWq4qz17tm1vcNra14hzF9lsUFw8SB78pgXGKNQaAMppm5r26-uCZB2RwNCJAygGYdgWRBOlJT1sb2bhgYTtVtZCorgOsGbR5Vzcgh5PgsulbPXFK5oja2dAzRt4lIra3KMm2OTxZE9jZMe8G4N9T41LNiE3eNycaWAeop1ke2SuXBYxQ-4UrZJYYCV6tgNKK6aqelYbERnASbOLGU9QBRx6A25x2TjXXj7gFVF75QPig62CBoVXBkcjtX0I5d8WUVZyrrLuiRKw70RQaS1IMhw59TI8vfEYzlJuwYmAQ2TIqdM51JS1wAAAAFhY794AQ")



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
