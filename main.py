from  telebot import *

# Создаем экземпляр бота
bot = telebot.TeleBot('5359515529:AAGQYh6_fD2QwKoldruDaYT771XodvaoPx4')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
@bot.message_handler(commands=["emir"])
def emir(m, res=False):
    bot.send_message(m.chat.id, 'эмирчик ')

@bot.message_handler(commands=['play'])
def kgb_message(message):
    markup = types.InlineKeyboardMarkup()
    k = types.InlineKeyboardButton(text="Камень", callback_data="Камень")
    g = types.InlineKeyboardButton(text="Ножницы", callback_data="Ножницы")
    b = types.InlineKeyboardButton(text="Бумага", callback_data="Бумага")

    markup.add(k, g, b)
    bot.send_message(message.chat.id, "Выберите один из предметов: ", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    city_list = ["Камень", "Ножницы", "Бумага"]
    kgb = random.choice(city_list)

    if call.data == 'Камень':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали: Камень", reply_markup=None)

    elif call.data == 'Ножницы':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали: Ножницы", reply_markup=None)
    elif call.data == 'Бумага':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали: Бумагу", reply_markup=None)

    if call.data == kgb:
        bot.send_message(call.message.chat.id, f"У вас ничья! Бот выбрал: {kgb}")

    elif call.data == "Камень":
        if kgb == "Ножницы":
            bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}")

        else:
            bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}")

    elif call.data == "Бумага":
        if kgb == "Камень":
            bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}")

        else:
            bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}")

    elif call.data == "Ножницы":
        if kgb == "Бумага":
            bot.send_message(call.message.chat.id, f"Вы победили! Бот выбрал: {kgb}")

        else:
            bot.send_message(call.message.chat.id, f"Вы проиграли! Бот выбрал: {kgb}")


bot.infinity_polling()
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])


def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
print('start')