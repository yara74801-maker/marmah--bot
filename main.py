from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from database import database


# ------------------------
# شروع ربات
# ------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = f"""
🌸 سلام {update.effective_user.first_name}

به ربات Marmah Bot خوش اومدی.

از دکمه‌ها یا دستور /help استفاده کن.

موفق باشی ❤️
"""

    await update.message.reply_text(text)


# ------------------------
# راهنما
# ------------------------

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📚 راهنمای ربات

👤 کاربران
/start
/help
موجودی
رتبه

👮 مدیران
اضافه کویین
کم کردن کویین
تنظیم خوشامد
تنظیم قوانین

👑 مالک
تنظیمات
آمار
"""

    await update.message.reply_text(text)


# ------------------------
# اجرای ربات
# ------------------------

async def on_start():

    await database.setup()


def main():

    app = Application.builder().token(BOT_TOKEN).post_init(on_start).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Marmah Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
