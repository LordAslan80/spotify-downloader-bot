from pathlib import Path
from spotify_downloader_bot.settings import BASE_DIR, ENV_FILE
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from .utils import api, get_song, remove_song, save_user_data


async def spotify_downloader(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        song_path = Path(f"{BASE_DIR}/downloads")
        song_path.mkdir(parents=True, exist_ok=True)

        requested_song = api(update.message.text)

        if not requested_song["error"]:
            song = get_song(song_path, requested_song["url"])

            await save_user_data(
                update.effective_user.full_name,
                update.effective_user.username,
                update.message.text,
            )

            await update.message.reply_audio(song)

            remove_song(song)
    except Exception as e:
        print(f"Error: {e}")

        await update.message.reply_text(
            text="Somthing went wrong.\nPlease make sure the url is correct."
        )


async def warning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text="Please send a valid Spotify track link.")


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.startswith("https://open.spotify.com/track"):
        await spotify_downloader(update, context)
    else:
        await warning(update, context)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


def start_bot():
    print("Starting Telegram bot...")
    app = Application.builder().token(ENV_FILE["BOT_TOKEN"]).build()

    # messages
    app.add_handler(MessageHandler(filters.Regex(""), handle_messages))

    # Errors
    app.add_error_handler(error)

    # start the bot
    print("Polling...")
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    start_bot()
