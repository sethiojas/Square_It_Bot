from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import square

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	''' Replies with a Generic mesage to /start and /help commands'''
	context.bot.send_message(chat_id = update.message.chat_id, text = "I'm Square It bot! Send me and image and I'll "
		"square it for you!")

def Square_It(update, context):
	''' Replies with a Squared Image of the photo which is sent by the user '''
	
	#Download photo
	image = context.bot.getFile(update.message.photo[-1].file_id)
	file_name = os.path.join(os.getcwd(), f"{image.file_id}.jpg")
	image.download(custom_path = file_name)

	#Square the picture
	square.square_image(file_name)

	#Open the picture and send it
	file = open(file_name, 'rb')
	update.message.reply_photo(file)
	file.close()
	os.remove(file_name)
	
#Create Handlers
start_handler = CommandHandler(['start', 'help'], start)
photo_handler = MessageHandler(Filters.photo, Square_It)

#Deploy Handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(photo_handler)

#Check For updates
updater.start_polling()