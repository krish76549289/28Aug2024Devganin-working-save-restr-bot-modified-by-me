# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21567814"))
API_HASH = getenv("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = getenv("BOT_TOKEN", "7864597080:AAGkfDbzl7bJKjov-mlp2he20MrYdADmLMc")
OWNER_ID = int(getenv("OWNER_ID", "6126688051"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://krishna56478910:KWPaEQfwoHbzan5g@strangerboykrishna.tux94dy.mongodb.net/")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002528316008"))
FORCESUB = getenv("FORCESUB", "-1002528316008")

