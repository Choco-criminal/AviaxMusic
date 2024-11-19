
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters
from AviaxMusic.utils import *
import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴍᴜsɪᴄ", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="Management", callback_data="management_action"),  
            [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),# New "Management" button
            ]
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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="Management", callback_data="management_action"),  # Management button
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def management_panel_page_1(_):
    buttons = [
        [
            InlineKeyboardButton(text="F-sub", callback_data="f_sub"),
            InlineKeyboardButton(text="Filters", callback_data="filters"),
            InlineKeyboardButton(text="Feds", callback_data="feds"),
        ],
        [
            InlineKeyboardButton(text="G-cast", callback_data="g_cast"),
            InlineKeyboardButton(text="Info", callback_data="info"),
            InlineKeyboardButton(text="Logs", callback_data="logs"),
        ],
        [
            InlineKeyboardButton(text="Locks", callback_data="locks"),
            InlineKeyboardButton(text="Muting", callback_data="muting"),
            InlineKeyboardButton(text="N-mode", callback_data="n_mode"),
        ],
        [
            InlineKeyboardButton(text="Notes", callback_data="notes"),
            InlineKeyboardButton(text="Owner", callback_data="owner"),
            InlineKeyboardButton(text="Pins", callback_data="pins"),
        ],
        [
            InlineKeyboardButton(text="Ping", callback_data="ping"),
            InlineKeyboardButton(text="Purge", callback_data="purge"),
            InlineKeyboardButton(text="Quotly", callback_data="quotly"),
        ],
        [
            InlineKeyboardButton(text="Next ➡️", callback_data="management_page_2"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Go Back", callback_data="go_home"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def management_panel_page_2(_):
    buttons = [
        [
            InlineKeyboardButton(text="Sticker", callback_data="sticker"),
            InlineKeyboardButton(text="Translator", callback_data="translator"),
            InlineKeyboardButton(text="Truth-Dare", callback_data="truth_dare"),
        ],
        [
            InlineKeyboardButton(text="Tag-All", callback_data="tag_all"),
            InlineKeyboardButton(text="Uall", callback_data="uall"),
            InlineKeyboardButton(text="Warns", callback_data="warns"),
        ],
        [
            InlineKeyboardButton(text="Welcome", callback_data="welcome"),
            InlineKeyboardButton(text="Zombies", callback_data="zombies"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Previous", callback_data="management_page_1"),
            InlineKeyboardButton(text="Next ➡️", callback_data="management_page_3"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Go Back", callback_data="go_home"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def management_panel_page_3(_):
    buttons = [
        [
            InlineKeyboardButton(text="A-spam", callback_data="a_spam"),
            InlineKeyboardButton(text="A-raid", callback_data="a_raid"),
            InlineKeyboardButton(text="A-flood", callback_data="a_flood"),
        ],
        [
            InlineKeyboardButton(text="A-channel", callback_data="a_channel"),
            InlineKeyboardButton(text="Afk", callback_data="afk"),
            InlineKeyboardButton(text="Admin", callback_data="admin"),
        ],
        [
            InlineKeyboardButton(text="Approval", callback_data="approval"),
            InlineKeyboardButton(text="B-list", callback_data="b_list"),
            InlineKeyboardButton(text="B-users", callback_data="b_users"),
        ],
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app
import config

# Start panel buttons
def start_panel():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ᴍᴜsɪᴄ", callback_data="settings_back_helper"),
            InlineKeyboardButton("Support Group", url=config.SUPPORT_GROUP),
            InlineKeyboardButton("Management", callback_data="management_action")
        ]
    ])

# Management panel buttons for a given page
def management_panel_page(page_num):
    panels = {
        1: [
            ["F-sub", "f_sub", "Filters", "filters", "Feds", "feds"],
            ["G-cast", "g_cast", "Info", "info", "Logs", "logs"],
            ["Locks", "locks", "Muting", "muting", "N-mode", "n_mode"],
            ["Notes", "notes", "Owner", "owner", "Pins", "pins"],
            ["Ping", "ping", "Purge", "purge", "Quotly", "quotly"],
            ["Next ➡️", "management_page_2", "⬅️ Go Back", "go_home"]
        ],
        2: [
            ["Sticker", "sticker", "Translator", "translator", "Truth-Dare", "truth_dare"],
            ["Tag-All", "tag_all", "Uall", "uall", "Warns", "warns"],
            ["Welcome", "welcome", "Zombies", "zombies"],
            ["⬅️ Previous", "management_page_1", "Next ➡️", "management_page_3"],
            ["⬅️ Go Back", "go_home"]
        ],
        3: [
            ["A-spam", "a_spam", "A-raid", "a_raid", "A-flood", "a_flood"],
            ["A-channel", "a_channel", "Afk", "afk", "Admin", "admin"],
            ["Approval", "approval", "B-list", "b_list", "B-users", "b_users"],
            ["Backup", "backup", "Cinfo", "cinfo", "Clean", "clean"],
            ["Connect", "connect", "Disable", "disable", "Db-clean", "db_clean"],
            ["⬅️ Previous", "management_page_2", "⬅️ Go Back", "go_home"]
        ]
    }
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, callback_data=cb_data) for text, cb_data in zip(row[::2], row[1::2])] for row in panels[page_num]])

# Callback query handler
@app.on_callback_query()
def handle_callback_query(client, query):
    data = query.data
    if data == "management_action":
        query.message.edit_text("Management Panel - Page 1", reply_markup=management_panel_page(1))
    elif data.startswith("management_page_"):
        page_num = int(data.split('_')[-1])
        query.message.edit_text(f"Management Panel - Page {page_num}", reply_markup=management_panel_page(page_num))
    elif data == "go_home":
        query.message.edit_text("Start Page", reply_markup=start_panel())
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
