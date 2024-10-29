from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters

API_TOKEN = ''

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello ! I am your new chat bot")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text))