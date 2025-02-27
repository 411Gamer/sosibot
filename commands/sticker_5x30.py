import telebot
import lognotify

def sticker_5x30(bot, config):
    @bot.message_handler(func=lambda m: m.text.split()[0].lower()[1:] in config['call_list17'])
    def handler(message):
        print(lognotify.info(text=f"{message.from_user.first_name}: Используеть 5x30"))
        bot.send_sticker(message.chat.id, config['sticker_5x30_ID'])