import telebot

def svaston(bot, config):
    @bot.message_handler(func=lambda message: message.text.split()[0].lstrip('.').lower() in config['call_list8'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        reply = f"{caller} отправляет свастон. Поддерживаю."
    
        print(f"{caller}: {reply}")
        bot.send_sticker(message.chat.id, config['sticker_svaston_ID'])
        bot.reply_to(message, reply, parse_mode='Markdown')