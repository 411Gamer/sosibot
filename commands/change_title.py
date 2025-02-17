import lognotify
import telebot

def change_title(bot, config):
    @bot.message_handler(func=lambda m: len(m.text.split()) >= 2 and m.text.split()[0].lower()[1:] + " " + m.text.split()[1].lower() in config['call_list18'])
    def handler(m):
        if m.text.split()[2]:
            reply = f"Название группы было изменено на «_{m.text.split()[2]}_»."
            new_title = " ".join(m.text.split()[2:])
            bot.set_chat_title(m.chat.id, new_title)
            bot.reply_to(m, reply, parse_mode='Markdown')