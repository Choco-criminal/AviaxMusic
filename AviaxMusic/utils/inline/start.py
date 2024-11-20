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
from strings import get_string, helpers


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


@app.on_callback_query(filters.regex("ANTIFLOOD_HELP"))
async def antiflood_help(client: Client, callback_query: CallbackQuery):
    antiflood_message = """•➥ *ᴀᴅᴍɪɴs ᴏɴʟʏ:*
  •➥ /antispam <on/off/yes/no>: ᴡɪʟʟ ᴛᴏɢɢʟᴇ ᴏᴜʀ ᴀɴᴛɪsᴘᴀᴍ ᴛᴇᴄʜ ᴏʀ ʀᴇᴛᴜʀɴ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs.
  ᴀɴᴛɪ-sᴘᴀᴍ, ᴜsᴇᴅ ʙʏ ʙᴏᴛ ᴅᴇᴠs ᴛᴏ ʙᴀɴ sᴘᴀᴍᴍᴇʀs ᴀᴄʀᴏss ᴀʟʟ ɢʀᴏᴜᴘs. ᴛʜɪs ʜᴇʟᴘs ᴘʀᴏᴛᴇᴄᴛ 
  ʏᴏᴜ ᴀɴᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘs ʙʏ ʀᴇᴍᴏᴠɪɴɢ sᴘᴀᴍ ғʟᴏᴏᴅᴇʀs ᴀs ǫᴜɪᴄᴋʟʏ ᴀs ᴘᴏssɪʙʟᴇ
  ɴᴏᴛᴇ: ᴜsᴇʀs ᴄᴀɴ ᴀᴘᴘᴇᴀʟ ɢʙᴀɴs ᴏʀ ʀᴇᴘᴏʀᴛ sᴘᴀᴍᴍᴇʀs ᴀᴛ 
  •➥ /flood: ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴀɴᴛɪғʟᴏᴏᴅ sᴇᴛᴛɪɴɢs
  •➥ /setflood <number/off/no>: sᴇᴛ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ᴀғᴛᴇʀ ᴡʜɪᴄʜ ᴛᴏ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏɴ ᴀ ᴜsᴇʀ. sᴇᴛ ᴛᴏ '0', 'off', or 'no' ᴛᴏ ᴅɪsᴀʙʟᴇ.
  •➥ /setfloodmode <ᴀᴄᴛɪᴏɴ ᴛʏᴘᴇ>: ᴄʜᴏᴏsᴇ ᴡʜɪᴄʜ ᴀᴄᴛɪᴏɴ ᴛᴏ ᴛᴀᴋᴇ ᴏɴ ᴀ ᴜsᴇʀ ᴡʜᴏ ʜᴀs ʙᴇᴇɴ ғʟᴏᴏᴅɪɴɢ. ᴏᴘᴛɪᴏɴs: ban/kick/mute/tban/tmute."""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antiflood_message, reply_markup=InlineKeyboardMarkup(buttons))

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
