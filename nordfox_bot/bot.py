import telebot
from telebot import types
import settings

bot = telebot.TeleBot(settings.API_KEY)

@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nВыберите, какие документы вы хотите получить:')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Договор поставки'))
    markup.add(types.InlineKeyboardButton('Договор проектирования'))
    markup.add(types.InlineKeyboardButton('Запрос документов от контрагента'))
    markup.add(types.InlineKeyboardButton('Документы в ответ на запрос покупателя'))
    bot.send_message(reply_markup = markup)
bot.polling(none_stop=True)