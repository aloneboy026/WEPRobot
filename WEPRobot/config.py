# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = ""  
    API_HASH = ""
    TOKEN = ""
    OWNER_ID = "6027144943"
    OWNER_USERNAME = "@ll_Mahadev_ll"
    MONGO_DB_URI = ""
    MONGO_DB = ""
    SUPPORT_CHAT = "@Girls_Talking_Group"
    JOIN_LOGGER = "-1001881047393"
    EVENT_LOGS = "-1001881047393"
    ERROR_LOG = "-1001881047393"

    # RECOMMENDED
    INFOPIC = "https://graph.org/file/32a94e912f02da0db4a3d.jpg"   
    CF_API_KEY = ""
    LASTFM_API_KEY = ""
    BOT_USERNAME = "@WEP_Robot"
    WALL_API = ""
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = ""
    REM_BG_API_KEY = ""
    TIME_API_KEY = ""
    CASH_API_KEY = ""
    REM_BG_API_KEY = ""
    ARQ_API_KEY = ""
    ARQ_API = ""
    ARQ_API_URL = ""
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    BOT_ID = ""
    STRING_SESSION = ""
    SESSION_STRING = ""
    SQLALCHEMY_DATABASE_URI = ""
    DATABASE_URL = ""
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@lI_Mahadev_Il"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = ""
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = ""
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = ""
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = ""
    WOLVES = ""
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
