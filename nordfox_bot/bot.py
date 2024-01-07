import telebot

bot = telebot.TeleBot('6801850548:AAGmHjWXyCczSl8e2X9b1otAyPGs5M9qJrk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nКакой договор вам нужен?')

bot.polling(none_stop=True)