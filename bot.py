import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5928894328:AAFCa2ZETdgCcl_RtGAHjJwH38AozzU90vY")

API_ID = int(os.environ.get("API_ID", "23906038"))

API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")

STRING = os.environ.get("STRING", "BQBWC-YgBcRxpozGiNOoWAzRkCQi94XPmy4X_o7kHCeELPl4FCNpRYgs3sHARgetk3qcwn5t6UktT1JRijj-BP4v9C87daGrWsje7GvmpdMEvZPMzG_InqlavMT5Gys1G8KAhMKxSpXDoR4a5l2KzUDdRMLZKRme5uBtIYv-BKJjr46jYqLHRpc4j4BPLHCDhzx4IZzbyEWD7e4Xatm61YFadi7Le6MBQl3W1uoMD3YIImKPQrx7J5RxZITpirULLW6l9hAYBD-8y1YNZPAndBBztmSlSM7w0x_kxZYh2Lbe-6IN05aBJdhSQDKGJHeSVPsEKZM8g32YhEnGMw6xm7ooAAAAATb5mV4A")



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
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
