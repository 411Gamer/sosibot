import lognotify
import random
import telebot
from telebot.types import BotCommand
import json
from datetime import datetime


def slash_dick(bot, config):
    @bot.message_handler(commands=['dick'])
    def handler(m):
        caller_id = m.from_user.id
        caller_tag = f"[{bot.get_chat_member(m.chat.id, caller_id).user.first_name}](tg://user?id={caller_id})"
        today = datetime.today().strftime("%Y-%m-%d")
        found = False
        
        with open(config['dickDatabase_file'], "r") as f:
            data = json.load(f)
            
        size_add = round(random.gauss(1, 3))
        if size_add < -10:
            size_add = -10
        
        for key, users in data.items():
            for user in users:
                if user["id"] == caller_id:
                    found = True
                    if user.get("last_played", "") == today:
                        reply = f"{caller_tag} уже играл(а) сегодня!\nСейчас он равен {user['size']} см.\nСледующая попытка завтра!"
                        bot.reply_to(m, reply, parse_mode='Markdown')
                    else:
                        user["size"] += size_add
                        user["last_played"] = today
                        if size_add == 0:
                            reply = f"{caller_tag}, твой писюн не изменился.\nСейчас он равен {user['size']} см.\nСледующая попытка завтра!"
                        elif size_add > 0:
                            reply = f"{caller_tag}, твой писюн вырос на {size_add} см.\nТеперь он равен {user['size']} см.\nСледующая попытка завтра!"
                        elif size_add < 0:
                            reply = f"{caller_tag}, твой писюн сократился на {abs(size_add)} см.\nТеперь он равен {user['size']} см.\nСледующая попытка завтра!"
                        
                        bot.reply_to(m, reply, parse_mode='Markdown')
                    break
            if found:
                break
        
        if not found:
            next_key = str(max(map(int, data.keys()), default=-1) + 1)
            data[next_key] = [{"id": caller_id, "size": size_add, "last_played": today}]
            if size_add == 0:
                reply = f"{caller_tag}, твой писюн не изменился.\nСейчас он равен {size_add} см.\nСледующая попытка завтра!"
            elif size_add > 0:
                reply = f"{caller_tag}, твой писюн вырос на {size_add} см.\nТеперь он равен {size_add} см.\nСледующая попытка завтра!"
            elif size_add < 0:
                reply = f"{caller_tag}, твой писюн сократился на {abs(size_add)} см.\nТеперь он равен {size_add} см.\nСледующая попытка завтра!"

            bot.reply_to(m, reply, parse_mode='Markdown')
        
        print(lognotify.info(text=f"{m.from_user.first_name}: {reply}"))
        with open(config['dickDatabase_file'], "w") as f:
            json.dump(data, f, indent=4)

