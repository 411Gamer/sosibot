import telebot
import lognotify

def ziga(bot, config):
    @bot.message_handler(func=lambda m: m.text.split()[0].lower()[1:] in config['call_list9'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        reply = f"{caller.title()} кидает зигу. Поддерживаю."
    
        print(lognotify.info(text=f"{caller}: {reply}"))
        bot.send_sticker(message.chat.id, config['sticker_ziga_ID'])
        bot.reply_to(message, reply, parse_mode='Markdown')