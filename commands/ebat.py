import telebot

def ebat(bot, config):
    block_user = config['block_user']
    list1_4_5 = config['list4'] + config['list5'] + config['list1']

    @bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.split()[0].lstrip('.').lower() in config['call_list5'])
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        replied_user = f'[{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})'
        lines = message.text.split()
    
        print(f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}")
        if message.reply_to_message.from_user.first_name == block_user and config['block_toggle']:
            caller, replied_user = replied_user, caller
            bot.reply_to(message, f"Опасно! {caller} использует UNO Reverse!", parse_mode='Markdown')
            print(f"replied_user: {message.reply_to_message.from_user.first_name}, caller: {message.from_user.first_name}")

        reply = f"{replied_user} был(а) въебат(а) {caller}'ом."
        if len(lines) >= 2 and lines[1].lower() in list1_4_5:
            reply = f"{replied_user} был(а) {lines[1].lower()} въебат(а) {caller}'ом."
            if len(lines) >= 4:
                lines[2] = lines[2] + " " + lines[3]
                del lines[3]
                if lines[2].lower() in config['list3']:
                    reply = f"{replied_user} был(а) {lines[1].lower()} въебат(а) {lines[2].lower()} {caller}'ом."
        
        if len(lines) >= 3:
            lines[1] = lines[1] + " " + lines[2]
            del lines[2]
            print(lines)
        
        if len(lines) >= 3 and lines[1].lower() in config['list3']:
            reply = f"{replied_user} был(а) въебат(а) {lines[1].lower()} {caller}'ом."
            if lines[2].lower() in list1_4_5:
                reply = f"{replied_user} был(а) {lines[2].lower()} въебат(а) {lines[1].lower()} {caller}'ом."
       
    
        print(f"{caller} обратился к {replied_user}: {reply}")
        bot.send_sticker(message.chat.id, config['sticker_ebat_ID'])
        bot.reply_to(message, reply, parse_mode='Markdown')
