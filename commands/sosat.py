import telebot
import lognotify

def sosat(bot, config):
    block_user = config['block_user']

    @bot.message_handler(func=lambda m: m.reply_to_message is not None and m.text.split()[0].lower()[1:] in config['call_list2'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        lines = message.text.split()
    
        print(lognotify.warning(text=f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}"))
        if message.reply_to_message.from_user.first_name == block_user and config['block_toggle']:
            caller, replied_user = replied_user, caller
            bot.reply_to(message, f"Опасно! {caller.title()} использует UNO Reverse!", parse_mode='Markdown')
            print(lognotify.warning(text=f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}"))
    
        reply = f"{replied_user.title()} отсосал(а) у тебя ({caller}). Хорошая робота."
        if len(lines) == 2 and lines[1].lower() in config['list1']:
            reply = f"Смачно {replied_user} соснул(а) у тебя ({caller}) и глотнул(а) твою кончу с довольным ебалом. Хорош."
        elif len(lines) == 2 and lines[1].lower() in config['list2']:
            reply = f"Сладко {replied_user} соснул(а) у тебя ({caller}). Молодец."
    
        print(lognotify.info(text=f"{caller} обратился к {replied_user}: {reply}"))
        bot.reply_to(message, reply, parse_mode='Markdown')