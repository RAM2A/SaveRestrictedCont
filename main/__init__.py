#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "24665357" #config("API_ID", default=None, cast=int)
API_HASH = "beb7e4b83ada668fa85f9a9b56338f1d" #config("API_HASH", default=None)
BOT_TOKEN = "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI" #config("BOT_TOKEN", default=None)
SESSION = "1BVtsOJ4Buzj-vIEfWXZ6GAdPuF4VvAWXd-t6FXOgOBKXAHKUak__gaSv3TYGotZ--GOILmpaCbdebjZlkfFR3Y64fkcnF6CcKfaCzGrQNzUaFhk6zlAI5qbeuSzD_5_pgy3XUxQ2oE9auLsbKs_na3OQYQzrnOd5nYvFRpuHdaWEc00-kCcO59ZTizmCSHt4-5Su3NC9z1j90acRKltNOiimRSaZtKXyO7YivjROypj9L8LiUK0UBGMWblfhXe1e4okfSoKqbJO4g49B6Bpcvdsq9PZUZOkjYkp7qE2beCXsubpWf_LlN9I8pG9vBKViOSha_KFNOW7MESwHae0NLZdvcoDqCB8=" #config("SESSION", default=None)
FORCESUB = "-1002137417670" #config("FORCESUB", default=None)
AUTH = "1717511106" #config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
