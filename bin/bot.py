from bottoken import token_val
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

def start(update, context):
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
        logging.info("Send the start message for %d",update.effective_chat.id)
    except:
        logging.warning("Couldn't print the start message for %d",update.effective_chat.id)

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level= logging.INFO, filename= "../logs/bot.log")
    logging.info("Bot server started")
    print(token_val)
    try:
        updater = Updater(token= token_val, use_context= True)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start',start)
        get_screenshot_handler = CommandHandler('get_screenshot',get_screenshot)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(get_screenshot_handler)
        logging.info("Successfully initialized handlers")
        updater.start_polling()
    except:
        logging.warning("Error intializing handler and setting up polling")

if __name__ == "__main__":
    main()