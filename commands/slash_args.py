import telebot
import json
from telebot.types import BotCommand

def slash_args(bot, config):
    AliasesCommands = f"""
С агрументами:
Отсос — {', '.join(config['call_list1'])}.
└ {', '.join(config['list1'])}, {', '.join(config['list5'])}.

Соси — {', '.join(config['call_list2'])}.
└ {', '.join(config['list1'])}, {', '.join(config['list5'])}.

Минет — {', '.join(config['call_list3'])}.
└ {', '.join(config['list1'])}, {', '.join(config['list5'])}.

Выебать — {', '.join(config['call_list5'])}.
├ Три аргумента. Пример: ".выебать сильно в жопу"
├ {', '.join(config['list1'])}.
└ {', '.join(config['list3'])}, {', '.join(config['list4'])}, {', '.join(config['list5'])}.

Пиздить — {', '.join(config['call_list10'])}.
└ {', '.join(config['list6'])}.

Обосрать — {', '.join(config['call_list16'])}.
└ {', '.join(config['list7'])}.

инфо — {', '.join(config['call_list13'])}.
└ Напишите номер.

Без аргументов:
Обнять  {', '.join(config['call_list6'])}.
Растрелять — {', '.join(config['call_list7'])}.
Свастон — {', '.join(config['call_list8'])}.
Зига — {', '.join(config['call_list9'])}.
Ядерка — {', '.join(config['call_list11'])}.
Задрот — {', '.join(config['call_list12'])}.
+ — {', '.join(config['call_list4'])}.
найти пидора — {', '.join(config['call_list14'])}.
5x30 — {', '.join(config['call_list17'])}.
обоссать — {', '.join(config['call_list15'])}.

Для вызова команды нужно написать перед ней точку, пример: ".пиздить ногами"
"""
    @bot.message_handler(commands=['args'])
    def handler(m):
        bot.reply_to(m, AliasesCommands)