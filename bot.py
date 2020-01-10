#version: v0.0.3
from telebot import TeleBot, types 
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
			file = f if f.endswith(".cfg") else None
		with open(file, 'r') as f: #потенциальная проблема из-за отсутствия файла
			parsedConfig = json.load(f)
		return (parsedConfig[token])
	except Exception as ex:
		raise ex

bot = None

def main():
	# add proxy 
	token = getConfig()
	bot = TeleBot(token)
	bot.polling()
	pass

@bot.message_handler(regex = "")
def saveSong(message):
	deadline = datetime.datetime.now() + datetime.timedelta(days = 7)
	info = '{}\nПесня добавлена.\nТвой дедлайн : {}'.format(message.text, deadline)
	kbStatus = types.InlineKeyboardMarkup()
	textDoneButton = types.InlineKeyboardButton(text = 'Lyrics X', callback_data = 'Lyrics +')
	tabsDoneButton = types.InlineKeyboardButton(text = 'Tabs X', callback_data = 'Tabs +')
	kbStatus.add(textDoneButton)
	kbStatus.add(tabsDoneButton)
	kbStatus.row(textDoneButton,tabsDoneButton) # фича конкретно этого прототипа . будет ли юзабельнее бургерных кнопок
	bot.send_message(message.chat.id, info, reply_markup = kbStatus)
	bot.delete_message(message.message_id)

@bot.message_handler(cotent_types=['text'])
def reportShit(message):
	bot.send_message(message.chat.id, 'SHIT')
	
@bot.message_handler(commands = ['get_stats'])
def getBotStats(message):
	pass

if __name__ == '__main__':
	main()