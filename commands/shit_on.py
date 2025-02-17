import telebot
import lognotify

def shit_on(bot, config):
    block_user = config['block_user']

    @bot.message_handler(func=lambda m: m.reply_to_message is not None and m.text.split()[0].lower()[1:] in config['call_list16'])
    def handler(m):
        caller = f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})'
        replied_user = f'[{m.reply_to_message.from_user.first_name}](tg://user?id={m.reply_to_message.from_user.id})'
        lines = m.text.split()
        
        print(lognotify.warning(text=f"replied_user: {m.reply_to_message.from_user.first_name}, caller: {m.from_user.first_name}"))
        if m.reply_to_message.from_user.first_name == block_user and config['block_toggle']:
            caller, replied_user = replied_user, caller
            bot.reply_to(m, f"Опасно! {caller.title()} использует UNO Reverse!", parse_mode='Markdown')
            print(lognotify.warning(text=f"replied_user: {m.reply_to_message.from_user.first_name}, caller: {m.from_user.first_name}"))
        
        reply = f"{caller.title()} обдристал {replied_user}. Еще если бы глаза витикали было бы харошо."
        
        if len(lines) >= 4:
            lines[1] = " ".join([lines[1], lines[2], lines[3], lines[4]]).strip()
            del lines[2:5]
        
        if len(lines) >= 2 and lines[1].lower() in config['list7']:
            reply = f"{caller.title()} обдристал {lines[1]} {replied_user}. _Настольгия...._"
    
        print(lognotify.info(text=f"{caller} обратился к {replied_user}: {reply}"))
        bot.reply_to(m, reply, parse_mode='Markdown')