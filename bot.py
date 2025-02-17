import os
import json
import lognotify
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
                    print(lognotify.debug(text=f"Module {file.lower()} loaded successfully"))
                else:
                    print(lognotify.info(text=f"Function {file[:-3]} not found in {module_name}"))
            except Exception as e:
                print(lognotify.error(text=f"Error loading {module_name}: {e}"))
    else:
        print("\033[2D ")
        print(lognotify.debug(text="All modules loaded successfully."))


bot.set_my_commands([
    BotCommand("help", "Помощь."),
    BotCommand("args", "Показывает доступные синонимы для команд."),
    BotCommand("dick", "Вырастить пиписю"),
    BotCommand("top_dick", "Топ 10 пипись чата")
])

register_handlers(bot, config)
print(lognotify.info(text="Bot was launched.\n"))
try:
    bot.polling(none_stop=True, skip_pending=True, timeout=99999999)
except KeyboardInterrupt:
    print(lognotify.warning(text="The bot has been turned off.\n"))
