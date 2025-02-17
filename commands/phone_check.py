import telebot
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberFormat, number_type

def get_phone_info(number):
    region = None
    try:
        num = phonenumbers.parse(number, region)
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Error: Incorrect number format!"
    type_mapping = {
        0: "Неизвестный",
        1: "Стационарный (городской)",
        2: "Мобильный",
        3: "VoIP",
        4: "Бесплатный",
        5: "Премиум",
        6: "Персональный",
        7: "Пейджер",
        8: "UAN",
        9: "Экстренный",
        10: "Голосовая почта",
        27: "Не географический",
    }

    info = {
        "E.164 формат": phonenumbers.format_number(num, PhoneNumberFormat.E164),
        "Код страны": num.country_code,
        "Регион": geocoder.description_for_number(num, "ru"),
        "Времиная зона": ", ".join(timezone.time_zones_for_number(num)),
        "Тип номера": type_mapping.get(number_type(num), "Неизвестный"),
        "Оператор": carrier.name_for_number(num, "ru"),
        "Валидный": "Да" if phonenumbers.is_valid_number(num) else "Нет",
        "Возможный": "Да" if phonenumbers.is_possible_number(num) else "Нет",
    }

    output = "\n".join(f"{key}: {value}" for key, value in info.items())
    return output

def phone_check(bot, config):
    @bot.message_handler(func=lambda message: len(message.text.split()) > 1 and message.text.split()[0].lstrip('.').lower() in config['call_list13'])
    # @bot.message_handler(func=lambda message: True)
    def handler(message):
        caller = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
        phone = message.text.split()[1]
        reply = get_phone_info(phone)

        print(f"{caller}: {reply}")
        bot.reply_to(message, reply, parse_mode='Markdown')