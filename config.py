from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21213404"))
API_HASH = getenv("API_HASH", "13ef1eb22194b5f3eee956e5c61f6b41")

BOT_TOKEN = getenv("BOT_TOKEN", "6919731273:AAGM1NL5mjKYd2RbrsHKVIB_mDD-vPlV29k")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6413079101"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Sensei_Chat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ANI_BOTS_UPDATES")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5066042764").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
