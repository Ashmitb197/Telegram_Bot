import os
import telebot
from telebot.types import Message

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["hi"])
def hi(message):
    bot.send_message(message.chat.id, "Hello")

bot.polling()