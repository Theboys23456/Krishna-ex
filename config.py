"""
from os import getenv


API_ID = int(getenv("API_ID", "16253557"))
API_HASH = getenv("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
BOT_TOKEN = getenv("BOT_TOKEN", "7923836196:AAFMTv7Uckt6RFvla8PrzHSK9s02q-8DfRg")
OWNER_ID = int(getenv("OWNER_ID", "1996039956"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1996039956").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002281623908"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002363250260"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "21567814"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7565686231:AAGQX2WmNI3grhC4vGKYp1II2eWE5ZLsprI")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("testingxtbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6126688051"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002583554860"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://krishna93107437:ecFL2x5KeUnOhHJJ@strangerboy27.h5bsz1t.mongodb.net/")
# -----------------------------------------------
FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002334419872"))

