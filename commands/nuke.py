import telebot
import lognotify

SosiBot = "[Sosi Bot](tg://resolve?domain=SosiBitara_bot)"

def nuke(bot, config):
    @bot.message_handler(func=lambda m: m.text.split()[0].lower()[1:] in config['call_list11'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        reply = f"{SosiBot} _добрался до пульта с ядеркой._"
    
        print(lognotify.info(text=f"{caller}: {reply}"))
        bot.reply_to(message, reply, parse_mode='Markdown')