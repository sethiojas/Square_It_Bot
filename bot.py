from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import os
import square
import telegram

#initialize updater and dispatcher
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
	''' Replies with a Generic mesage to /start and /help commands'''
	context.bot.send_message(chat_id = update.message.chat_id, text = "I'm Square It bot! Send me an image and I'll "
		"square it for you!")

def Square_It(update, context):
	''' Saves picture locally and asks the user for the colour of background '''
	
	#Download photo
	image = context.bot.getFile(update.message.photo[-1].file_id)
	FILE_NAME = os.path.join(os.getcwd(), f"{image.file_id}.jpg")
	image.download(custom_path = FILE_NAME)
	
	#save path in file
	with open("name.txt", 'w') as f:
		f.write(FILE_NAME)

	#Custom inline keyboard to present an option of black or white background for
	#squared image
	custom_keyboard = [[telegram.InlineKeyboardButton('White', callback_data = 'White')],
 					[telegram.InlineKeyboardButton('Black', callback_data = 'Black')]]
	
	reply_markup = telegram.InlineKeyboardMarkup(custom_keyboard)
	
	context.bot.send_message(chat_id=update.message.chat_id,
	                 text="Please choose the background colour",
	                 reply_markup=reply_markup)

def callback(update, context):
	'''
	Sends the square image according to the
	Background color choice.
	Deletes the local copy of the picture
	'''

	query = update.callback_query
	colour = query.data #selected color as per user input

	query.edit_message_text(text=f"Selected option: {colour}")
    
    #get File path
	with open("name.txt", 'r') as f:
		FILE_NAME = f.read()
	FILE_NAME = FILE_NAME.strip()
   
	square.square_image(FILE_NAME, colour)
    
	file = open(FILE_NAME, 'rb')
	context.bot.send_photo(caption = "Here you go!", chat_id = query.message.chat_id, photo = file)
   
	file.close()
	os.remove(FILE_NAME)
	os.remove('name.txt')

#Create Handlers
start_handler = CommandHandler(['start', 'help'], start)
photo_handler = MessageHandler(Filters.photo, Square_It)
callback_handler = CallbackQueryHandler(callback)

#Deploy Handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(callback_handler)

#Check For updates
updater.start_polling()