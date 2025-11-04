from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# === Replace below with your data ===
BOT_TOKEN = "8242428419:AAGwULBvgPvK70PhxjH3AHU5Kx1qix3y1to"   # <--- Replace safely, don’t share publicly

SBI_QR_URL = "https://your-sbi-qr-image-link.com/sbi_qr.jpg"
KOTAK_QR_URL = "https://your-kotak-qr-image-link.com/kotak_qr.jpg"

SBI_UPI_ID = "pritvaghasiya14@oksbi"
KOTAK_UPI_ID = "8320099766@kotak811"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏦 State Bank of India", callback_data="sbi")],
        [InlineKeyboardButton("🏦 Kotak 811", callback_data="kotak")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Select your payment bank 👇", reply_markup=reply_markup)


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "sbi":
        caption = f"💙 *State Bank of India Payment Details*\n\nUPI ID: `{SBI_UPI_ID}`"
        await query.message.reply_photo(photo=SBI_QR_URL, caption=caption, parse_mode="Markdown")

    elif query.data == "kotak":
        caption = f"❤️ *Kotak 811 Payment Details*\n\nUPI ID: `{KOTAK_UPI_ID}`"
        await query.message.reply_photo(photo=KOTAK_QR_URL, caption=caption, parse_mode="Markdown")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()
          
