#version: v0.0.2
import telebot, telebot.Types 
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
		bot = telebot.TeleBot(token)
		pass

@bot.message_handler(regex = "")
def saveSong(message):
	deadline = datetime.datetime.now() + datetime.timedelta(days = 7)
	info = '{}\nПесня добавлена.\nТвой дедлайн : {}'.format(message.text, deadline)
	kbStatus = Types.TeleBotCallbackKeoard()
	textDoneButton = Types.TeleBotCallbackButton(text = 'Lyrics X', callback_data = 'Lyrics +')
	tabsDoneButton = Types.TelebotCallbackButton(text = 'Tabs X', callback_data = 'Tabs +')
	kbStatus.add(textDoneButton)
	kbStatus.add(tabsDoneButton)
	bot.send_message(message.chat.id, info, callback = kbStatus)
	bot.delete_message(message.message_id)

@bot.message_handler(cotent_types=['text'])
def reportShit(message):
	bot.send_message(message.chat.id, 'SHIT')
	
if __name__ == '__main__':
	main()