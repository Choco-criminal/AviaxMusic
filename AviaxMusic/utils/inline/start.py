from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app
import config

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters
from AviaxMusic.utils import *
import config
from AviaxMusic import app

# Start panel buttons
from pyrogram.types import InlineKeyboardButton

import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
          
        
        [
            InlineKeyboardButton(
                text="ᴍᴜsɪᴄ", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="Management", callback_data="management_action"),
        ], 
              
            [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
            ], 
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="Management", callback_data="management_action"),  # New "Management" button
        ],
    ]
    return buttons

# Management panel buttons for a given page
# Management panel buttons for a given page
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



def management_panel_buttons(page_num):
    # Define the commands for all buttons in order
    buttons = [
        InlineKeyboardButton("A-spam", callback_data="ANTISPAM_HELP"), InlineKeyboardButton("A-raid", callback_data="RAID_HELP"), InlineKeyboardButton("A-flood", callback_data="ANTIFLOOD_HELP"), InlineKeyboardButton("A-channel", callback_data="ACHANNEL_HELP"), InlineKeyboardButton("Afk", callback_data="AFK_HELP"), InlineKeyboardButton("Admin", callback_data="ADMIN_HELP"), InlineKeyboardButton("Approval", callback_data="APPROVE_HELP"), InlineKeyboardButton("B-list", callback_data="BLACKLIST_HELP"), InlineKeyboardButton("B-users", callback_data="BUSER_HELP"), InlineKeyboardButton("Backup", callback_data="BACKUP_HELP"), InlineKeyboardButton("Cinfo", callback_data="CINFO_HELP"), InlineKeyboardButton("Clean", callback_data="CLEANER_HELP"), InlineKeyboardButton("Connect", callback_data="CONNECTIONS_HELP"), InlineKeyboardButton("Disable", callback_data="DISABLE_HELP"), InlineKeyboardButton("Db-clean", callback_data="DBCLEAN_HELP"), InlineKeyboardButton("F-sub", callback_data="FSUB_HELP"), InlineKeyboardButton("Filters", callback_data="CUST_FILTERS_HELP"), InlineKeyboardButton("Feds", callback_data="FEDS_HELP"), InlineKeyboardButton("G-cast", callback_data="GCAST_HELP"), InlineKeyboardButton("Info", callback_data="USERINFO_HELP"), InlineKeyboardButton("Logs", callback_data="LOG_HELP"), InlineKeyboardButton("Locks", callback_data="LOCKS_HELP"), InlineKeyboardButton("Muting", callback_data="MUTING_HELP"), InlineKeyboardButton("N-mode", callback_data="NMODE_HELP"), InlineKeyboardButton("Notes", callback_data="NOTES_HELP"), InlineKeyboardButton("Owner", callback_data="OWNER_HELP"), InlineKeyboardButton("Pins", callback_data="PINS_HELP"), InlineKeyboardButton("Ping", callback_data="PING_HELP"), InlineKeyboardButton("Purge", callback_data="PURGE_HELP"), InlineKeyboardButton("Quotly", callback_data="QUOTLY_HELP"), InlineKeyboardButton("Sticker", callback_data="STICKER_HELP"), InlineKeyboardButton("Translator", callback_data="GTRANSLATE_HELP"), InlineKeyboardButton("Truth-Dare", callback_data="TD_HELP"), InlineKeyboardButton("Tag-All", callback_data="TAGS_HELP"), InlineKeyboardButton("Uall", callback_data="USERINFO_HELP"), InlineKeyboardButton("Warns", callback_data="WARNS_HELP"), InlineKeyboardButton("Welcome", callback_data="WELCOME_HELP"), InlineKeyboardButton("Zombies", callback_data="ZOMBIES_HELP")    ]
    
    # Number of buttons per page (3 buttons per row, 5 rows per page -> 15 buttons per page)
    buttons_per_page = 15
    total_pages = (len(buttons) + buttons_per_page - 1) // buttons_per_page  # Calculate total number of pages

    # Get the buttons for the current page
    start_index = (page_num - 1) * buttons_per_page
    end_index = start_index + buttons_per_page
    page_buttons = buttons[start_index:end_index]

    # Split the buttons into rows of 3
    keyboard = [page_buttons[i:i+3] for i in range(0, len(page_buttons), 3)]

    # Add navigation buttons (Previous, Next, Close)
    nav_buttons = []
    if page_num > 1:
        nav_buttons.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"management_page_{page_num - 1}"))
    if page_num < total_pages:
        nav_buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"management_page_{page_num + 1}"))
    nav_buttons.append(InlineKeyboardButton("Close ❌", callback_data="settingsback_helper"))
    
    # Add navigation buttons as the last row
    keyboard.append(nav_buttons)

    return InlineKeyboardMarkup(keyboard)


