import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()

telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
web_app_url = os.getenv('WEB_APP_URL')

bot = telebot.TeleBot()


@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    webUrl = types.WebAppInfo(web_app_url)
    web_btn = types.InlineKeyboardButton(text='НАЖМИ!', web_app=webUrl)
    markup.add(web_btn)
    bot.send_message(message.from_user.id, "Давай давай оп оп", reply_markup = markup)


if __name__ == '__main__':
    bot.infinity_polling()
