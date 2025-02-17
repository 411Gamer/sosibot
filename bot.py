import os
import json
import importlib
import telebot
from telebot.types import BotCommand

with open("config.json") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["token"])

def register_handlers(bot, config):
    modules = sorted(os.listdir("commands"), key=lambda x: x == "msg_check.py")
    for file in modules:
        if file.endswith(".py"):
            module_name = f"commands.{file[:-3]}"
            try:
                module = importlib.import_module(module_name)
                command_func = getattr(module, file[:-3], None)
                if callable(command_func):
                    command_func(bot, config)
                else:
                    print(f"Функция {file[:-3]} не найдена в {module_name}")
            except Exception as e:
                print(f"Ошибка при загрузке {module_name}: {e}")

bot.set_my_commands([
    BotCommand("help", "Помощь."),
    BotCommand("args", "Показывает доступные синонимы для команд.")
])

register_handlers(bot, config)
print("Bot was launched.")
bot.polling(none_stop=True, skip_pending=True, timeout=99999999)
