import telebot

def otsos(bot, config):
    @bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.split()[0].lstrip('.').lower() in config['call_list1'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        lines = message.text.split()
        reply =  f"{lines[0]} сделан для {replied_user} от {caller}."
    
        if len(lines) == 2 and lines[1].lower() in config['list1']:
            reply = f"{replied_user} поздравляю тебе смачно соснули, а точнее {caller}! Ты кочнил(а) ему прямо в рот."
        elif len(lines) == 2 and lines[1].lower() in config['list2']:
            reply = f"{replied_user} поздравляю тебе сладко соснули, а точнее {caller}! Конча полетела прямо в рот."
    
        print(f"{caller} обратился к {replied_user}: {reply}")
        bot.reply_to(message, reply, parse_mode='Markdown')