# Callback query handler for Antispam help
@app.on_callback_query(filters.regex("ANTISPAM_HELP"))
async def antispam_help(client: Client, callback_query: CallbackQuery):
    antispam_message =  """
  •➥ *ᴀᴅᴍɪɴs ᴏɴʟʏ:*
  •➥ /antispam <on/off/yes/no>: ᴡɪʟʟ ᴛᴏɢɢʟᴇ ᴏᴜʀ ᴀɴᴛɪsᴘᴀᴍ ᴛᴇᴄʜ ᴏʀ ʀᴇᴛᴜʀɴ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ    sᴇᴛᴛɪɴɢs.
  ᴀɴᴛɪ-sᴘᴀᴍ, ᴜsᴇᴅ ʙʏ ʙᴏᴛ ᴅᴇᴠs ᴛᴏ ʙᴀɴ sᴘᴀᴍᴍᴇʀs ᴀᴄʀᴏss ᴀʟʟ ɢʀᴏᴜᴘs. ᴛʜɪs ʜᴇʟᴘs ᴘʀᴏᴛᴇᴄᴛ \
  ʏᴏᴜ ᴀɴᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘs ʙʏ ʀᴇᴍᴏᴠɪɴɢ sᴘᴀᴍ ғʟᴏᴏᴅᴇʀs ᴀs ǫᴜɪᴄᴋʟʏ ᴀs ᴘᴏssɪʙʟᴇ
  
  ɴᴏᴛᴇ: ᴜsᴇʀs ᴄᴀɴ ᴀᴘᴘᴇᴀʟ ɢʙᴀɴs ᴏʀ ʀᴇᴘᴏʀᴛ sᴘᴀᴍᴍᴇʀs ᴀᴛ 
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antispam_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for A-raid
@app.on_callback_query(filters.regex("RAID_HELP"))
async def a_raid(client: Client, callback_query: CallbackQuery):
    a_raid_message = """
  ᴇᴠᴇʀ ʜᴀᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʀᴀɪᴅᴇᴅ ʙʏ sᴘᴀᴍᴍᴇʀs ᴏʀ ʙᴏᴛs?
  Tʜɪs ᴍᴏᴅᴜʟᴇ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ǫᴜɪᴄᴋʟʏ sᴛᴏᴘ ᴛʜᴇ ʀᴀɪᴅᴇʀs
  Bʏ ᴇɴᴀʙʟɪɴɢ *ʀᴀɪᴅ ᴍᴏᴅᴇ* I ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴋɪᴄᴋ ᴇᴠᴇʀʏ ᴜsᴇʀ ᴛʜᴀᴛ ᴛʀɪᴇs ᴛᴏ ᴊᴏɪɴ
  Wʜᴇɴ ᴛʜᴇ ʀᴀɪᴅ ɪs ᴅᴏɴᴇ ʏᴏᴜ ᴄᴀɴ ᴛᴏɢɢʟᴇ ʙᴀᴄᴋ ʟᴏᴄᴋɢʀᴏᴜᴘ ᴀɴᴅ ᴇᴠᴇʀʏᴛʜɪɴɢ ᴡɪʟʟ ʙᴇ ʙᴀᴄᴋ ᴛᴏ  ɴᴏʀᴍᴀʟ.
  
  *Aᴅᴍɪɴs ᴏɴʟʏ!* 
  •➥ /raid `(ᴏғғ/ᴛɪᴍᴇ ᴏᴘᴛɪᴏɴᴀʟ)` : ᴛᴏɢɢʟᴇ ᴛʜᴇ ʀᴀɪᴅ ᴍᴏᴅᴇ (ᴏɴ/ᴏғғ)
  ɪғ ɴᴏ ᴛɪᴍᴇ ɪs ɢɪᴠᴇɴ ɪᴛ ᴡɪʟʟ ᴅᴇғᴀᴜʟᴛ ᴛᴏ 2 ʜᴏᴜʀs ᴛʜᴇɴ ᴛᴜʀɴ ᴏғғ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
  ʙʏ ᴇɴᴀʙʟɪɴɢ *ʀᴀɪᴅ ᴍᴏᴅᴇ* I ᴡɪʟʟ ᴋɪᴄᴋ ᴇᴠᴇʀʏ ᴜsᴇʀ ᴏɴ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ɢʀᴏᴜᴘ.
  •➥ /raidtime (ᴛɪᴍᴇ ᴏᴘᴛɪᴏɴᴀʟ) : ᴠɪᴇᴡ ᴏʀ sᴇᴛ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ᴅᴜʀᴀᴛɪᴏɴ ғᴏʀ ʀᴀɪᴅ ᴍᴏᴅᴇ, ᴀғᴛᴇʀ  ᴛʜᴀᴛ ᴛɪᴍᴇ ғʀᴏᴍ ᴛᴏɢɢʟɪɴɢ ᴛʜᴇ ʀᴀɪᴅ ᴍᴏᴅᴇ ᴡɪʟʟ ᴛᴜʀɴ ᴏғғ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
  Dᴇғᴀᴜʟᴛ ɪs 6 ʜᴏᴜʀs
  •➥ /raidactiontime `(ᴛɪᴍᴇ ᴏᴘᴛɪᴏɴᴀʟ)` : ᴠɪᴇᴡ ᴏʀ sᴇᴛ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ᴅᴜʀᴀᴛɪᴏɴ ᴛʜᴀᴛ ᴛʜᴇ ʀᴀɪᴅ    ᴍᴏᴅᴇ ᴡɪʟʟ ᴛᴇᴍᴘʙᴀɴ ᴅᴇғᴀᴜʟᴛ ɪs 1 ʜᴏᴜʀ
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(a_raid_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Antiflood help
@app.on_callback_query(filters.regex("ANTIFLOOD_HELP"))
async def antiflood_help(client: Client, callback_query: CallbackQuery):
    antiflood_message = """
  •➥ *ᴀᴅᴍɪɴs ᴏɴʟʏ:*
  •➥ /antispam <on/off/yes/no>: ᴡɪʟʟ ᴛᴏɢɢʟᴇ ᴏᴜʀ ᴀɴᴛɪsᴘᴀᴍ ᴛᴇᴄʜ ᴏʀ ʀᴇᴛᴜʀɴ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs.
  ᴀɴᴛɪ-sᴘᴀᴍ, ᴜsᴇᴅ ʙʏ ʙᴏᴛ ᴅᴇᴠs ᴛᴏ ʙᴀɴ sᴘᴀᴍᴍᴇʀs ᴀᴄʀᴏss ᴀʟʟ ɢʀᴏᴜᴘs. ᴛʜɪs ʜᴇʟᴘs ᴘʀᴏᴛᴇᴄᴛ 
  ʏᴏᴜ ᴀɴᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘs ʙʏ ʀᴇᴍᴏᴠɪɴɢ sᴘᴀᴍ ғʟᴏᴏᴅᴇʀs ᴀs ǫᴜɪᴄᴋʟʏ ᴀs ᴘᴏssɪʙʟᴇ
  ɴᴏᴛᴇ: ᴜsᴇʀs ᴄᴀɴ ᴀᴘᴘᴇᴀʟ ɢʙᴀɴs ᴏʀ ʀᴇᴘᴏʀᴛ sᴘᴀᴍᴍᴇʀs ᴀᴛ 
  •➥ /flood: ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴀɴᴛɪғʟᴏᴏᴅ sᴇᴛᴛɪɴɢs
  •➥ /setflood <number/off/no>: sᴇᴛ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ᴀғᴛᴇʀ ᴡʜɪᴄʜ ᴛᴏ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏɴ ᴀ ᴜsᴇʀ. sᴇᴛ ᴛᴏ '0', 'off', or 'no' ᴛᴏ ᴅɪsᴀʙʟᴇ.
  •➥ /setfloodmode <ᴀᴄᴛɪᴏɴ ᴛʏᴘᴇ>: ᴄʜᴏᴏsᴇ ᴡʜɪᴄʜ ᴀᴄᴛɪᴏɴ ᴛᴏ ᴛᴀᴋᴇ ᴏɴ ᴀ ᴜsᴇʀ ᴡʜᴏ ʜᴀs ʙᴇᴇɴ ғʟᴏᴏᴅɪɴɢ. ᴏᴘᴛɪᴏɴs: ban/kick/mute/tban/tmute. 
 """  # The content remains the same.
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antiflood_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for A-channel
@app.on_callback_query(filters.regex("ACHANNEL_HELP"))
async def a_channel(client: Client, callback_query: CallbackQuery):
    a_channel_message =  """
*ᴀɴᴛɪ ᴄʜᴀɴɴᴇʟ*
  ᴛɪʀᴇᴅ ᴏғ ᴛᴇʟᴇɢʀᴀᴍ's sᴛᴜᴘɪᴅɪᴛʏ? ᴡᴇʟʟ ʜᴇʀᴇ ʏᴏᴜ ɢᴏ
  *ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:*
  •➥ /antichannel <on/off>: ʙᴀɴs ᴀɴᴅ ᴅᴇʟᴇᴛᴇs ᴀɴʏᴏɴᴇ ᴡʜᴏ ᴛʀɪᴇs ᴛᴏ ᴛᴀʟᴋ ᴀs ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ғᴏʀᴄᴇs ᴇᴍ ᴛᴏ ᴛᴀʟᴋ ᴀs ᴛʜᴇᴍsᴇʟᴠᴇs
  •➥ /antilinkedchan <on/off>: ᴍᴀᴋᴇs ᴇxᴏɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇ ʟɪɴᴋᴇᴅ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs ғʀᴏᴍ ᴄʜᴀᴛʀᴏᴏᴍ
  •➥ /antichannelpin <on/off>: ᴍᴀᴋᴇs ᴇxᴏɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴜɴᴘɪɴ ʟɪɴᴋᴇᴅ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs ғʀᴏᴍ ᴄʜᴀᴛʀᴏᴏᴍ
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(a_channel_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Afk
@app.on_callback_query(filters.regex("AFK_HELP"))
async def afk(client: Client, callback_query: CallbackQuery):
    afk_message =  """
    *ᴀғᴋ*
  •➥ /afk - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ.
  •➥ /afk [ʀᴇᴀsᴏɴ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀ ʀᴇᴀsᴏɴ.
  •➥ /afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ.
  •➥ /afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] [ʀᴇᴀsᴏɴ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴀғᴋ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴀsᴏɴ ʙᴏᴛʜ
 """
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(afk_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Admin
@app.on_callback_query(filters.regex("ADMIN_HELP"))
async def admin(client: Client, callback_query: CallbackQuery):
    admin_message = """
    *ᴀᴅᴍɪɴ*
  •➥ /admins*:* ʟɪꜱᴛ ᴏғ ᴀᴅᴍɪɴꜱ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
  *ᴀᴅᴍɪɴꜱ ᴏɴʟʏ:* 
  •➥ /invitelink*:* ɢᴇᴛꜱ ᴄʜᴀᴛ ɪɴᴠɪᴛᴇʟɪɴɪɴᴠɪᴛᴇʟɪɴᴋ
  •➥ /lowpromote*:* ᴘʀᴏᴍᴏᴛᴇꜱ ᴛʜᴇ ᴜꜱᴇʀ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴡɪᴛʜ ʟᴏᴡ ʀɪɢʜᴛ
  •➥ /promote*:* ᴘʀᴏᴍᴏᴛᴇꜱ ᴛʜᴇ ᴜꜱᴇʀ ʀᴇᴘʟɪᴇᴅ ᴛᴏ 
  •➥ /fullpromote*:* ᴘʀᴏᴍᴏᴛᴇꜱ ᴛʜᴇ ᴜꜱᴇʀ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴡɪᴛʜ ғᴜʟʟ ʀɪɢʜᴛꜱ
  •➥ /demote*:* ᴅᴇᴍᴏᴛᴇꜱ ᴛʜᴇ ᴜꜱᴇʀ ʀᴇᴘʟɪᴇᴅ ᴛᴏ
  •➥ /title <ᴛɪᴛʟᴇ ʜᴇʀᴇ>*:* ꜱᴇᴛꜱ ᴀ ᴄᴜꜱᴛᴏᴍ ᴛɪᴛʟᴇ ғᴏʀ ᴀɴ ᴀᴅᴍɪɴ ᴛʜᴀᴛ ᴛʜᴇ ʙᴏᴛ ᴘʀᴏᴍᴏᴛᴇᴅ
  •➥ /reload*:* ғᴏʀᴄᴇ ʀᴇғʀᴇꜱʜ ᴛʜᴇ ᴀᴅᴍɪɴꜱ ʟɪꜱᴛ 
"""

    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(admin_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Approval
@app.on_callback_query(filters.regex("APPROVE_HELP"))
async def approval(client: Client, callback_query: CallbackQuery):
    approval_message =  """
    *ᴀᴘᴘʀᴏᴠᴇ*
  •➥ *ꜱᴏᴍᴇᴛɪᴍᴇꜱ, ʏᴏᴜ ᴍɪɢʜᴛ ᴛʀᴜꜱᴛ ᴀ ᴜꜱᴇʀ ɴᴏᴛ ᴛᴏ ꜱᴇɴᴅ ᴜɴᴡᴀɴᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ. ᴍᴀʏʙᴇ ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇᴍ ᴀᴅᴍɪɴ, ʙᴜᴛ ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ᴏᴋ ᴡɪᴛʜ ʟᴏᴄᴋꜱ ʙʟᴀᴄᴋʟɪꜱᴛꜱ, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ɴᴏᴛ ᴀᴘᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇᴍ*
      ᴛʜᴀᴛ ᴡʜᴀᴛ ᴀᴘᴘʀᴏᴠᴀʟꜱ ᴀʀᴇ ғᴏʀ - ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴛʀᴜꜱᴛᴡᴏʀᴛʜʏ . ᴜꜱᴇʀꜱ ᴛᴏ ᴀʟʟᴏᴡ ᴛʜᴇᴍ ᴛᴏ ꜱᴇɴᴅ
      *ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ:*
  •➥ /approval*:* ᴄʜᴇᴄᴋ ᴀ ᴜꜱᴇʀ ᴀᴘᴘʀᴏᴠᴀʟ ꜱᴛᴀᴛᴜꜱ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ.
  •➥ /approve*:* ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜꜱᴇʀ. ʟᴏᴄᴋꜱ, ʙʟᴀᴄᴋʟɪꜱᴛꜱ, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴡᴏɴ'ᴛ ᴀᴘᴘʟʏ ᴛᴏ ᴛʜᴇᴍ ᴀɴʏᴍᴏʀᴇ.
  •➥ /unapprove*:* ᴜɴᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜꜱᴇʀ. ᴛʜᴇʏ ᴡɪʟʟ ɴᴏᴡ ʙᴇ ꜱᴜʙᴊᴇᴄᴛ to ʟᴏᴄᴋꜱ, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴀɢᴀɪɴ.
  •➥ /approved*:* ʟɪꜱᴛ ᴀʟʟ ᴀᴘᴘʀᴏᴠᴇᴅ ᴜꜱᴇʀꜱ
  •➥ /unapproveall*:* ᴜɴᴀᴘᴘʀᴏᴠᴇ *ᴀʟʟ* ᴜꜱᴇʀꜱ ɪɴ a ᴄʜᴀᴛ. ᴛʜɪꜱ ᴄᴀɴɴᴏᴛ ʙᴇ ᴜɴᴅᴏɴᴇ.
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(approval_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for B-list
@app.on_callback_query(filters.regex("BLACKLIST_HELP"))
async def b_list(client: Client, callback_query: CallbackQuery):
    b_list_message = """
    *ʙʟᴀᴄᴋʟɪsᴛ*
  •➥ʙʟᴀᴄᴋʟɪꜱᴛꜱ ᴀʀᴇ ᴜꜱᴇᴅ ᴛᴏ ꜱᴛᴏᴘ ᴄᴇʀᴛᴀɪɴ ᴛʀɪɢɢᴇʀꜱ ғʀᴏᴍ ʙᴇɪɴɢ ꜱᴀɪᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ. ᴀɴʏ ᴛɪᴍᴇ ᴛʜᴇ ᴛʀɪɢɢᴇʀ ɪꜱ ᴍᴇɴᴛɪᴏɴᴇᴅ, ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ɪᴍᴍᴇᴅɪᴀᴛᴇʟʏ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ. ᴀ ɢᴏᴏᴅ ᴄᴏᴍʙᴏ ɪs sᴏᴍᴇᴛɪᴍᴇs ᴛᴏ ᴘᴀɪʀ ᴛʜɪs ᴜᴘ ᴡɪᴛʜ ᴡᴀʀɴ ғɪʟᴛᴇʀs!
  
  ɴᴏᴛᴇ: ʙʟᴀᴄᴋʟɪsᴛs ᴅᴏ ɴᴏᴛ ᴀғғᴇᴄᴛ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs
  •➥ /ʙʟᴀᴄᴋʟɪsᴛ : ᴠɪᴇᴡ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴡᴏʀᴅs.
   ᴀᴅᴍɪɴ ᴏɴʟʏ:
  •➥ /ᴀᴅᴅʙʟᴀᴄᴋʟɪsᴛ <ᴛʀɪɢɢᴇʀs> : ᴀᴅᴅ ᴀ ᴛʀɪɢɢᴇʀ ᴛᴏ ᴛʜᴇ ʙʟᴀᴄᴋʟɪsᴛ. ᴇᴀᴄʜ ʟɪɴᴇ ɪs ᴄᴏɴsɪᴅᴇʀᴇᴅ ᴏɴᴇ ᴛʀɪɢɢᴇʀ, sᴏ ᴜsɪɴɢ ᴅɪғғᴇʀᴇɴᴛ ʟɪɴᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ʏᴏᴜ ᴛᴏ ᴀᴅᴅ ᴍᴜʟᴛɪᴘʟᴇ ᴛʀɪɢɢᴇʀs.
  •➥ /ᴜɴʙʟᴀᴄᴋʟɪsᴛ <ᴛʀɪɢɢᴇʀs> : ʀᴇᴍᴏᴠᴇ ᴛʀɪɢɢᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙʟᴀᴄᴋʟɪsᴛ. sᴀᴍᴇ ɴᴇᴡʟɪɴᴇ ʟᴏɢɪᴄ ᴀᴘᴘʟɪᴇs ʜᴇʀᴇ, sᴏ ʏᴏᴜ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴛʀɪɢɢᴇʀs ᴀᴛ ᴏɴᴄᴇ.
  •➥ /ʙʟᴀᴄᴋʟɪsᴛᴍᴏᴅᴇ <ᴏғғ/ᴅᴇʟ/ᴡᴀʀɴ/ʙᴀɴ/ᴋɪᴄᴋ/ᴍᴜᴛᴇ/ᴛʙᴀɴ/ᴛᴍᴜᴛᴇ> : ᴀᴄᴛɪᴏɴ ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ sᴇɴᴅs ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴡᴏʀᴅs.
   ʀʙʟᴀᴄᴋʟɪsᴛ sᴛɪᴄᴋᴇʀ ɪs ᴜsᴇᴅ ᴛᴏ sᴛᴏᴘ ᴄᴇʀᴛᴀɪɴ sᴛɪᴄᴋᴇʀs ᴡʜᴇɴᴇᴠᴇʀ ᴀ sᴛɪᴄᴋᴇʀ ɪs sᴇɴᴛ, ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪᴍᴍᴇᴅɪᴀᴛᴇʟʏ
 """
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(b_list_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for B-users
@app.on_callback_query(filters.regex("BUSER_HELP"))
async def b_users(client: Client, callback_query: CallbackQuery):
    b_users_message = """
  *ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs*
  •➥ /ignore: ʙʟᴀᴄᴋʟɪsᴛs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴇɴᴛɪʀᴇʟʏ.
  •➥ /lockdown <ᴏғғ/ᴏɴ>: ᴛᴏɢɢʟᴇs ʙᴏᴛ ᴀᴅᴅɪɴɢ ᴛᴏ ɢʀᴏᴜᴘs.
  •➥ /ignoredlist: Lists ɪɢɴᴏʀᴇᴅ ᴜsᴇʀs.   
  •➥ /notice: ʀᴇᴍᴏᴠᴇs ᴜsᴇʀ ғʀᴏᴍ ʙʟᴀᴄᴋʟɪsᴛ   
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(b_users_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Backup
@app.on_callback_query(filters.regex("BACKUP_HELP"))
async def backup(client: Client, callback_query: CallbackQuery):
    backup_message =  """
    *ᴀᴅᴍɪɴ ᴏɴʟʏ:*
  •➥ /import: ʀᴇᴘʟʏ ᴛᴏ ᴀ group ʙᴜᴛʟᴇʀ ʙᴀᴄᴋᴜᴘ ғɪʟᴇ ᴛᴏ ɪᴍᴘᴏʀᴛ ᴀs ᴍᴜᴄʜ ᴀs ᴘᴏssɪʙʟᴇ, ᴍᴀᴋɪɴɢ ᴛʜᴇ ᴛʀᴀɴsғᴇʀ sᴜᴘᴇʀ sɪᴍᴘʟᴇ! ɴᴏᴛᴇ \
     ᴛʜᴀᴛ ғɪʟᴇs/ᴘʜᴏᴛᴏs ᴄᴀɴ'ᴛ ʙᴇ ɪᴍᴘᴏʀᴛᴇᴅ ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
  •➥ /export: ᴇxᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴅᴀᴛᴀ, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴇxᴘᴏʀᴛᴇᴅ ᴀʀᴇ: ʀᴜʟᴇs, ɴᴏᴛᴇs (ᴅᴏᴄᴜᴍᴇɴᴛs, ɪᴍᴀɢᴇs, ᴍᴜsɪᴄ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ, ᴠᴏɪᴄᴇ, ᴛᴇxᴛ, ᴛᴇxᴛ ʙᴜᴛᴛᴏɴs)
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(backup_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Cinfo
@app.on_callback_query(filters.regex("CINFO_HELP"))
async def cinfo(client: Client, callback_query: CallbackQuery):
    cinfo_message = """
  •➥ /cinfo*:* ᴜsᴀɢᴇe:**cinfo ᴄʜᴀᴛ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ
  •➥ /uinfo*:* ɢᴇᴛ ᴜsᴇʀ ᴛɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
  •➥ /info*:* ɢᴇᴛ ᴜsᴇʀ ᴛɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
"""

    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(cinfo_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Clean
@app.on_callback_query(filters.regex("CLEANER_HELP"))
async def clean(client: Client, callback_query: CallbackQuery):
    clean_message = """
  •➥ ʙʟᴜᴇ ᴛᴇxᴛ ᴄʟᴇᴀɴᴇʀ ʀᴇᴍᴏᴠᴇᴅ ᴀɴʏ ᴍᴀᴅᴇ ᴜᴘ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛʜᴀᴛ ᴘᴇᴏᴘʟᴇ ꜱᴇɴᴅ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
  •➥ /cleanblue <on/off/yes/no>*:* ᴄʟᴇᴀɴ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀғᴛᴇʀ ꜱᴇɴᴅɪɴɢ
  •➥ /ignoreblue <word>*:* ᴘʀᴇᴠᴇɴᴛ ᴀᴜᴛᴏ ᴄʟᴇᴀɴɪɴɢ ᴏғ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ
  •➥ /unignoreblue <word>*:* ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴠᴇɴᴛ ᴀᴜᴛᴏ ᴄʟᴇᴀɴɪɴɢ ᴏғ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ
  •➥ /listblue*:* ʟɪꜱᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴡʜɪᴛᴇʟɪꜱᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅꜱ
   *ғᴏʟʟᴏᴡɪɴɢ ᴀʀᴇ ᴅɪꜱᴀꜱᴛᴇʀꜱ ᴏɴʟʏ ᴄᴏᴍᴍᴀɴᴅꜱ, ᴀᴅᴍɪɴꜱ 𝚌𝚊𝚗𝚗𝚘𝚝 ᴜꜱᴇ ᴛʜᴇꜱᴇ:*
  •➥ /gignoreblue <word>*:* ɢʟᴏʙᴀʟʟʏ ɪɢɴᴏʀᴇᴀ ʙʟᴜᴇᴛᴇxᴛ ᴄʟᴇᴀɴɪɴɢ ᴏғ ꜱᴀᴠᴇᴅ ᴡᴏʀᴅ ᴀᴄʀᴏꜱꜱ  fubuki.
  •➥ /ungignoreblue <word>*:* ʀᴇᴍᴏᴠᴇ ꜱᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғʀᴏᴍ ɢʟᴏʙᴀʟ ᴄʟᴇᴀɴɪɴɢ ʟɪꜱᴛ
 """
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(clean_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Connect
@app.on_callback_query(filters.regex("CONNECTIONS_HELP"))
async def connect(client: Client, callback_query: CallbackQuery):
    connect_message = """
  •➥ *sᴏᴍᴇᴛɪᴍᴇs, ʏᴏᴜ ᴊᴜsᴛ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ sᴏᴍᴇ ɴᴏᴛᴇs ᴀɴᴅ ғɪʟᴛᴇʀs ᴛᴏ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ, ʙᴜᴛ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴇᴠᴇʀʏᴏɴᴇ ᴛᴏ sᴇᴇ; ᴛʜɪs ɪs ᴡʜᴇʀᴇ ᴄᴏɴɴᴇᴄᴛɪᴏɴs ᴄᴏᴍᴇ ɪɴ...
    ᴛʜɪs ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴀ ᴄʜᴀᴛ's ᴅᴀᴛᴀʙᴀsᴇ, ᴀɴᴅ ᴀᴅᴅ ᴛʜɪɴɢs ᴛᴏ ɪᴛ ᴡɪᴛʜᴏᴜᴛ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀᴘᴘᴇᴀʀɪɴɢ ɪɴ ᴄʜᴀᴛ! ғᴏʀ ᴏʙᴠɪᴏᴜs ʀᴇᴀsᴏɴs, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴅᴅ ᴛʜɪɴɢs; ʙᴜᴛ ᴀɴʏ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄᴀɴ ᴠɪᴇᴡ ʏᴏᴜʀ ᴅᴀᴛᴀ.*
  •➥ /connect: ᴄᴏɴɴᴇᴄᴛꜱ ᴛᴏ ᴄʜᴀᴛ (ᴄᴀɴ ʙᴇ ᴅᴏɴᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ ʙʏ /connect ᴏʀ /connect<chatid> ɪɴ ᴘᴍ)
  •➥ /connection: ʟɪꜱᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀᴛꜱ
  •➥ /disconnect: ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ
  •➥ /helpconnect: ʟɪꜱᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛʜᴀᴛ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʀᴇᴍᴏᴛᴇʟʏ
  *ᴀᴅᴍɪɴ ᴏɴʟʏ:*
  •➥ /allowconnect <yes/no>: ᴀʟʟᴏᴡ ᴀ ᴜꜱᴇʀ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴀ ᴄʜᴀᴛ
"""

    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(connect_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Disable
@app.on_callback_query(filters.regex("DISABLE_HELP"))
async def disable(client: Client, callback_query: CallbackQuery):
    disable_message = """
  •➥ /cmds*:* ᴄʜᴇᴄᴋ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ ᴏғ ᴅɪꜱᴀʙʟᴇᴅ ᴄᴏᴍᴍᴀɴᴅꜱ
   *ᴀᴅᴍɪɴꜱ ᴏɴʟʏ:*
  •➥ /enable <ᴄᴍᴅ ɴᴀᴍᴇ>*:* ᴇɴᴀʙʟᴇ ᴛʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ
  •➥ /disable <ᴄᴍᴅ ɴᴀᴍᴇ>*:* ᴅɪꜱᴀʙʟᴇ ᴛʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ
  •➥ /enablemodule <ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ>*:* ᴇɴᴀʙʟᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ ɪɴ ᴛʜᴀᴛ ᴍᴏᴅᴜʟᴇ
  •➥ /disablemodule <ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ>*:* ᴅɪꜱᴀʙʟᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ ɪɴ ᴛʜᴀᴛ ᴍᴏᴅᴜʟᴇ
  •➥ /listcmds*:* ʟɪꜱᴛ ᴀʟʟ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏɢɢʟᴇᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(disable_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Db-clean
@app.on_callback_query(filters.regex("DBCLEAN_HELP"))
async def db_clean(client: Client, callback_query: CallbackQuery):
    db_clean_message = """
    *ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ*
  •➥ /dbcleanup: ʀᴇᴍᴏᴠᴇs ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄs ᴀɴᴅ ɢʀᴏᴜᴘs ғʀᴏᴍ ᴅʙ.
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(db_clean_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for F-sub
@app.on_callback_query(filters.regex("FSUB_HELP"))
async def f_sub(client: Client, callback_query: CallbackQuery):
    f_sub_message =  """
  *ғᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ:*
  
  •➥ *fubuki ᴄᴀɴ ᴍᴜᴛᴇ ᴍᴇᴍʙᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ɴᴏᴛ ꜱᴜʙꜱᴄʀɪʙᴇᴅ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴜɴᴛɪʟ ᴛʜᴇʏ ꜱᴜʙꜱᴄʀɪʙᴇ*
  •➥ ᴡʜᴇɴ ᴇɴᴀʙʟᴇᴅ ɪ ᴡɪʟʟ ᴍᴜᴛᴇ ᴜɴꜱᴜʙꜱᴄʀɪʙᴇᴅ ᴍᴇᴍʙᴇʀꜱ ᴀɴᴅ ꜱʜᴏᴡ ᴛʜᴇᴍ ᴀ ᴜɴᴍᴜᴛᴇ ʙᴜᴛᴛᴏɴ. ᴡʜᴇɴ ᴛʜᴇʏ ᴘʀᴇꜱꜱᴇᴅ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ɪ ᴡɪʟʟ ᴜɴᴍᴜᴛᴇ ᴛʜᴇᴍ
  
  •➥ *ꜱᴇᴛᴜᴘ*
  •➥ [ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀꜱ ᴀᴅᴍɪɴ](https://t.me/fubuki_cutibot?startgroup=new)
  •➥ [ᴀᴅᴅ ᴍᴇ ɪɴ your ᴄʜᴀɴɴᴇʟ ᴀꜱ ᴀᴅᴍɪɴ](https://t.me/fubuki_cutibot?startgroup=new)
  
   *ᴄᴏᴍᴍᴍᴀɴᴅꜱ*
  •➥ /fsub channel username - ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴀɴᴅ sᴇᴛᴜᴘ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.
  •➥ /fsub off - ᴛᴏ ᴛᴜʀɴ ᴏғ ғᴏʀᴄᴇꜱᴜʙꜱᴄʀɪʙᴇ..
  💡 ɪғ ʏᴏᴜ ᴅɪꜱᴀʙʟᴇ ғꜱᴜʙ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ꜱᴇᴛ ᴀɢᴀɪɴ ғᴏʀ ᴡᴏʀᴋɪɴɢ /fsub channel username
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(f_sub_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Filters
@app.on_callback_query(filters.regex("CUST_FILTERS_HELP"))
async def filters(client: Client, callback_query: CallbackQuery):
    filters_message = """
  •➥ /filters*:* ʟɪꜱᴛ ᴀʟʟ ᴀᴄᴛɪᴠᴇ ғɪʟᴛᴇʀꜱ ꜱᴀᴠᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ
    *ᴀᴅᴍɪɴ ᴏɴʟʏ:*
   •➥ /filter <keyword> <reply message>*:* ᴀᴅᴅ a ғɪʟᴛᴇʀ ᴛᴏ ᴛʜɪꜱ chat. ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴡ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇꜱꜱᴀɢᴇ ᴡʜᴇɴᴇᴠᴇʀ 'ᴋᴇʏᴡᴏʀᴅ ɪꜱ ᴍᴇɴᴛɪᴏɴᴇᴅ. ɪғ ʏᴏᴜ ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜱᴛɪᴄᴋᴇʀ ᴡɪᴛʜ ᴀ ᴋᴇʏᴡᴏʀᴅ, ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴀᴛ ꜱᴛɪᴄᴋᴇʀ. ɴᴏᴛᴇ: ᴀʟʟ ғɪʟᴛᴇʀ ᴋᴇʏᴡᴏʀᴅꜱ ᴀʀᴇ ɪɴ  ʟᴏᴡᴇʀᴄᴀꜱᴇ. ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴋᴇʏᴡᴏʀᴅ ᴛᴏ ʙᴇ ᴀ ꜱᴇɴᴛᴇɴᴄᴇꜱ, ᴜꜱᴇ ϙᴜᴏᴛᴇꜱ
  
    ᴇɢ : /filter "hey there" How you  doin?
    ꜱᴇᴘᴀʀᴀᴛᴇ ᴅɪғғ ʀᴇᴘʟɪᴇꜱ ʙʏ %%% ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ʀᴇᴘʟɪᴇꜱ
     *ᴇxᴀᴍᴘʟᴇ:*   /filter "filtername"
     Reply 1
     %%%
     Reply 2
     %%%
     Reply 3
   •➥ /stop <filter keyword>*:* ꜱᴛᴏᴘ ᴛʜᴀᴛ ғɪʟᴛᴇʀ
     *ᴄʜᴀᴛ creator only:*
   •➥ /removeallfilters*:* ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴄʜᴀᴛ ғɪʟᴛᴇʀꜱ ᴀᴛ ᴏɴᴄᴇ.
     *ɴᴏᴛᴇ*: ғɪʟᴛᴇʀꜱ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛ ᴍᴀʀᴋᴅᴏᴡɴ formatters like: {first}, {last} ᴇᴛᴄ.. ᴀɴᴅ ʙᴜᴛᴛᴏɴꜱ.
      ᴄʜᴇᴄᴋ /markdownhelp ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ!
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(filters_message, reply_markup=InlineKeyboardMarkup(buttons))



from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


# Callback query handler for Feds
@app.on_callback_query(filters.regex("FEDS_HELP"))
async def feds(client: Client, callback_query: CallbackQuery):
    feds_message =  """
  Eᴠᴇʀʏᴛʜɪɴɢ ɪs ғᴜɴ, ᴜɴᴛɪʟ ᴀ sᴘᴀᴍᴍᴇʀ sᴛᴀʀᴛs ᴇɴᴛᴇʀɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴀɴᴅ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ʙʟᴏᴄᴋ ɪᴛ. Tʜᴇɴ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴛᴀʀᴛ ʙᴀɴɴɪɴɢ ᴍᴏʀᴇ, ᴀɴᴅ ᴍᴏʀᴇ, ᴀɴᴅ ɪᴛ ʜᴜʀᴛs.
  Bᴜᴛ ᴛʜᴇɴ ʏᴏᴜ ʜᴀᴠᴇ ᴍᴀɴʏ ɢʀᴏᴜᴘs, ᴀɴᴅ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛʜɪs sᴘᴀᴍᴍᴇʀ ᴛᴏ ʙᴇ ɪɴ ᴏɴᴇ ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘs - ʜᴏᴡ ᴄᴀɴ ʏᴏᴜ ᴅᴇᴀʟ? Dᴏ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴍᴀɴᴜᴀʟʟʏ ʙʟᴏᴄᴋ ɪᴛ, ɪɴ ᴀʟʟ ʏᴏᴜʀ ɢʀᴏᴜᴘs?
  *Nᴏ ʟᴏɴɢᴇʀ!* Wɪᴛʜ Fᴇᴅᴇʀᴀᴛɪᴏɴ, ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ᴀ ʙᴀɴ ɪɴ ᴏɴᴇ ᴄʜᴀᴛ ᴏᴠᴇʀʟᴀᴘ ᴡɪᴛʜ ᴀʟʟ ᴏᴛʜᴇʀ ᴄʜᴀᴛs.
  Yᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴅᴇsɪɢɴᴀᴛᴇ ғᴇᴅᴇʀᴀᴛɪᴏɴ ᴀᴅᴍɪɴs, sᴏ ʏᴏᴜʀ ᴛʀᴜsᴛᴇᴅ ᴀᴅᴍɪɴ ᴄᴀɴ ʙᴀɴ ᴀʟʟ ᴛʜᴇ sᴘᴀᴍᴍᴇʀs ғʀᴏᴍ ᴄʜᴀᴛs ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ.
  
  *Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ɪɴ ᴅᴇᴘᴛʜ ᴀʙᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs.*
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(feds_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for G-cast
# Callback query handler for Info
@app.on_callback_query(filters.regex("USERINFO_HELP"))
async def info(client: Client, callback_query: CallbackQuery):
    info_message = """
  •➥ /setbio <ᴛᴇxᴛ>: ᴡʜɪʟᴇ ʀᴇᴘʟʏɪɴɢ, ᴡɪʟʟ sᴀᴠᴇ ᴀɴᴏᴛʜᴇʀ ᴜsᴇᴅ's ʙɪᴏ
  •➥ /bio: ᴡɪʟʟ ɢᴇᴛ your ᴏʀ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ's ʙɪᴏ. ᴛʜɪs ᴄᴀɴɴᴏᴛ ʙᴇ sᴇᴛ ʙʏ ʏᴏᴜʀsᴇʟғ.
  •➥ /setme <text>: ᴡɪʟʟ sᴇᴛ ʏᴏᴜʀ ɪɴғᴏ
  •➥ /me: ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ ᴏʀ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ ɪɴғᴏ
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(info_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Logs
@app.on_callback_query(filters.regex("LOG_HELP"))
async def logs(client: Client, callback_query: CallbackQuery):
    logs_message =  """
  •➥ /logchannel*:* ɢᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ɪɴғᴏ.
  •➥ /setlog*:* sᴇᴛ ᴛʜᴇ log ᴄʜᴀɴɴᴇʟ.
  •➥ /unsetlog*:* ᴜɴsᴇᴛ ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
  •➥ /logsettings
  *sᴇᴛᴛɪɴɢ ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ɪs ᴅᴏɴᴇ ʙʏ* 
  ➩ ᴀᴅᴅɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴄʜᴀɴɴᴇʟ (ᴀs ᴀɴ ᴀᴅᴍɪɴ!)
  ➩ sᴇɴᴅɪɴɢ /setlog ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ
  ➩ ғᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ /setlog ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(logs_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Locks
@app.on_callback_query(filters.regex("LOCKS_HELP"))
async def locks(client: Client, callback_query: CallbackQuery):
    locks_message =  """
  •➥ /locktypes*:* ʟɪꜱᴛꜱ ᴀʟʟ ᴘᴏꜱꜱɪʙʟᴇ ʟᴏᴄᴋᴛʏᴘᴇꜱ
  *ᴀᴅᴍɪɴꜱ ᴏɴʟʏ:*
  •➥ /lock <type>*:* ʟᴏᴄᴋ ɪᴛᴇᴍꜱ ᴏғ ᴀ ᴄᴇʀᴛᴀɪɴ ɴype (ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ)
  •➥ /unlock <type>*:* ᴜɴʟᴏᴄᴋ ɪᴛᴇᴍꜱ ᴏғ ᴀ ᴄᴇʀᴛᴀɪɴ ᴛʏᴘᴇ (ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ)
  •➥ /locks*:* ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ list ᴏғ ʟᴏᴄᴋꜱ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ.
  ʟᴏᴄᴋꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ᴛᴏ ʀᴇꜱᴛʀɪᴄᴛ ᴀ ɢʀᴏᴜᴘ ᴜꜱᴇʀꜱ.
  Locking ᴜʀʟs ᴡɪʟʟ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ ᴜʀʟs, ʟᴏᴄᴋɪɴɢ sᴛɪᴄᴋᴇʀs ᴡɪʟʟ ʀᴇsᴛʀɪᴄᴛ     ᴀʟʟ
  ɴᴏɴ-ᴀᴅᴍɪɴ users ғʀᴏᴍ sᴇɴᴅɪɴɢ sᴛɪᴄᴋᴇʀs, ᴇᴛᴄ.
  ʟᴏᴄᴋɪɴɢ ʙᴏᴛs ᴡɪʟʟ sᴛᴏᴘ ɴᴏɴ-ᴀᴅᴍɪɴs  ғʀᴏᴍ ᴀᴅᴅɪɴɢ ʙᴏᴛs ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ.
  *ɴᴏᴛᴇ:*
  •➥ ᴜɴʟᴏᴄᴋɪɴɢ ᴘᴇʀᴍɪssɪᴏɴ *ɪɴғᴏ* ᴡɪʟʟ ᴀʟʟᴏᴡ ᴍᴇᴍʙᴇʀs (ɴᴏɴ-ᴀᴅᴍɪɴs) ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ.ɪɴғᴏʀᴍᴀᴛɪᴏɴ, sᴜᴄʜ ᴀs ᴛʜᴇ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ᴏʀ ᴛʜᴇ ɢʀᴏᴜᴘ ɴᴀᴍᴇ
  •➥ ᴜɴʟᴏᴄᴋɪɴɢ ᴘᴇʀᴍɪssɪᴏɴ *ᴘɪɴ* ᴡɪʟʟ ᴀʟʟᴏᴡ ᴍᴇᴍʙᴇʀs (ɴᴏɴ-ᴀᴅᴍɪɴs) ᴛᴏ ᴘɪɴɴᴇᴅ ᴀ ᴍᴇssᴀɢᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(locks_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Muting
@app.on_callback_query(filters.regex("MUTING_HELP"))
async def muting(client: Client, callback_query: CallbackQuery):
    muting_message = """
  •➥*ᴀᴅᴍɪɴꜱ ᴏɴʟʏ:*
  •➥ /mute <userhandle>*:* ꜱɪʟᴇɴᴄᴇꜱ ᴀ ᴜꜱᴇʀ. ᴄᴀɴ ᴀʟꜱᴏ ʙᴇ ᴜꜱᴇᴅ as a ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜꜱᴇʀ.
  •➥ /dmute <userhandle>*:*  ᴅᴇʟᴇᴛᴇ ᴍᴀssᴀɢᴇ + ᴍᴜᴛᴇ ᴀ ᴜsᴇʀ
  •➥ /smute <userhandle>*:* ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇ + ᴅᴇʟᴇᴛᴇ ᴄᴏᴍᴍᴀɴᴅ + ᴍᴜᴛᴇ ᴀ ᴜsᴇʀ 
  •➥ /tmute <userhandle> x(m/h/)*:* ᴍᴜᴛᴇꜱ ᴀ ᴜꜱᴇʀ ғᴏʀ x ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). m   = ᴍɪɴᴜᴛᴇꜱ, h = ʜᴏᴜʀꜱ, d = ᴅᴀʏꜱ.
  •➥ /unmute <userhandle>*:* ᴜɴᴍᴜᴛᴇꜱ ᴀ ᴜꜱᴇʀ. ᴄᴀɴ ᴀʟꜱᴏ ʙᴇ ᴜꜱᴇᴅ ᴀꜱ ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜꜱᴇʀ.
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(muting_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for N-mode
@app.on_callback_query(filters.regex("NMODE_HELP"))
async def n_mode(client: Client, callback_query: CallbackQuery):
    n_mode_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(n_mode_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Notes
@app.on_callback_query(filters.regex("NOTES_HELP"))
async def notes(client: Client, callback_query: CallbackQuery):
    notes_message = """
Note Management Commands

User Commands:

/get <notename>: Retrieve a note.
#<notename>: Shortcut for /get.
/notes or /saved: List all saved notes.
/number: Get the note by its list number.
/get <notename> noformat: Fetch note without formatting (useful for updates).

Admin Commands:

/save <notename> <notedata>: Save a note with a name. Add buttons using [text](buttonurl:link).
/save <notename>: Save the replied message as a note.
Separate random replies with %%% (e.g., Reply 1 %%% Reply 2).

/clear <notename>: Delete a specific note.
/removeallnotes: Clear all notes in the group.
Notes:
Note names are case-sensitive and saved in lowercase.
"""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(n_mode_message, reply_markup=InlineKeyboardMarkup(buttons))


# Callback query handler for Owner help
@app.on_callback_query(filters.regex("OWNER_HELP"))
async def owner_help(client: Client, callback_query: CallbackQuery):
    owner_message = """Owner command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(owner_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Pins help
@app.on_callback_query(filters.regex("PINS_HELP"))
async def pins_help(client: Client, callback_query: CallbackQuery):
    pins_message = """
  •➥ /pin*:* sɪʟᴇɴᴛʟʏ ᴘɪɴs ᴛʜᴇ ᴍᴇssᴀɢᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ - ᴀᴅᴅ 'loud' ᴏʀ 'notify' ᴛᴏ ɢɪᴠᴇ ɴᴏᴛɪғs ᴛᴏ ᴜsᴇʀs.
  •➥ /unpin*:* ᴜɴᴘɪɴs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ.
  •➥ /pinned*:* ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ.
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(pins_message, reply_markup=InlineKeyboardMarkup(buttons))


# Callback query handler for Purge help
@app.on_callback_query(filters.regex("PURGE_HELP"))
async def purge_help(client: Client, callback_query: CallbackQuery):
    purge_message = """  
  •➥ /purge *:* ʀᴇᴘʟʏ ᴡɪᴛʜ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴡʜᴇʀᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs sʜᴏᴜʟᴅ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ
  •➥ /del *:* ᴅᴇʟᴇᴛᴇ ᴀ ʀᴇᴘʟʏᴇᴅ ᴍᴇssᴀɢᴇ 
  """
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(purge_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Quotly help
@app.on_callback_query(filters.regex("QUOTLY_HELP"))
async def quotly_help(client: Client, callback_query: CallbackQuery):
    quotly_message =  """
  •➥ /q → ᴄʀᴇᴀᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ 
  •➥ /q r → ᴄʀᴇᴀᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʀᴇᴘʟʏ
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(quotly_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Sticker help
@app.on_callback_query(filters.regex("STICKER_HELP"))
async def sticker_help(client: Client, callback_query: CallbackQuery):
    sticker_message = """
  •➥ /stickerid *:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ᴍᴇ ᴛᴏ ᴛᴇʟʟ ʏᴏᴜ ɪᴛꜱ ғɪʟᴇ ɪᴅ.
  •➥ /getsticker *:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ᴍᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛꜱ ʀᴀᴡ ᴘɴɢ ғɪʟᴇ.
  •➥ /kang *:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ᴀᴅᴅ ɪᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ. [ ɪᴍɢ, ɢɪғ, ᴘʜᴏᴛᴏ]
  •➥ /delsticker *:* ʀᴇᴘʟʏ ᴛᴏ ʏᴏᴜʀ ᴀɴɪᴍᴇ ᴇxɪꜱᴛ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ ᴛᴏ ᴅᴇʟᴇᴛᴇ ɪᴛ.
  •➥ /stickers *:* ғɪɴᴅ ꜱᴛɪᴄᴋᴇʀꜱ ғᴏʀ ɢɪᴠᴇɴ ᴛᴇʀᴍ ᴏɴ ᴄᴏᴍʙᴏᴛ ꜱᴛɪᴄᴋᴇʀ ᴄᴀᴛᴀʟᴏɢᴜᴇ
  •➥ /mmf <ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛᴇxᴛ> *:* ᴛᴏ ᴅʀᴀᴡ a ᴛᴇxᴛ ғᴏʀ ꜱᴛɪᴄᴋᴇʀ 

"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(sticker_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Translator help
@app.on_callback_query(filters.regex("GTRANSLATE_HELP"))
async def translator_help(client: Client, callback_query: CallbackQuery):
    translator_message = """
  •➥ *ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ sᴛᴜғғ!*
  •➥ /tl (or /tr): ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ᴛʀᴀɴsʟᴀᴛᴇs ɪᴛ ᴛᴏ ᴇɴɢʟɪsʜ.
  •➥ /tl <lang>: ᴛʀᴀɴsʟᴀᴛᴇs ᴛᴏ <lang>
   *ᴇɢ:* /tl ja: ᴛʀᴀɴsʟᴀᴛᴇs ᴛᴏ ᴊᴀᴘᴀɴᴇsᴇ.
  •➥ /tl <source>//<dest>: ᴛʀᴀɴsʟᴀᴛᴇs ғʀᴏᴍ <source> ᴛᴏ <lang>.
   ᴇɢ:  /tl ja//en: ᴛʀᴀɴsʟᴀᴛᴇs ғʀᴏᴍ ᴊᴀᴘᴀɴᴇsᴇ ᴛᴏ ᴇɴɢʟɪsʜ.
  •➥ /langs: ɢᴇᴛ ᴀ ʟɪsᴛ of sᴜᴘᴘᴏʀᴛᴇᴅ ʟᴀɴɢᴜᴀɢᴇs ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪᴏɴ.
   *ɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ to ᴠᴏɪᴄᴇ and ᴠᴏɪᴄᴇ ᴛᴏ ᴛᴇxᴛ..*
  •➥ /tts <lang code>*:* ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ᴏᴜᴛᴘᴜᴛ
  •➥ /stt*:* ᴛʏᴘᴇ ɪɴ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠᴏɪᴄᴇ ᴍᴇssᴀɢᴇ(sᴜᴘᴘᴏʀᴛ ᴇɴɢʟɪsʜ ᴏɴʟʏ) ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴛᴇxᴛ ғʀᴏᴍ ɪᴛ.

"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(translator_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Truth-Dare help
@app.on_callback_query(filters.regex("TD_HELP"))
async def truth_dare_help(client: Client, callback_query: CallbackQuery):
    truth_dare_message = """
  •➥ /truth *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
  •➥ /dare *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(truth_dare_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Tag-All help
@app.on_callback_query(filters.regex("TAGS_HELP"))
async def tag_all_help(client: Client, callback_query: CallbackQuery):
    tag_all_message =  """
  •➥ /tagall ᴏʀ @all (ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ᴍᴇssᴀɢᴇ) ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴡɪᴛʜᴏᴜᴛ ᴇxᴄᴇᴘᴛɪᴏɴ
  •➥ /cancel : ғᴏʀ ᴄᴀɴᴄᴇʟɪɴɢ ᴛʜᴇ ᴍᴇɴᴛɪᴏɴ-ᴀʟʟ.
  •➥ /tagalert : ᴏɴ/ᴏғғ
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(tag_all_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Uall help
@app.on_callback_query(filters.regex("USERINFO_HELP"))
async def uall_help(client: Client, callback_query: CallbackQuery):
    uall_message = """Uall command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(uall_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Warns help
@app.on_callback_query(filters.regex("WARNS_HELP"))
async def warns_help(client: Client, callback_query: CallbackQuery):
    warns_message = """
  •➥ /warns <ᴜsᴇʀʜᴀɴᴅʟᴇ>: ɢᴇᴛ ᴀ ᴜsᴇʀ's ɴᴜᴍʙᴇʀ, ᴀɴᴅ ʀᴇᴀsᴏɴ, ᴏғ ᴡᴀʀɴs.
  •➥ /warnliat : ʟɪsᴛ ᴏғ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴡᴀʀɴɪɴɢ ғɪʟᴛᴇʀs
  •➥ /warn <ᴜsᴇʀʜᴀɴᴅʟᴇ>: ᴡᴀʀɴ ᴀ ᴜsᴇʀ. ᴀғᴛᴇʀ 3 ᴡᴀʀɴs, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ
  •➥ /dwarn <ᴜsᴇʀʜᴀɴᴅʟᴇ>: ᴡᴀʀɴ ᴀ ᴜsᴇʀ ᴀɴᴅ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ. ᴀғᴛᴇʀ 3 ᴡᴀʀɴs, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ.
  •➥ /resetwarn <ᴜsᴇʀʜᴀɴᴅʟᴇ>: ʀᴇsᴇᴛ ᴛʜᴇ ᴡᴀʀɴs ғᴏʀ ᴀ ᴜsᴇʀ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ.
  •➥ /addwarn <ᴋᴇʏᴡᴏʀᴅ> <ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ>: sᴇᴛ ᴀ ᴡᴀʀɴɪɴɢ ғɪʟᴛᴇʀ ᴏɴ ᴀ ᴄᴇʀᴛᴀɪɴ ᴋᴇʏᴡᴏʀᴅ. ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴋᴇʏᴡᴏʀᴅ ᴛᴏ ʙᴇ ᴀ sᴇɴᴛᴇɴᴄᴇ, ᴇɴᴄᴏᴍᴘᴀss ɪᴛ ᴡɪᴛʜ ϙᴜᴏᴛᴇs, ᴀs sᴜᴄʜ: /ᴀᴅᴅᴡᴀʀɴ "ᴠᴇʀʏ ᴀɴɢʀʏ" ᴛʜɪs ɪs ᴀɴ ᴀɴɢʀʏ ᴜsᴇʀ.
  •➥ /nowarn <ᴋᴇʏᴡᴏʀᴅ>: sᴛᴏᴘ ᴀ ᴡᴀʀɴɪɴɢ ғɪʟᴛᴇʀ
  •➥ /warnlimit <ɴᴜᴍ>: sᴇᴛ ᴛʜᴇ ᴡᴀʀɴɪɴɢ ʟɪᴍɪᴛ
  •➥ /strongwarn  <ᴏɴ/ʏᴇs/ᴏғғ/ɴᴏ>: ɪғ sᴇᴛ ᴛᴏ ᴏɴ, ᴇxᴄᴇᴇᴅɪɴɢ ᴛʜᴇ ᴡᴀʀɴ ʟɪᴍɪᴛ ᴡɪʟʟ ʀᴇsᴜʟᴛ ɪɴ ᴀ ʙᴀɴ. ᴇʟsᴇ, ᴡɪʟʟ ᴊᴜsᴛ ᴘᴜɴᴄʜ.
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(warns_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Welcome help
@app.on_callback_query(filters.regex("WELCOME_HELP"))
async def welcome_help(client: Client, callback_query: CallbackQuery):
    welcome_message = """
  Customize Your Group's Welcome/Goodbye Messages!
You can personalize messages using these variables:

{first}: User's first name
{last}: User's last name (or first name if none)
{fullname}: User's full name
{username}: Username (or a mention if none)
{mention}: Mentions the user by first name
{id}: User's ID
{count}: Member number
{chatname}: Chat name
Markdown & Buttons:

Add bold, italics, links, and buttons. Example button for rules:
[Rules](buttonurl://t.me/fubuki_cutibot?start=group_id)
Replace group_id with your group’s ID (use /id to find it, including the - sign).

You can also set media (images, GIFs, videos, voice) as welcome messages by replying to the media and using /setwelcome.
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(welcome_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Zombies help
@app.on_callback_query(filters.regex("ZOMBIES_HELP"))
async def zombies_help(client: Client, callback_query: CallbackQuery):
    zombies_message = """
  •➥ /zombies : ғɪɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
  •➥ /zombies clean : ᴄʟᴇᴀɴ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ
"""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(zombies_message, reply_markup=InlineKeyboardMarkup(buttons))
# Example usage: management_panel_buttons(1)

# Callback query handler for management panel
@app.on_callback_query(filters.regex(r"management_page_\d+"))
async def handle_management_panel(client: Client, callback_query: CallbackQuery):
    page_num = int(callback_query.data.split("_")[-1])
    await callback_query.message.edit_text(
        f"Management Panel - Page {page_num}",
        reply_markup=management_panel_buttons(page_num)
    )
    


# Callback query handler for close/back button



# Start button or panel setup (Assuming it's triggered somewhere in your bot code)
@app.on_callback_query(filters.regex("management_action"))
async def management_action(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Management Panel - Page 1",
        reply_markup=management_panel_buttons(1)
                                                                                         )
