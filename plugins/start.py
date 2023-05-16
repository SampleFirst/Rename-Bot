from datetime import date as date_
import datetime
import pytz
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "TrueDealsMaster")
STRING = os.environ.get("STRING", "BQFsxvYAcnMtxv-d_Xf4vONOIUj42RpvK02wRKDS9zWq4qz17tm1vcNra14hzF9lsUFw8SB78pgXGKNQaAMppm5r26-uCZB2RwNCJAygGYdgWRBOlJT1sb2bhgYTtVtZCorgOsGbR5Vzcgh5PgsulbPXFK5oja2dAzRt4lIra3KMm2OTxZE9jZMe8G4N9T41LNiE3eNycaWAeop1ke2SuXBYxQ-4UrZJYYCV6tgNKK6aqelYbERnASbOLGU9QBRx6A25x2TjXXj7gFVF75QPig62CBoVXBkcjtX0I5d8WUVZyrrLuiRKw70RQaS1IMhw59TI8vfEYzlJuwYmAQ2TIqdM51JS1wAAAAFhY794AQ")
ADMIN = int(os.environ.get("ADMIN", 5217294686))
bot_username = os.environ.get("BOT_USERNAME","PremiumRenameBot")
log_channel = int(os.environ.get("LOG_CHANNEL", "-1001898316484"))
token = os.environ.get('TOKEN', '5928894328:AAEJyrBTn0rYer7aP4JxIBlxfLcopTA9fC8')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/4488a1891072c63fed940.jpg")


# Set the timezone to Indian Standard Time
ist_tz = pytz.timezone('Asia/Kolkata')
currentTime = datetime.datetime.now(ist_tz)

if currentTime.hour < 12:
    wish = "❤️ 𝗚𝗼𝗼𝗱 𝗠𝗼𝗿𝗻𝗶𝗻𝗴 ❤️"
elif 12 <= currentTime.hour < 16:
    wish = '🤍 𝗚𝗼𝗼𝗱 𝗔𝗳𝘁𝗲𝗿𝗻𝗼𝗼𝗻 🤍'
else:
    wish = '💙 𝗚𝗼𝗼𝗱 𝗘𝘃𝗲𝗻𝗶𝗻𝗴 💙'

print(wish)

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""𝗛𝗲𝗹𝗹𝗼 {wish} {message.from_user.first_name } \n\n𝗜 𝗮𝗺 𝗳𝗶𝗹𝗲 𝗿𝗲𝗻𝗮𝗺𝗲𝗿 𝗯𝗼𝘁, 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝘁 𝗮𝗻𝘆 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗢𝗿 𝗩𝗶𝗱𝗲𝗼 𝗮𝗻𝗱 𝗲𝗻𝘁𝗲𝗿 𝗻𝗲𝘄 𝗳𝗶𝗹𝗲𝗻𝗮𝗺𝗲 𝘁𝗼 𝗿𝗲𝗻𝗮𝗺𝗲 𝗶𝘁"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('🔔 ᴜᴘᴅᴀᴛᴇ', url='https://t.me/iPepkornBots'),
        InlineKeyboardButton('💁‍♂️ sᴜᴘᴘᴏʀᴛ', url='https://t.me/iPapkornSupportGroup')
        ]] )
        )
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('🔔 ᴜᴘᴅᴀᴛᴇ', url='https://t.me/iPepkornBots'),
        InlineKeyboardButton('💁‍♂️ sᴜᴘᴘᴏʀᴛ', url='https://t.me/iPapkornSupportGroup')
        ]] )
        )
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 100MB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	𝗛𝗲𝗹𝗹𝗼 {wish} {message.from_user.first_name } \n\n𝗜 𝗮𝗺 𝗳𝗶𝗹𝗲 𝗿𝗲𝗻𝗮𝗺𝗲𝗿 𝗯𝗼𝘁, 𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝘁 𝗮𝗻𝘆 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗢𝗿 𝗩𝗶𝗱𝗲𝗼 𝗮𝗻𝗱 𝗲𝗻𝘁𝗲𝗿 𝗻𝗲𝘄 𝗳𝗶𝗹𝗲𝗻𝗮𝗺𝗲 𝘁𝗼 𝗿𝗲𝗻𝗮𝗺𝗲 𝗶𝘁""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('🔔 ᴜᴘᴅᴀᴛᴇ', url='https://t.me/iPepkornBots'),
        InlineKeyboardButton('💁‍♂️ sᴜᴘᴘᴏʀᴛ', url='https://t.me/iPapkornSupportGroup')
        ]] )
        )
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__You are not subscribed my channel__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"✨ #RenameBot_LOGS ✨,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Use About cmd first /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"Hello dear {message.from_user.first_name}  **we are currently working on this issue**\n\nPlease try to rename files from your another account.\nBecause this BOT can't rename file sent by some ids.\n\nIf you are an **ADMIN** Don't worry ! here we have a solution for you dear {message.from_user.first_name }.\n\nPlease use \n👉 `/addpremium your_other_userid` 👈 to use premium feautres\n\n",
reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('🔔 ᴜᴘᴅᴀᴛᴇ', url='https://t.me/iPepkornBots'),
        InlineKeyboardButton('💁‍♂️ sᴜᴘᴘᴏʀᴛ', url='https://t.me/iPapkornSupportGroup')
        ]] )
        )
        await message.reply_text(text=f"🦋")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 600
    else:
        LIMIT = 50
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% of daily {humanbytes(limit)} data quota exhausted.\n\n  File size detected {humanbytes(file.file_size)}\n  Used Daily Limit {humanbytes(used)}\n\nYou have only **{humanbytes(remain)}** left on your Account.\nIf U Want to Rename Large File Upgrade Your Plan ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daily Limit {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Can't upload files bigger than 2GB ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
