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
        InlineKeyboardButton("A-spam", callback_data="ANTISPAM_HELP"), InlineKeyboardButton("A-raid", callback_data="a_raid"),
        InlineKeyboardButton("A-flood", callback_data="ANTIFLOOD_HELP"), InlineKeyboardButton("A-channel", callback_data="a_channel"),
        InlineKeyboardButton("Afk", callback_data="afk"), InlineKeyboardButton("Admin", callback_data="admin"),
        InlineKeyboardButton("Approval", callback_data="approval"), InlineKeyboardButton("B-list", callback_data="b_list"),
        InlineKeyboardButton("B-users", callback_data="b_users"), InlineKeyboardButton("Backup", callback_data="backup"),
        InlineKeyboardButton("Cinfo", callback_data="cinfo"), InlineKeyboardButton("Clean", callback_data="clean"),
        InlineKeyboardButton("Connect", callback_data="connect"), InlineKeyboardButton("Disable", callback_data="disable"),
        InlineKeyboardButton("Db-clean", callback_data="db_clean"), InlineKeyboardButton("F-sub", callback_data="f_sub"),
        InlineKeyboardButton("Filters", callback_data="filters"), InlineKeyboardButton("Feds", callback_data="feds"),
        InlineKeyboardButton("G-cast", callback_data="g_cast"), InlineKeyboardButton("Info", callback_data="info"),
        InlineKeyboardButton("Logs", callback_data="logs"), InlineKeyboardButton("Locks", callback_data="locks"),
        InlineKeyboardButton("Muting", callback_data="muting"), InlineKeyboardButton("N-mode", callback_data="n_mode"),
        InlineKeyboardButton("Notes", callback_data="notes"), InlineKeyboardButton("Owner", callback_data="owner"),
        InlineKeyboardButton("Pins", callback_data="pins"), InlineKeyboardButton("Ping", callback_data="ping"),
        InlineKeyboardButton("Purge", callback_data="purge"), InlineKeyboardButton("Quotly", callback_data="quotly"),
        InlineKeyboardButton("Sticker", callback_data="sticker"), InlineKeyboardButton("Translator", callback_data="translator"),
        InlineKeyboardButton("Truth-Dare", callback_data="TD_HELP"), InlineKeyboardButton("Tag-All", callback_data="tag_all"),
        InlineKeyboardButton("Uall", callback_data="uall"), InlineKeyboardButton("Warns", callback_data="warns"),
        InlineKeyboardButton("Welcome", callback_data="welcome"), InlineKeyboardButton("Zombies", callback_data="zombies")
    ]
    
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
