from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Callback query handler for Antispam help

@app.on_callback_query(filters.regex("ANTISPAM_HELP"))
async def antispam_help(client: Client, callback_query: CallbackQuery):
    antispam_message = """  •➥ *ᴀᴅᴍɪɴs ᴏɴʟʏ:*
  •➥ /antispam <on/off/yes/no>: ᴡɪʟʟ ᴛᴏɢɢʟᴇ ᴏᴜʀ ᴀɴᴛɪsᴘᴀᴍ ᴛᴇᴄʜ ᴏʀ ʀᴇᴛᴜʀɴ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs.
  ᴀɴᴛɪ-sᴘᴀᴍ, ᴜsᴇᴅ ʙʏ ʙᴏᴛ ᴅᴇᴠs ᴛᴏ ʙᴀɴ sᴘᴀᴍᴍᴇʀs ᴀᴄʀᴏss ᴀʟʟ ɢʀᴏᴜᴘs. ᴛʜɪs ʜᴇʟᴘs ᴘʀᴏᴛᴇᴄᴛ 
  ʏᴏᴜ ᴀɴᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘs ʙʏ ʀᴇᴍᴏᴠɪɴɢ sᴘᴀᴍ ғʟᴏᴏᴅᴇʀs ᴀs ǫᴜɪᴄᴋʟʏ ᴀs ᴘᴏssɪʙʟᴇ
  ɴᴏᴛᴇ: ᴜsᴇʀs ᴄᴀɴ ᴀᴘᴘᴇᴀʟ ɢʙᴀɴs ᴏʀ ʀᴇᴘᴏʀᴛ sᴘᴀᴍᴍᴇʀs ᴀᴛ @AbishnoiMF
  •➥ /flood: ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴀɴᴛɪғʟᴏᴏᴅ sᴇᴛᴛɪɴɢs
  •➥ /setflood <number/off/no>: sᴇᴛ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ᴀғᴛᴇʀ ᴡʜɪᴄʜ ᴛᴏ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏɴ ᴀ ᴜsᴇʀ. sᴇᴛ ᴛᴏ '0', 'off', or 'no' ᴛᴏ ᴅɪsᴀʙʟᴇ.
  •➥ /setfloodmode <ᴀᴄᴛɪᴏɴ ᴛʏᴘᴇ>: ᴄʜᴏᴏsᴇ ᴡʜɪᴄʜ ᴀᴄᴛɪᴏɴ ᴛᴏ ᴛᴀᴋᴇ ᴏɴ ᴀ ᴜsᴇʀ ᴡʜᴏ ʜᴀs ʙᴇᴇɴ ғʟᴏᴏᴅɪɴɢ. ᴏᴘᴛɪᴏɴs: ban/kick/mute/tban/tmute. """
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antispam_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for A-Raid
@app.on_callback_query(filters.regex("a_raid"))
async def a_raid(client: Client, callback_query: CallbackQuery):
    a_raid_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(a_raid_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Antiflood help
@app.on_callback_query(filters.regex("ANTIFLOOD_HELP"))
async def antiflood_help(client: Client, callback_query: CallbackQuery):
    antiflood_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antiflood_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for A-Channel
@app.on_callback_query(filters.regex("a_channel"))
async def a_channel(client: Client, callback_query: CallbackQuery):
    a_channel_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(a_channel_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Afk
@app.on_callback_query(filters.regex("afk"))
async def afk(client: Client, callback_query: CallbackQuery):
    afk_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(afk_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Admin
@app.on_callback_query(filters.regex("admin"))
async def admin(client: Client, callback_query: CallbackQuery):
    admin_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(admin_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Approval
@app.on_callback_query(filters.regex("approval"))
async def approval(client: Client, callback_query: CallbackQuery):
    approval_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(approval_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for B-list
@app.on_callback_query(filters.regex("b_list"))
async def b_list(client: Client, callback_query: CallbackQuery):
    b_list_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(b_list_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for B-users
@app.on_callback_query(filters.regex("b_users"))
async def b_users(client: Client, callback_query: CallbackQuery):
    b_users_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(b_users_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Backup
@app.on_callback_query(filters.regex("backup"))
async def backup(client: Client, callback_query: CallbackQuery):
    backup_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(backup_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Cinfo
@app.on_callback_query(filters.regex("cinfo"))
async def cinfo(client: Client, callback_query: CallbackQuery):
    cinfo_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(cinfo_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Clean
@app.on_callback_query(filters.regex("clean"))
async def clean(client: Client, callback_query: CallbackQuery):
    clean_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(clean_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Connect
@app.on_callback_query(filters.regex("connect"))
async def connect(client: Client, callback_query: CallbackQuery):
    connect_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(connect_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Disable
@app.on_callback_query(filters.regex("disable"))
async def disable(client: Client, callback_query: CallbackQuery):
    disable_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(disable_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Db-clean
@app.on_callback_query(filters.regex("db_clean"))
async def db_clean(client: Client, callback_query: CallbackQuery):
    db_clean_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(db_clean_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for F-sub
@app.on_callback_query(filters.regex("f_sub"))
async def f_sub(client: Client, callback_query: CallbackQuery):
    f_sub_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(f_sub_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Filters
@app.on_callback_query(filters.regex("filters"))
async def filters(client: Client, callback_query: CallbackQuery):
    filters_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(filters_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Feds
@app.on_callback_query(filters.regex("feds"))
async def feds(client: Client, callback_query: CallbackQuery):
    feds_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(feds_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for G-cast
@app.on_callback_query(filters.regex("g_cast"))
async def g_cast(client: Client, callback_query: CallbackQuery):
    g_cast_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(g_cast_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Info
@app.on_callback_query(filters.regex("info"))
async def info(client: Client, callback_query: CallbackQuery):
    info_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(info_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Logs
@app.on_callback_query(filters.regex("logs"))
async def logs(client: Client, callback_query: CallbackQuery):
    logs_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(logs_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Locks
@app.on_callback_query(filters.regex("locks"))
async def locks(client: Client, callback_query: CallbackQuery):
    locks_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(locks_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Muting
@app.on_callback_query(filters.regex("muting"))
async def muting(client: Client, callback_query: CallbackQuery):
    muting_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(muting_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for N-mode
@app.on_callback_query(filters.regex("n_mode"))
async def n_mode(client: Client, callback_query: CallbackQuery):
    n_mode_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(n_mode_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Notes
@app.on_callback_query(filters.regex("notes"))
async def notes(client: Client, callback_query: CallbackQuery):
    notes_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(notes_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback
# Callback query handler for Owner help
@app.on_callback_query(filters.regex("owner"))
async def owner_help(client: Client, callback_query: CallbackQuery):
    owner_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(owner_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Pins help
@app.on_callback_query(filters.regex("pins"))
async def pins_help(client: Client, callback_query: CallbackQuery):
    pins_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(pins_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Ping help
@app.on_callback_query(filters.regex("ping"))
async def ping_help(client: Client, callback_query: CallbackQuery):
    ping_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(ping_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Purge help
@app.on_callback_query(filters.regex("purge"))
async def purge_help(client: Client, callback_query: CallbackQuery):
    purge_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(purge_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Quotly help
@app.on_callback_query(filters.regex("quotly"))
async def quotly_help(client: Client, callback_query: CallbackQuery):
    quotly_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(quotly_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Sticker help
@app.on_callback_query(filters.regex("sticker"))
async def sticker_help(client: Client, callback_query: CallbackQuery):
    sticker_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(sticker_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Translator help
@app.on_callback_query(filters.regex("translator"))
async def translator_help(client: Client, callback_query: CallbackQuery):
    translator_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(translator_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Truth-Dare help
@app.on_callback_query(filters.regex("truth_dare"))
async def truth_dare_help(client: Client, callback_query: CallbackQuery):
    truth_dare_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(truth_dare_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Tag-All help
@app.on_callback_query(filters.regex("tag_all"))
async def tag_all_help(client: Client, callback_query: CallbackQuery):
    tag_all_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(tag_all_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Uall help
@app.on_callback_query(filters.regex("uall"))
async def uall_help(client: Client, callback_query: CallbackQuery):
    uall_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(uall_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Warns help
@app.on_callback_query(filters.regex("warns"))
async def warns_help(client: Client, callback_query: CallbackQuery):
    warns_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(warns_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Welcome help
@app.on_callback_query(filters.regex("welcome"))
async def welcome_help(client: Client, callback_query: CallbackQuery):
    welcome_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(welcome_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Zombies help
@app.on_callback_query(filters.regex("zombies"))
async def zombies_help(client: Client, callback_query: CallbackQuery):
    zombies_message = ""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(zombies_message, reply_markup=InlineKeyboardMarkup(buttons))
  
