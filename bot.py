#version: v0.0.5
from telebot import TeleBot, types
import dbworker
import helper
import logging
import datetime
import json
import re
import os
import sys

def getConfig():
	try:
		# token, proxy = None, None
		file = None
		cwd = os.getcwd()
		for f in os.listdir(cwd):
			if f.endswith(".cfg"): file = f
		with open(file, 'r') as f: #потенциальная проблема из-за отсутствия файла
			parsedConfig = json.load(f)
		return (parsedConfig)
	except Exception as ex:
		raise ex

# logging.baseConfig(filename="debug.log", level=logging.DEBUG) # read the logging doc

config = getConfig()
bot = TeleBot(config['token'])

def main():
	global config
	global bot
	connection = dbworker.getConnection(config[database])
	# while True:
	# try: 
	bot.polling(none_stop = True)
	# except Exception as e:
	# 	logging.error(e)
	# 	print(e)

@bot.message_handler(regexp = "https?") #look for advanced url regexp  
def saveSong(message):
	deadline = datetime.datetime.now() + datetime.timedelta(days = 7)
	info = '{}\nПесня добавлена.\nТвой дедлайн : {}'.format(message.text, deadline)
	statusKeyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text = 'Lyrics X', callback_data = 'Lyrics +')
	button2 = types.InlineKeyboardButton(text = 'Tabs X', callback_data = 'Tabs +')
	statusKeyboard.row(button1,button2)
	# dbworker.insertData(connection, ','.join(message.chat.id, message.text, deadline))
	bot.send_message(message.chat.id, info, reply_markup = statusKeyboard)
	bot.delete_message(message.chat.id, message.message_id)
	
@bot.message_handler(commands = ['get_stats'])
def getBotStats(message):
	pass

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, helper.getHelp())
	pass

@bot.message_handler(content_types=['text'])
def reportShit(message):
	bot.send_message(message.chat.id, 'SHIT')

def getWeeklyStats():
	pass


if __name__ == '__main__':
	main()