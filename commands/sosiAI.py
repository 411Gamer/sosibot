import telebot
import os
from g4f.client import Client
import lognotify
import threading
import json

client = Client()
history = []


def ai(m, bot, config):
    caller = m.from_user.first_name
    text = m.text.split()
    del text[0]
    text = ' '.join(text)
    prompt = f"Сообщение от пользователя {caller}: {text}"

    if m.reply_to_message:
        prompt += f". Сообщение {m.reply_to_m.from_user.first_name} на которое отвечант {caller}, сообщение: {m.reply_to_m.text}"

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

    print(lognotify.info(text=f"{caller}: {prompt}"))
    
    if response.choices[0].message.content.startswith("<!DOCTYPE HTML PUBLIC"):
        print(lognotify.error(text="AI: Ошибка. Попытайтесь еще раз."))
        bot.reply_to(m, "Ошибка. Попытайтесь еще раз.")
    else:
        print(lognotify.info(text=f"AI: {response.choices[0].message.content}\n"))
        bot.reply_to(m, response.choices[0].message.content, parse_mode='Markdown')

def sosiAI(bot, config):
    @bot.message_handler(func=lambda m: any(m.text.lower()[1:].startswith(wakeup_word) for wakeup_word in config['call_list12']))
    def handler(m):
        threading.Thread(target=ai, args=(m, bot, config)).start()