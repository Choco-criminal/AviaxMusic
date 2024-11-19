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

# Management panel buttons generator
def management_panel_buttons(page_num):
    panels = {
        1: [
            [InlineKeyboardButton("F-sub", callback_data="f_sub"), InlineKeyboardButton("Filters", callback_data="filters")],
            [InlineKeyboardButton("Feds", callback_data="feds"), InlineKeyboardButton("G-cast", callback_data="g_cast")],
            [InlineKeyboardButton("Info", callback_data="info"), InlineKeyboardButton("Logs", callback_data="logs")],
            [InlineKeyboardButton("Locks", callback_data="locks"), InlineKeyboardButton("Muting", callback_data="muting")],
            [InlineKeyboardButton("N-mode", callback_data="n_mode"), InlineKeyboardButton("Notes", callback_data="notes")],
            [InlineKeyboardButton("Owner", callback_data="owner"), InlineKeyboardButton("Pins", callback_data="pins")],
            [InlineKeyboardButton("Ping", callback_data="ping"), InlineKeyboardButton("Purge", callback_data="purge")],
            [InlineKeyboardButton("Quotly", callback_data="quotly"), InlineKeyboardButton("Next ➡️", callback_data="management_page_2")],
            [InlineKeyboardButton("Close ❌", callback_data="settingsback_helper")]
        ],
        2: [
            [InlineKeyboardButton("Sticker", callback_data="sticker"), InlineKeyboardButton("Translator", callback_data="translator")],
            [InlineKeyboardButton("Truth-Dare", callback_data="truth_dare"), InlineKeyboardButton("Tag-All", callback_data="tag_all")],
            [InlineKeyboardButton("Uall", callback_data="uall"), InlineKeyboardButton("Warns", callback_data="warns")],
            [InlineKeyboardButton("Welcome", callback_data="welcome"), InlineKeyboardButton("Zombies", callback_data="zombies")],
            [InlineKeyboardButton("⬅️ Previous", callback_data="management_page_1"), InlineKeyboardButton("Next ➡️", callback_data="management_page_3")],
            [InlineKeyboardButton("Close ❌", callback_data="settingsback_helper")]
        ],
        3: [
            [InlineKeyboardButton("A-spam", callback_data="a_spam"), InlineKeyboardButton("A-raid", callback_data="a_raid")],
            [InlineKeyboardButton("A-flood", callback_data="a_flood"), InlineKeyboardButton("A-channel", callback_data="a_channel")],
            [InlineKeyboardButton("Afk", callback_data="afk"), InlineKeyboardButton("Admin", callback_data="admin")],
            [InlineKeyboardButton("Approval", callback_data="approval"), InlineKeyboardButton("B-list", callback_data="b_list")],
            [InlineKeyboardButton("B-users", callback_data="b_users"), InlineKeyboardButton("Backup", callback_data="backup")],
            [InlineKeyboardButton("Cinfo", callback_data="cinfo"), InlineKeyboardButton("Clean", callback_data="clean")],
            [InlineKeyboardButton("Connect", callback_data="connect"), InlineKeyboardButton("Disable", callback_data="disable")],
            [InlineKeyboardButton("Db-clean", callback_data="db_clean"), InlineKeyboardButton("⬅️ Previous", callback_data="management_page_2")],
            [InlineKeyboardButton("Close ❌", callback_data="settingsback_helper")]
        ]
    }
    return InlineKeyboardMarkup(panels[page_num])


# Callback query handler for management panel
@app.on_callback_query(filters.regex(r"management_page_\d+"))
async def handle_management_panel(client: Client, callback_query: CallbackQuery):
    page_num = int(callback_query.data.split("_")[-1])
    await callback_query.message.edit_text(
        f"Management Panel - Page {page_num}",
        reply_markup=management_panel_buttons(page_num)
    )


# Callback query handler for management actions
@app.on_callback_query(filters.regex(r"^f_sub|filters|feds|g_cast|info|logs|locks|muting|n_mode|notes|owner|pins|ping|purge|quotly|sticker|translator|truth_dare|tag_all|uall|warns|welcome|zombies|a_spam|a_raid|a_flood|a_channel|afk|admin|approval|b_list|b_users|backup|cinfo|clean|connect|disable|db_clean$"))
async def handle_action(client: Client, callback_query: CallbackQuery):
    action = callback_query.data
    await callback_query.message.edit_text(
        f"**{action.replace('_', ' ').capitalize()}** action selected!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Back", callback_data=f"management_page_1")]
        ])
    )


# Callback query handler for close/back button
@app.on_callback_query(filters.regex("settingsback_helper"))
async def handle_close(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Back to settings.",
        reply_markup=start_panel(_)
    )
