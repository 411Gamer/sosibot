import telebot
import os
from g4f.client import Client
import threading
import json

client = Client()
history = []


def ai(message, bot, config):
    caller = message.from_user.first_name
    text = message.text.split()
    del text[0]
    text = ' '.join(text)
    prompt = f"Сообщение от пользователя {caller}: {text}"

    if message.reply_to_message:
        prompt += f". Сообщение {message.reply_to_message.from_user.first_name} на которое отвечант {caller}, сообщение: {message.reply_to_message.text}"

    if os.path.exists(config['history_file']):
        with open(config['history_file'], 'r', encoding='utf-8') as f:
            history = json.load(f)
    else:
        history = []
        history.insert(0, config['system_prompt'])

    history.append({"role": "user", "content": prompt})
    with open(config['history_file'], 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history,
        web_search=False
    )

    print(f"{caller}: {prompt}")
    print(f"AI: {response.choices[0].message.content}\n")
    bot.reply_to(message, response.choices[0].message.content, parse_mode='Markdown')

def sosiAI(bot, config):
    @bot.message_handler(func=lambda message: any(message.text.lstrip('.').lower().startswith(wakeup_word) for wakeup_word in config['call_list12']))
    def handler(message):
        print(message.text)
        threading.Thread(target=ai, args=(message, bot, config)).start()