import telebot
import lognotify

def minet(bot, config):
    @bot.message_handler(func=lambda m: m.text.split()[0].lower()[1:] in config['call_list3'] and not m.reply_to_message)
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        lines = message.text.split()
        reply = f"Ты сделал(а) себе минет молодец {caller}! Ты кончил."

        if len(lines) == 2 and lines[1].lower() in config['list1']:
            reply = f"Ты сделал(а) смачный минет себе молодец {caller}! Вкусно получилось не так ли?"
        elif len(lines) == 2 and lines[1].lower() in config['list2']:
            reply = f"Ты сделал(а) сладкий минет себе молодец {caller}! Ты сожрал(а) свою кончу."

        print(lognotify.info(text=f"{caller}: {reply}"))
        bot.reply_to(message, reply, parse_mode='Markdown')