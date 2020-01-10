#version: v0.0.2
import telebot, telebot.Types 
# import time
import datetime
import json
import re

def getConfig():
	pass

bot = telebot.TeleBot()

def main():
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

if __name__ == '__main__':
	main()