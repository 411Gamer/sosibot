import telebot

def sticker_5x30(bot, config):
    @bot.message_handler(func=lambda message: message.text.split()[0].lstrip('.').lower() in config['call_list17'])
    def handler(message):
        bot.send_sticker(message.chat.id, config['sticker_5x30_ID'])