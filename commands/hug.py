import telebot
import lognotify

def hug(bot, config):
    @bot.message_handler(func=lambda m: m.reply_to_message is not None and m.text.split()[0].lower()[1:] in config['call_list6'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        reply = f"{caller.title()} 🤗обнимает {replied_user}."
    
        print(lognotify.info(text=f"{caller} обратился к {replied_user}: {reply}"))
        bot.reply_to(message, reply, parse_mode='Markdown')