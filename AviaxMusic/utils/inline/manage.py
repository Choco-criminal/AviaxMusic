# Callback query handler for Antispam help
@app.on_callback_query(filters.regex("ANTISPAM_HELP"))
async def antispam_help(client: Client, callback_query: CallbackQuery):
    antispam_message = """   """
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antispam_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for A-raid
@app.on_callback_query(filters.regex("RAID_HELP"))
async def a_raid(client: Client, callback_query: CallbackQuery):
    a_raid_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(a_raid_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Antiflood help
@app.on_callback_query(filters.regex("ANTIFLOOD_HELP"))
async def antiflood_help(client: Client, callback_query: CallbackQuery):
    antiflood_message = """..."""  # The content remains the same.
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(antiflood_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for A-channel
@app.on_callback_query(filters.regex("ACHANNEL_HELP"))
async def a_channel(client: Client, callback_query: CallbackQuery):
    a_channel_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(a_channel_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Afk
@app.on_callback_query(filters.regex("AFK_HELP"))
async def afk(client: Client, callback_query: CallbackQuery):
    afk_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(afk_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Admin
@app.on_callback_query(filters.regex("ADMIN_HELP"))
async def admin(client: Client, callback_query: CallbackQuery):
    admin_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(admin_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Approval
@app.on_callback_query(filters.regex("APPROVE_HELP"))
async def approval(client: Client, callback_query: CallbackQuery):
    approval_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(approval_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for B-list
@app.on_callback_query(filters.regex("BLACKLIST_HELP"))
async def b_list(client: Client, callback_query: CallbackQuery):
    b_list_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(b_list_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for B-users
@app.on_callback_query(filters.regex("BUSER_HELP"))
async def b_users(client: Client, callback_query: CallbackQuery):
    b_users_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(b_users_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Backup
@app.on_callback_query(filters.regex("BACKUP_HELP"))
async def backup(client: Client, callback_query: CallbackQuery):
    backup_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(backup_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Cinfo
@app.on_callback_query(filters.regex("CINFO_HELP"))
async def cinfo(client: Client, callback_query: CallbackQuery):
    cinfo_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(cinfo_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Clean
@app.on_callback_query(filters.regex("CLEANER_HELP"))
async def clean(client: Client, callback_query: CallbackQuery):
    clean_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(clean_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Connect
@app.on_callback_query(filters.regex("CONNECTIONS_HELP"))
async def connect(client: Client, callback_query: CallbackQuery):
    connect_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(connect_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Disable
@app.on_callback_query(filters.regex("DISABLE_HELP"))
async def disable(client: Client, callback_query: CallbackQuery):
    disable_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(disable_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Db-clean
@app.on_callback_query(filters.regex("DBCLEAN_HELP"))
async def db_clean(client: Client, callback_query: CallbackQuery):
    db_clean_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_1")]]
    await callback_query.message.edit_text(db_clean_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for F-sub
@app.on_callback_query(filters.regex("FSUB_HELP"))
async def f_sub(client: Client, callback_query: CallbackQuery):
    f_sub_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(f_sub_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Filters
@app.on_callback_query(filters.regex("CUST_FILTERS_HELP"))
async def filters(client: Client, callback_query: CallbackQuery):
    filters_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(filters_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Feds
@app.on_callback_query(filters.regex("FEDS_HELP"))
async def feds(client: Client, callback_query: CallbackQuery):
    feds_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(feds_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for G-cast
@app.on_callback_query(filters.regex("GCAST_HELP"))
async def g_cast(client: Client, callback_query: CallbackQuery):
    g_cast_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(g_cast_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Info
@app.on_callback_query(filters.regex("USERINFO_HELP"))
async def info(client: Client, callback_query: CallbackQuery):
    info_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(info_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Logs
@app.on_callback_query(filters.regex("LOG_HELP"))
async def logs(client: Client, callback_query: CallbackQuery):
    logs_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(logs_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Locks
@app.on_callback_query(filters.regex("LOCKS_HELP"))
async def locks(client: Client, callback_query: CallbackQuery):
    locks_message = ""
    buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]]
    await callback_query.message.edit_text(locks_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Muting
@app.on_callback_query(filters.regex("MUTING_HELP"))
async def muting(client: Client, callback_query: CallbackQuery):
    muting_message = ""
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
    notes

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
    pins_message = """Pins command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(pins_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Ping help
@app.on_callback_query(filters.regex("PING_HELP"))
async def ping_help(client: Client, callback_query: CallbackQuery):
    ping_message = """Ping command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(ping_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Purge help
@app.on_callback_query(filters.regex("PURGE_HELP"))
async def purge_help(client: Client, callback_query: CallbackQuery):
    purge_message = """Purge command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(purge_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Quotly help
@app.on_callback_query(filters.regex("QUOTLY_HELP"))
async def quotly_help(client: Client, callback_query: CallbackQuery):
    quotly_message = """Quotly command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_2")]
    ]
    await callback_query.message.edit_text(quotly_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Sticker help
@app.on_callback_query(filters.regex("STICKER_HELP"))
async def sticker_help(client: Client, callback_query: CallbackQuery):
    sticker_message = """Sticker command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(sticker_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Translator help
@app.on_callback_query(filters.regex("GTRANSLATE_HELP"))
async def translator_help(client: Client, callback_query: CallbackQuery):
    translator_message = """Translator command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(translator_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Truth-Dare help
@app.on_callback_query(filters.regex("TD_HELP"))
async def truth_dare_help(client: Client, callback_query: CallbackQuery):
    truth_dare_message = """Truth-Dare command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(truth_dare_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Tag-All help
@app.on_callback_query(filters.regex("TAGS_HELP"))
async def tag_all_help(client: Client, callback_query: CallbackQuery):
    tag_all_message = """Tag-All command help text here."""
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
    warns_message = """Warns command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(warns_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Welcome help
@app.on_callback_query(filters.regex("WELCOME_HELP"))
async def welcome_help(client: Client, callback_query: CallbackQuery):
    welcome_message = """Welcome command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(welcome_message, reply_markup=InlineKeyboardMarkup(buttons))

# Callback query handler for Zombies help
@app.on_callback_query(filters.regex("ZOMBIES_HELP"))
async def zombies_help(client: Client, callback_query: CallbackQuery):
    zombies_message = """Zombies command help text here."""
    buttons = [
        [InlineKeyboardButton("⬅️ Back", callback_data="management_page_3")]
    ]
    await callback_query.message.edit_text(zombies_message, reply_markup=InlineKeyboardMarkup(buttons))
