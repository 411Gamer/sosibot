import telebot
import lognotify

def press_f(bot, config):
    @bot.message_handler(func=lambda m: m.reply_to_message is not None and m.text.split()[0].lower()[1:] in config['call_list4'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        reply = "✅ Уважение оказано."
    
        print(lognotify.info(text=f"{caller} обратился к {replied_user}: {reply}"))
        bot.reply_to(message, reply, parse_mode='Markdown')