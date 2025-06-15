import telebot
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Салом! 👋 Aqiltop ботга хуш келибсан. Бу ерда сен мотивация, даромад идеялари ва фойдали маслаҳатлар оласан.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Ҳозирча мен тест режимидаман. Яқин кунларда кўпроқ функциялар қўшилади!")

bot.polling()
