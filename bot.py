#version: v0.0.4
from telebot import TeleBot, types
import dbworker
import logging # in v0.0.5
# import time
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

# def initBot(config):
# 	return TeleBot(config['token'])

config = getConfig()
bot = TeleBot(config['token'])

def main():
	# global config
	# connection = dbworker.getConnection(config[database])
	global bot
	# while True:
	# try: 
	bot.polling(none_stop = True)
	# except Exception as e:
	# 	logging.error(e)
	# 	print(e)

@bot.message_handler(regexp = "https?")
def saveSong(message):
	deadline = datetime.datetime.now() + datetime.timedelta(days = 7)
	info = '{}\nПесня добавлена.\nТвой дедлайн : {}'.format(message.text, deadline)
	kbStatus = types.InlineKeyboardMarkup()
	textDoneButton = types.InlineKeyboardButton(text = 'Lyrics X', callback_data = 'Lyrics +')
	tabsDoneButton = types.InlineKeyboardButton(text = 'Tabs X', callback_data = 'Tabs +')
	kbStatus.row(textDoneButton,tabsDoneButton)
	bot.send_message(message.chat.id, info, reply_markup = kbStatus)
	bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=['text'])
def reportShit(message):
	bot.send_message(message.chat.id, 'SHIT')
	
@bot.message_handler(commands = ['get_stats'])
def getBotStats(message):
	pass

@bot.message_handler(commands = ['help'])
def help(message):
	pass

def getWeeklyStats():
	pass


if __name__ == '__main__':
	main()