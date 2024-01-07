import telebot
import settings

bot = telebot.TeleBot(settings.API_KEY)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nКакой договор вам нужен?')

bot.polling(none_stop=True)