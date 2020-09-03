#!/usr/bin/env python

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import logging
import json, requests
from datetime import datetime
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# telegram.ext.JobQueue.run_repeating(telegram.ext.JobQueue(), bot, 10) # Prevents sleeping?

CONT, SPLIT, TODAY, DATE, RESP, LOOP = range(6)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="👋 Hello, I'm Tony bot! 😀")
    context.bot.send_message(chat_id=update.effective_chat.id, text="🛕 Welcome to the Daily Stoic! 🛕\n\n It's yet another beautiful day! 🌈☀")
    context.bot.send_message(chat_id=update.effective_chat.id, text="💪 Our work together is about to begin 💪")
    kb = [[telegram.KeyboardButton('/Yes')],
          [telegram.KeyboardButton('/No')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("🤓 Shall I kindly begin by sharing a short passage for today❓📄.", reply_markup=kb_markup)
    return CONT

def date_split(update, context):
    kb = [[telegram.KeyboardButton('/Today')],
          [telegram.KeyboardButton('/AnotherDate')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("👍 Great enthusiasm! Do you want to read *today's* or *another date's* passage❓❓❓", reply_markup=kb_markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return SPLIT

def get_passage(date):
    url = "https://my-stoic-bot.herokuapp.com/passages?date={}".format(date) # query from json-server hosted in heroku
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)[0]["message"]
    return js
    
def today_date(update, context):
    user = update.message.from_user
    TODAY = datetime.today().strftime("%b%d")
    context.bot.send_message(chat_id=update.effective_chat.id, text="🤓 Thanks! \n\nBtw, these passages are adapted from:\n\n 📚 *The Daily Stoic* by Ryan Holiday\n\n to help you live a good and meaningful life. 👴👴👴", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Flipping to {} 🧙‍♂️🧙‍♂️🧙‍♂️. Do allow approximately 2-5s... 🙏".format(TODAY))
    js = get_passage(TODAY)
    context.bot.send_message(chat_id=update.effective_chat.id, text=js)
    kb = [[telegram.KeyboardButton('/Definitely')],
          [telegram.KeyboardButton('/No')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("🤓 Do slowly read the previous passage. When you are done, let me know if you want another passage of wisdom? 📄.", reply_markup=kb_markup)
    return RESP

def custom_date(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🤓 Thanks! \n\nBtw, these passages are adapted from:\n\n 📚 *The Daily Stoic* by Ryan Holiday\n\n to help you live a good and meaningful life. 👴👴👴", parse_mode=telegram.ParseMode.MARKDOWN)
    context.bot.send_message(chat_id=update.effective_chat.id, text="➡ Start by typing *MMMdd* e.g. (Jan03, Sep27) to read. 🐱‍🏍.", parse_mode=telegram.ParseMode.MARKDOWN)
    user = update.message.from_user
    logger.info("User %s entered %s", user.first_name, update.message.text)
    return DATE

def custom_date2(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text="Very well, {}. Flipping to {} 🧙‍♂️🧙‍♂️🧙‍♂️. Do allow approximately 2-5s... 🙏".format(user.first_name, update.message.text))
    logger.info("User %s reading date %s", user.first_name, update.message.text)
    js = get_passage(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=js)
    kb = [[telegram.KeyboardButton('/Definitely')],
          [telegram.KeyboardButton('/No')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("🤓 As you are reading, do you wish for another passage? 📄.", reply_markup=kb_markup)
    return RESP

def loop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🔥🔥🔥 That's amazing. Remember it is never about how much you read, but how much you are actively reflecting or practising.")
    # context.bot.send_message(chat_id=update.effective_chat.id, text="➡ Continue by typing *MMMdd* e.g. (Jan03, Sep27) to read. 🐱‍🏍.", parse_mode=telegram.ParseMode.MARKDOWN)
    user = update.message.from_user
    logger.info("User %s entered %s", user.first_name, update.message.text)
    kb = [[telegram.KeyboardButton('/Today')],
          [telegram.KeyboardButton('/AnotherDate')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("👍 Now, would you want to read *today's* or *other date's* passage❓❓❓", reply_markup=kb_markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return SPLIT

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oops, didn't really understand you there 🤨")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oops, didn't really understand your command 🤨")

def help_command(update, context):
    update.message.reply_text("/start - to start the bot")

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! Hope we can talk again soon. You know where to (/start) 😁',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def main():
    TOKEN = '1322982150:AAGYLypxEx132JKT3EXyfpzZtTzzswiM0e4'
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={
            CONT: [CommandHandler('Yes', date_split), CommandHandler('No', cancel)],
            SPLIT: [CommandHandler('Today', today_date), CommandHandler('AnotherDate', custom_date)],
            DATE: [MessageHandler(Filters.regex('^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[0-3][0-9]$'), custom_date2)],
            RESP: [CommandHandler('Definitely', loop), CommandHandler('No', cancel)]
            # PHOTO: [MessageHandler(Filters.photo, photo),
                    # CommandHandler('skip', skip_photo)],
            # LOCATION: [MessageHandler(Filters.location, location),
                       # CommandHandler('skip', skip_location)],
            # BIO: [MessageHandler(Filters.text & ~Filters.command, bio)]
        },
        fallbacks=[CommandHandler('No', cancel)])
    dispatcher.add_handler(conv_handler)

    updater.start_polling() # Start locally hosting Bot
    updater.idle()  # Run the bot until you press Ctrl-C or the process receives SIGINT,

    PORT = int(os.environ.get('PORT', 5000))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://my-stoic-telebot.herokuapp.com/' + TOKEN)
    

if __name__ == '__main__':
    main()