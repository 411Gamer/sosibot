import telebot

def rastrel(bot, config):
    block_user = config['block_user']

    @bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.split()[0].lstrip('.').lower() in config['call_list7'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        reply = f"{caller} растрелял(а) {replied_user}."
    
        print(f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}")
        if message.reply_to_message.from_user.first_name == block_user and config['block_toggle']:
            caller, replied_user = replied_user, caller
            bot.reply_to(message, f"Опасно! {caller} использует UNO Reverse!", parse_mode='Markdown')
            print(f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}")
    
        print(f"{caller} обратился к {replied_user}: {reply}")
        bot.send_sticker(message.chat.id, config['sticker_rastrel_ID'])
        bot.reply_to(message, reply, parse_mode='Markdown')