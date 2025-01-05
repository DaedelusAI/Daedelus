from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from daedelus import Daedelus

# Initialize Daedelus
daedelus = Daedelus()

def handle_command(update: Update, context: CallbackContext):
    command = update.message.text.split()[0].lstrip("/")
    args = update.message.text.split()[1:]
    response = daedelus.handle_command(command, args)
    update.message.reply_text(response)

def main():
    TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["launch", "guide", "status"], handle_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
