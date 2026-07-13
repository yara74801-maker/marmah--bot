import os

# =========================
# Bot Settings
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
BOT_NAME = "Marmah Bot"

# شناسه عددی مالک اصلی
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# =========================
# Database
# =========================

DATABASE_NAME = "marmah.db"

# =========================
# Security
# =========================

MAX_WARNS = 3
MAX_SPAM = 5
SPAM_TIME = 10

# =========================
# Force Join
# =========================

FORCE_JOIN = False
FORCE_JOIN_CHANNEL = ""

# =========================
# Coins
# =========================

START_COINS = 100
DAILY_REWARD = 20

# =========================
# Welcome
# =========================

WELCOME_ENABLED = True

# =========================
# Logs
# =========================

LOGS_ENABLED = True
