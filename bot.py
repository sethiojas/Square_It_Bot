from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	''' Replies with a Generic mesage to /start and /help commands'''
	context.bot.send_message(chat_id = update.message.chat_id, text = "I'm Square It bot! Send me and image and I'll "
		"square it for you!")

def Square_It(update, context):
	''' Downloads pictures send by user '''
	image = context.bot.getFile(update.message.photo[-1].file_id)
	file_name = os.path.join(os.getcwd(), f"{image.file_id}.jpg")
	image.download(custom_path = file_name)
	
#Create Handlers
start_handler = CommandHandler(['start', 'help'], start)
photo_handler = MessageHandler(Filters.photo, Square_It)

#Deploy Handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(photo_handler)

#Check For updates
updater.start_polling()