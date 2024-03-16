from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://i.pinimg.com/originals/a9/0e/54/a90e54ebea40010708f8d8a9c27eaae1.jpg")
START_IMG = getenv("START_IMG", "https://i.pinimg.com/originals/a9/0e/54/a90e54ebea40010708f8d8a9c27eaae1.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/b1o_d_a")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/b1o_d_a")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6264668799").split()))


FAILED = "https://i.pinimg.com/originals/a9/0e/54/a90e54ebea40010708f8d8a9c27eaae1.jpg"
