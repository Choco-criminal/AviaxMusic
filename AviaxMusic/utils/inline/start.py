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
