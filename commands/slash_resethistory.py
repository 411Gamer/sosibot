import os
import telebot
from telebot.types import BotCommand
import lognotify

def slash_resethistory(bot, config):
    @bot.message_handler(commands=['resethistory'])
    def handler(m):
        # if m.from_user.id == config['authorID']:
        chat_id = m.chat.id
        user_id = m.from_user.id
        admins = [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
        if user_id in admins:
            try:
                os.remove(config['history_file'])
                print(lognotify.info(text="History has been cleared"))
                bot.reply_to(m, "История браузера удалена.")
            except FileNotFoundError:
                print(lognotify.error(text=f"File {config['history_file']} Not Found"))
                bot.reply_to(m, f"File {config['history_file']} Not Found.")