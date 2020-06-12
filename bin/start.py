import logging
import subprocess
from properties import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import ImageGrab
from telegram.ext import BaseFilter
from datetime import datetime

class CommandFilter(BaseFilter):
    def filter( self, message):
        if message.text.split()[0] in permitted_commands:
            return True
        else:
            logging.info("%s is not allowed to be executed in the server",message.text.split()[0])

def start(update, context):
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
        logging.info("Send the start message for %d",update.effective_chat.id)
    except Exception as e:
        logging.warning("An error occured in start_handler for user-%d",update.effective_chat.id)
        logging.error(str(e))

def exec_command(update, context):
    command = update.message.text.split()
    try:
        output = subprocess.check_output(command, cwd= currdir).decode('utf-8')
        logging.info("%s: %s", command, output)
        if output:
            context.bot.send_message(chat_id=update.effective_chat.id, text=output)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))


def main():
    logging_location = log_location + log_name
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level= logging.INFO, filename= logging_location)
    logging.info("Bot server started")
    print(token_val)
    try:
        command_filter = CommandFilter()
        updater = Updater(token= token_val, use_context= True)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start',start)
        command_message_handler = MessageHandler(command_filter, exec_command)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(command_message_handler)
        logging.info("Successfully initialized handlers")
    except Exception as e:
        logging.warning("Error intializing handlers")
        logging.error(str(e))
    updater.start_polling()

if __name__ == "__main__":
    main()