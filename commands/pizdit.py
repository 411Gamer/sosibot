import telebot

def pizdit(bot, config):
    block_user = config['block_user']

    @bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.split()[0].lstrip('.').lower() in config['call_list10'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        lines = message.text.split()
    
        print(f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}")
        if message.reply_to_message.from_user.first_name == block_user and config['block_toggle']:
            caller, replied_user = replied_user, caller
            bot.reply_to(message, f"Опасно! {caller} использует UNO Reverse!", parse_mode='Markdown')
            print(f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}")
    
        reply = f"{replied_user} был(а) отпизден(а) {caller}. Имба."
        if len(lines) == 2 and lines[1].lower() in config['list6']:
            reply = f"{replied_user} был(а) отпизден(а) {caller} {lines[1]}. Почему раньше не сделал таких нужно пиздить {lines[1]}."
    
        print(f"{caller} обратился к {replied_user}: {reply}")
        bot.reply_to(message, reply, parse_mode='Markdown')