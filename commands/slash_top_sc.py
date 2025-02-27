import lognotify
import os
import json
import telebot
from telebot.types import BotCommand
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

commands_handler = [
    BotCommand("top_sc", "Топ 10 социальных кредитов чата")
]


def slash_top_sc(bot, config):
    @bot.message_handler(commands=['top_sc'])
    def handler(m):
        if m.chat.type == 'private':
            markup = InlineKeyboardMarkup()
            add_bot_btn = InlineKeyboardButton("Добавить в группу", url=f"https://t.me/SosiBitara_Bot?startgroup=true")
            markup.add(add_bot_btn)
            bot.send_message(m.chat.id, "Я работаю только в группах (чатах)", reply_markup=markup)
            return

        if f"@{bot.get_me().username}" not in m.text:
            return
        caller = f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})'

        if os.path.exists(f"{config['ChatsSettings_path']}/{m.chat.id}/{config['SocialCreditDB_file']}"):
            with open(f"{config['ChatsSettings_path']}/{m.chat.id}/{config['SocialCreditDB_file']}", 'r') as f:
                database = json.load(f)
        else:
            bot.send_message(m.chat.id, "Никто еще не использовал /sc.")
            return

        table = "Топ 10 социального кредита чата\n\n"
        players = sorted(
            [(database[i][0], i) for i in database if isinstance(database[i], list) and database[i]],  
            key=lambda x: x[0]['credits'], reverse=True
        )[:10]

        for num, (player, _) in enumerate(players, start=1):
            table += f"{num}┤ {bot.get_chat_member(m.chat.id, player['id']).user.first_name} — {player['credits']} кредитов.\n"

        print(lognotify.info(text=f"{caller}: Использует /top_sc", text_case=None))
        bot.reply_to(m, table)
