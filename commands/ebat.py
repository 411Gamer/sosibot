import telebot
import lognotify

def ebat(bot, config):
    block_user = config['block_user']
    list1_4_5 = config['list4'] + config['list5'] + config['list1']

    @bot.message_handler(func=lambda m: m.reply_to_message is not None and m.text.split()[0].lower()[1:] in config['call_list5'])
    def handler(m):
        caller = f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})'
        replied_user = f'[{m.reply_to_message.from_user.first_name}](tg://user?id={m.reply_to_message.from_user.id})'
        lines = m.text.split()
    
        print(lognotify.warning(text=f"replied_user: {replied_user}, caller: {caller}"))
        if m.reply_to_message.from_user.id == block_user and config['block_toggle']:
            caller, replied_user = replied_user, caller
            bot.reply_to(m, f"Опасно! {caller.title()} использует UNO Reverse!", parse_mode='Markdown')
            print(lognotify.warning(text=f"replied_user: {replied_user}, caller: {caller}"))


        reply = f"{replied_user.title()} был(а) въебат(а) {caller}'ом."
        if len(lines) >= 2 and lines[1].lower() in list1_4_5:
            reply = f"{replied_user.title()} был(а) {lines[1].lower()} въебат(а) {caller}'ом."
            if len(lines) >= 4:
                lines[2] = lines[2] + " " + lines[3]
                del lines[3]
                if lines[2].lower() in config['list3']:
                    reply = f"{replied_user.title()} был(а) {lines[1].lower()} въебат(а) {lines[2].lower()} {caller}'ом."

        if len(lines) >= 3:
            lines[1] = lines[1] + " " + lines[2]
            del lines[2]

        if len(lines) >= 3 and lines[1].lower() in config['list3']:
            reply = f"{replied_user.title()} был(а) въебат(а) {lines[1].lower()} {caller}'ом."
            if lines[2].lower() in list1_4_5:
                reply = f"{replied_user.title()} был(а) {lines[2].lower()} въебат(а) {lines[1].lower()} {caller}'ом."


        print(lognotify.info(text=f"{caller} обратился к {replied_user}: {reply}"))
        bot.send_sticker(m.chat.id, config['sticker_ebat_ID'])
        bot.reply_to(m, reply, parse_mode='Markdown')