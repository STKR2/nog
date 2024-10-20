
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","8934899"))
API_HASH = getenv("API_HASH","bf3e98d2c351e4ad06946b4897374a1e")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ultroidofficial_chat")
