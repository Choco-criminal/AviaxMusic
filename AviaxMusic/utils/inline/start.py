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
def management_panel_page(page_num):
    panels = {
        1: [
            ["F-sub", "f_sub", "Filters", "filters", "Feds", "feds"],
            ["G-cast", "g_cast", "Info", "info", "Logs", "logs"],
            ["Locks", "locks", "Muting", "muting", "N-mode", "n_mode"],
            ["Notes", "notes", "Owner", "owner", "Pins", "pins"],
            ["Ping", "ping", "Purge", "purge", "Quotly", "quotly"],
            ["Next ➡️", "management_page_2", "⬅️ Go Back", "settings_back_helper"]
        ],
        2: [
            ["Sticker", "sticker", "Translator", "translator", "Truth-Dare", "truth_dare"],
            ["Tag-All", "tag_all", "Uall", "uall", "Warns", "warns"],
            ["Welcome", "welcome", "Zombies", "zombies"],
            ["⬅️ Previous", "management_page_1", "Next ➡️", "management_page_3"],
            ["⬅️ Go Back", "settings_back_helper"]
        ],
        3: [
            ["A-spam", "a_spam", "A-raid", "a_raid", "A-flood", "a_flood"],
            ["A-channel", "a_channel", "Afk", "afk", "Admin", "admin"],
            ["Approval", "approval", "B-list", "b_list", "B-users", "b_users"],
            ["Backup", "backup", "Cinfo", "cinfo", "Clean", "clean"],
            ["Connect", "connect", "Disable", "disable", "Db-clean", "db_clean"],
            ["⬅️ Previous", "management_page_2", "⬅️ Go Back", "settings_back_helper"]
        ]
    }
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, callback_data=cb_data) for text, cb_data in zip(row[::2], row[1::2])] for row in panels[page_num]])




@# Callback query handler
@app.on_callback_query()
def handle_callback_query(client, query):
    data = query.data
    if data == "management_action":
        query.message.edit_text("Management Panel - Page 1", reply_markup=management_panel_page(1))
    elif data.startswith("management_page_"):
        page_num = int(data.split('_')[-1])
        query.message.edit_text(f"Management Panel - Page {page_num}", reply_markup=management_panel_page(page_num))
    elif data == "settings_back_helper":
        # Handle the "Go Back" button to return to the start panel
        query.message.edit_text("Start Page", reply_markup=start_panel(_))
    else:
        # Directly return back button
        for page_num, actions in {
            1: ["f_sub", "filters", "feds", "g_cast", "info", "logs", "locks", "muting", "n_mode", "notes", "owner", "pins", "ping", "purge", "quotly"],
            2: ["sticker", "translator", "truth_dare", "tag_all", "uall", "warns", "welcome", "zombies"],
            3: ["a_spam", "a_raid", "a_flood", "a_channel", "afk", "admin", "approval", "b_list", "b_users", "backup", "cinfo", "clean", "connect", "disable", "db_clean"]
        }.items():
            if data in actions:
                query.message.edit_text(f"{data.replace('_', '-')} action selected!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data=f"management_page_{page_num}")]]))
                break
