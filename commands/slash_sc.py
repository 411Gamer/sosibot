import lognotify
import random
import telebot
import os
from telebot.types import BotCommand
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
from datetime import datetime

commands_handler = [
    BotCommand("sc", "Испытать удачу с социальным кредитом.")
]

def slash_sc(bot, config):
    @bot.message_handler(commands=['sc'])
    def handler(m):
        if m.chat.type == 'private':
            markup = InlineKeyboardMarkup()
            add_bot_btn = InlineKeyboardButton("Добавить в группу", url=f"https://t.me/SosiBitara_Bot?startgroup=true")
            markup.add(add_bot_btn)
            bot.send_message(m.chat.id, "Я работаю только в группах (чатах)", reply_markup=markup)
            return None
        caller_id = m.from_user.id
        caller_tag = f"[{bot.get_chat_member(m.chat.id, caller_id).user.first_name}](tg://user?id={caller_id})"
        today = datetime.today().strftime("%Y-%m-%d")
        found = False
        
        os.makedirs(f"{config['ChatsSettings_path']}/{m.chat.id}", exist_ok=True)
        if os.path.exists(f"{config['ChatsSettings_path']}/{m.chat.id}/{config['SocialCreditDB_file']}"):
            with open(f"{config['ChatsSettings_path']}/{m.chat.id}/{config['SocialCreditDB_file']}", 'r') as f:
                data = json.load(f)
        else:
            data = {}
            
        size_add = random.choices(range(-10, 16), weights=[1]*10 + [3]*16)[0]
        if size_add < -10:
            size_add = -10
        
        for key, users in data.items():
            for user in users:
                if user["id"] == caller_id:
                    found = True
                    if user.get("last_played", "") == today:
                        reply = f"{caller_tag} уже играл(а) сегодня!\nСейчас он равен {user['credits']}.\nСледующая попытка завтра!"
                        bot.reply_to(m, reply, parse_mode='Markdown')
                    else:
                        user["credits"] += size_add
                        user["last_played"] = today
                        if size_add == 0:
                            reply = f"{caller_tag}, твой социальный кредит не изменился.\nСейчас он равен {user['credits']}.\nСледующая попытка завтра!"
                        elif size_add > 0:
                            reply = f"{caller_tag}, твой социальный кредит вырос на {size_add}.\nТеперь он равен {user['credits']}.\nСледующая попытка завтра!"
                        elif size_add < 0:
                            reply = f"{caller_tag}, твой социальный кредит сократился на {abs(size_add)}.\nТеперь он равен {user['credits']}.\nСледующая попытка завтра!"
                        
                        bot.reply_to(m, reply, parse_mode='Markdown')
                    break
            if found:
                break
        
        if not found:
            next_key = str(max(map(int, data.keys()), default=-1) + 1)
            data[next_key] = [{"id": caller_id, "credits": size_add, "last_played": today}]
            if size_add == 0:
                reply = f"{caller_tag}, твой социальный кредит не изменился.\nСейчас он равен {size_add}.\nСледующая попытка завтра!"
            elif size_add > 0:
                reply = f"{caller_tag}, твой социальный кредит вырос на {size_add}.\nТеперь он равен {size_add}.\nСледующая попытка завтра!"
            elif size_add < 0:
                reply = f"{caller_tag}, твой социальный кредит сократился на {abs(size_add)}.\nТеперь он равен {size_add}.\nСледующая попытка завтра!"

            bot.reply_to(m, reply, parse_mode='Markdown')
        
        print(lognotify.info(text=f"{m.from_user.first_name}: {reply}", text_case=None))
        with open(f"{config['ChatsSettings_path']}/{m.chat.id}/{config['SocialCreditDB_file']}", "w") as f:
            json.dump(data, f, indent=4)

