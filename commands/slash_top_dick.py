import lognotify
import json
import telebot
from telebot.types import BotCommand

def slash_top_dick(bot, config):
    @bot.message_handler(commands=['top_dick'])
    def handler(m):
        with open(config['dickDatabase_file'], 'r') as f:
            database = json.load(f)

        table = "Топ 10 пипись игроков в чате\n\n"
        players = sorted(
            [(database[i][0], i) for i in database if isinstance(database[i], list) and database[i]],  
            key=lambda x: x[0]['size'], reverse=True
        )[:10]

        for num, (player, _) in enumerate(players, start=1):
            table += f"{num}┤ [{bot.get_chat_member(m.chat.id, player['id']).user.first_name}](tg://user?id={player['id']}) — {player['size']} см.\n"

        bot.reply_to(m, table, parse_mode='Markdown')
