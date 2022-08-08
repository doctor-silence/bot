from lib2to3.pgen2 import token
import telebot

bot_client = telebot.TeleBot(token='5477763774:AAHesdvLdwnzKAe0R0AW7T1j-ENoEUuo8xc')

@bot_client.massage_handler(commands=['start'])
def echo(massage):
    c = 1

bot_client.polling()
