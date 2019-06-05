import telebot
import pyjokes
import time
import json
import config
import datetime
import pytz
import traceback


TOKEN = "829593578:AAHlUspWbFlV287wEzXHAr3ZONjyp-EjCsQ"
bot = telebot.TeleBot(TOKEN)

chat_id= config.my_id
bot.get
bot.send_message(chat_id.id, 'Wake up!')