# первым делом инструмент для бота (библиотеку)
import telebot;
from telebot import types;

token = '2101241794:AAESTzO7C0hgAK8J2PyK-LwnmGq-5Oe9qJw' # задаем токен: каким именно ботом будем управлять
bot = telebot.TeleBot(token) # пихаем бота в отдельную переменную

@bot.message_handler(commands=['start']) # отдельное приветствие
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
    
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler(content_types='text') # Теперь объявим метод для получения текстовых сообщений
def message_reply(message):
    if message.text=="Кнопка":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка 2")
        markup.add(item1)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    elif message.text=="Кнопка 2":
        bot.send_message(message.chat.id,'Спасибо за прочтение статьи!')
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.infinity_polling()