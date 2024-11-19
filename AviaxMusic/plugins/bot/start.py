import asyncio
import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo
import config
from AviaxMusic import app
from AviaxMusic.misc import _boot_
from AviaxMusic.plugins.sudo.sudoers import sudoers_list
from AviaxMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AviaxMusic.utils import bot_sys_stats
from AviaxMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AviaxMusic.utils.decorators.language import LanguageStart
from AviaxMusic.utils.formatters import get_readable_time
from AviaxMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

#--------------------------

NEXI_VID = [
"https://envs.sh/pYY.mp4",
"https://envs.sh/pC0.mp4",
"https://envs.sh/pFS.mp4", 
"https://envs.sh/pYG.mp4", 
"https://envs.sh/_Z5.mp4", 
"https://envs.sh/_ZG.mp4", 
"https://envs.sh/_Z9.mp4", 

]



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    
    # Sending initial emoji
    msg = await message.reply_sticker("CAACAgUAAxkDAAIEoWcm-PmfbFGDQWZ7u5kyCQUfqzFiAAIeCgACya4ZVWcoG8RVlky8NgQ")
    await asyncio.sleep(2) 
    # Repeat the cycle of emojis three times
    
    await msg.delete()
    

    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_video(
                random.choice(NEXI_VID),
                caption=_["help_1"].format(config.SUPPORT_GROUP),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_GROUP),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        await message.reply_video(
            random.choice(NEXI_VID),
            caption="(⁠θ⁠‿⁠θ⁠) {0} \n\n● 𝙼𝚎𝚎𝚝 𝐅𝐮𝐛𝐮𝐤𝐢 ʏᴏᴜʀ ᴀʟʟ ɪɴ ᴏɴᴇ ʙᴏᴛ, ʀᴇᴀᴅʏ ᴛᴏ ᴛᴜʀɴ ᴜᴘ ᴛʜᴇ ʜᴇᴀᴛ.\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n◇ sʜᴇ ᴋɴᴏᴡs ᴇxᴀᴄᴛʟʏ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ—sᴛʀᴇᴀᴍɪɴɢ 𝐦𝐮𝐬𝐢𝐜 ғʀᴏᴍ ᴀʟʟ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇs, 𝐦𝐚𝐧𝐚𝐠𝐢ɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴡɪᴛʜ ᴀ sᴜʟᴛʀʏ ғɪɴᴇssᴇ.\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n◇ 𝐒𝐦𝐨𝐨𝐭𝐡, 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥, 𝐞𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭, 𝐅𝐮𝐛𝐮𝐤𝐢 ᴡɪʟʟ ᴛᴀᴋᴇ ᴄᴏɴᴛʀᴏʟ ᴡʜɪʟᴇ ʏᴏᴜ sɪᴛ ʙᴀᴄᴋ, ʀᴇʟᴀx, ᴀɴᴅ ʟᴇᴛ ʜᴇʀ ᴡᴏʀᴋ ʜᴇʀ ᴍᴀɢɪᴄ.\n━━━━━━━━━━━━━━━━━━━━━━━━━".format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start","fubuki"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_video(
        random.choice(NEXI_VID),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_GROUP,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_video(
                    random.choice(NEXI_VID),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
