import telebot

def minet(bot, config):
    @bot.message_handler(func=lambda message: message.text.split()[0].lstrip('.').lower() in config['call_list3'] and not message.reply_to_message)
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        lines = message.text.split()
        reply = f"Ты сделал(а) себе минет молодец {caller}! Ты кончил."

        if len(lines) == 2 and lines[1].lower() in config['list1']:
            reply = f"Ты сделал(а) смачный минет себе молодец {caller}! Вкусно получилось не так ли?"
        elif len(lines) == 2 and lines[1].lower() in config['list2']:
            reply = f"Ты сделал(а) сладкий минет себе молодец {caller}! Ты сожрал(а) свою кончу."

        bot.reply_to(message, reply, parse_mode='Markdown')