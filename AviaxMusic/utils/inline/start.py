
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
        [
            InlineKeyboardButton(text="Backup", callback_data="backup"),
            InlineKeyboardButton(text="Cinfo", callback_data="cinfo"),
            InlineKeyboardButton(text="Clean", callback_data="clean"),
        ],
        [
            InlineKeyboardButton(text="Connect", callback_data="connect"),
            InlineKeyboardButton(text="Disable", callback_data="disable"),
            InlineKeyboardButton(text="Db-clean", callback_data="db_clean"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Previous", callback_data="management_page_2"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Go Back", callback_data="go_home"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def get_back_button(callback_data):
    """
    Helper function to return to the correct management page after viewing an action.
    """
    if callback_data in ["f_sub", "filters", "feds", "g_cast", "info", "logs", "locks", "muting", "n_mode", "notes", "owner", "pins", "ping", "purge", "quotly"]:
        return InlineKeyboardButton(text="⬅️ Back", callback_data="management_page_1")
    elif callback_data in ["sticker", "translator", "truth_dare", "tag_all", "uall", "warns", "welcome", "zombies"]:
        return InlineKeyboardButton(text="⬅️ Back", callback_data="management_page_2")
    elif callback_data in ["a_spam", "a_raid", "a_flood", "a_channel", "afk", "admin", "approval", "b_list", "b_users", "backup", "cinfo", "clean", "connect", "disable", "db_clean"]:
        return InlineKeyboardButton(text="⬅️ Back", callback_data="management_page_3")


# Logic to handle callback queries in your bot
@app.on_callback_query()
def handle_callback_query(client, query):
    data = query.data

    if data == "management_action":
        query.message.edit_text("Management Panel - Page 1", reply_markup=management_panel_page_1(_))
    
    elif data == "management_page_1":
        query.message.edit_text("Management Panel - Page 1", reply_markup=management_panel_page_1(_))
    
    elif data == "management_page_2":
        query.message.edit_text("Management Panel - Page 2", reply_markup=management_panel_page_2(_))
    
    elif data == "management_page_3":
        query.message.edit_text("Management Panel - Page 3", reply_markup=management_panel_page_3(_))
    
    elif data == "go_home":
        query.message.edit_text("Start Page", reply_markup=start_panel(_))

    # Handle specific button actions and add the back button to the respective page.
    elif data in ["f_sub", "filters", "feds", "g_cast", "info", "logs", "locks", "muting", "n_mode", "notes", "owner", "pins", "ping", "purge", "quotly", "sticker", "translator", "truth_dare", "tag_all", "uall", "warns", "welcome", "zombies", "a_spam", "a_raid", "a_flood", "a_channel", "afk", "admin", "approval", "b_list", "b_users", "backup", "cinfo", "clean", "connect", "disable", "db_clean"]:
        back_button = get_back_button(data)
        query.message.edit_text(f"{data.replace('_', '-')} action selected!", reply_markup=InlineKeyboardMarkup([[back_button]]))

    # Handle more actions if needed
