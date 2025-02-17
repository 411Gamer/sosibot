import telebot

SosiBot = "[Sosi Bot](tg://resolve?domain=SosiBitara_bot)"

def nuke(bot, config):
    @bot.message_handler(func=lambda message: message.text.split()[0].lstrip('.').lower() in config['call_list11'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        reply = f"{SosiBot} _добрался до пульта с ядеркой._"
    
        print(f"{caller}: {reply}")
        bot.reply_to(message, reply, parse_mode='Markdown')