import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID" , "25475489"))
API_HASH = getenv("API_HASH" , "3fc2b371f4fbb0166758736414d8be92")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN" , "7617090520:AAH6OqlzkAGlJUhtd6O3yd9sRfDo6lxwn00")
#-------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","UnknownX_9_11")
#--------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Fubuki_xbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "˹𝙁ᴜʙᴜᴋɪ ✘ 𝐌ᴜsɪᴄ˼🫧")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Not_ur_assistent")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Choco-criminal/AviaxMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private



SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Choco_for_u")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ANIME_CHAT_ANG")


# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------



# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION1", "BQE4qWEAh0hMwsEORDJsTe-XW7wC7HMP8JKwKuOebOVxz6kQBMFfOgZPuQHD1RPX9yBtw5RWiw24Vp8qdO-FzXJvhP0DrwGLErxPlmmwxOzVLj5bJZ6XGD_QNOk-H0NyJZ8-pUb8TB85yC6HcKfXEztkVkghCo-Ol-_FiD-hVXsU2cN5g7GQs3_GdpnKC-MN6XZhdiEcgMxWYEXw4fbfG4Xzasvp6tE45rdkjWBfIBzPVzBL4tQqUtQzr9_uWIPrmIDjc4EmSy_xDefBi8jIhYkm84SokliLRpR8nbFxzXeUX2GCrrKoDWeT0aPhC0F3smP7Wy7Vxfn8nF1OwfbYnfrtcUhCPAAAAAHZxlQ5AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


#------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/pC0.mp4"
)
PING_IMG_URL = "https://envs.sh/AAt.mp4"
PLAYLIST_IMG_URL = "https://envs.sh/p4F.jpg"
STATS_IMG_URL = "https://envs.sh/pYG.mp4"
TELEGRAM_AUDIO_URL = "https://envs.sh/pC3.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/pC3.jpg"
STREAM_IMG_URL = "https://envs.sh/p4e.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/p4w.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4e4c15823f0056c0756c8-1230cfcb94e69c070c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/vTelegraphBot-10-21-13https://graph.org/vTelegraphBot-10-21-13"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/vTelegraphBot-10-21-13https://graph.org/vTelegraphBot-10-21-13"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c7ea15528fc9816e05141-0a5598ac2585dae36f.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# --------

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ---------------------------------


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
