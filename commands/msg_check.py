import telebot
import re

tiktok_pattern = r'https?://(www\.)?vm\.tiktok\.com|https?://(www\.)?tiktok\.com'
instagram_pattern = r'https?://(www\.)?instagram\.com'

def msg_check(bot, config):
    @bot.message_handler(func=lambda message: True)
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        ponos_text = message.text.lower()
    
        if re.search(tiktok_pattern, ponos_text):
            reply = "Фу блять убери это говно. Я не хочу дегродировать как ты. Я твою мать ебал с этим твоим тики током."
        elif re.search(instagram_pattern, ponos_text):
            reply = "Опять эта хрень нахуя ты это скидиваешь в этот чат никто не хочет смотреть твой тупой инстаграм."
        else:
            reply = None
    
        if reply:
            print(f"{caller}: {reply}")
            bot.reply_to(message, reply, parse_mode='Markdown')