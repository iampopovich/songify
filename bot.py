#version: v0.0.62
from telebot import TeleBot, types
import dbworker
import helper
# import logging # добавлю позже
import datetime
import json
import re
import os
import sys

def getConfig():
	try:
		f = open('config.cfg','r')
		parsedConfig = json.load(f)
		f.close()
		return (parsedConfig)
	except IOError:
		print('Seems like something wrong with config file...')
		sys.exit()
	
# logging.baseConfig(filename='debug.log', level=logging.DEBUG) # read the logging doc
URLREGEXP = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
config = getConfig()
bot = TeleBot(config['token'])
dbworker.getConnection(config['database'])

def main():
	global config
	global bot
	# while True:
	# try: 
	bot.polling(none_stop = True)
	# except Exception as e:
	# 	logging.error(e)
	# 	print(e)

@bot.message_handler(regexp = URLREGEXP)  
def saveSong(message):
	global config
	deadline = datetime.date.today() + datetime.timedelta(days = 7)
	info = '{}\nПесня добавлена.\nТвой дедлайн : {}'.format(message.text, deadline)
	statusKeyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text = 'Lyrics X', callback_data = 'Lyrics +')
	button2 = types.InlineKeyboardButton(text = 'Tabs X', callback_data = 'Tabs +')
	statusKeyboard.row(button1,button2)
	bot.send_message(message.chat.id, info, reply_markup = statusKeyboard)
	bot.delete_message(message.chat.id, message.message_id)
	try:
		query = 'insert into userSongs values({},\'{}\',{},{},{})'.format(message.chat.id, message.text, deadline,0,0)
		dbworker.insertData(config['database'], query)
	except Exception as ex:
		print (ex)
		bot.send_message(message.chat.id, 'песня не записана в базу')
	
@bot.message_handler(commands = ['start'])
def startBot(message):
	global config
	query = 'select * from users where chatID = {} limit 1'.format(message.chat.id)
	if dbworker.checkData(config['database'],query):
		bot.send_message(message.chat.id, 'Вы уже пользовались ботом ранее. Запросите список песен командой /songs')
	else:
		query = 'insert into users values ({},\'\')'.format(message.chat.id)
		dbworker.insertData(config['database'], query)
	
@bot.message_handler(commands = ['get_stats'])
def getBotStats(message):
	global config
	query = 'select * from statistics where userID = {}'.format(message.chat.id)
	dataset = dbworker.getData(config['database'],query)
	if len(dataset) != 0 : bot.send_message(message.chat.id, '\n'.join(dataset))
	else: bot.send_message(message.chat.id, 'Статистики в базе не найдено')

@bot.message_handler(commands = ['songs'])
def getSongs(message):
	global config
	query = 'select * from userSongs where chatID = {}'.format(message.chat.id)
	dataset = dbworker.getData(config['database'], query)
	if len(dataset) != 0 : bot.send_message(message.chat.id, '\n'.join(map(str,dataset)))
	else: bot.send_message(message.chat.id, 'Песен в базе не найдено')

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, helper.getHelp())
	return None

@bot.message_handler(content_types=['text'])
def reportShit(message):
	bot.send_message(message.chat.id, 'SHIT')

def getWeeklyStats():
	pass

if __name__ == '__main__':
	main()