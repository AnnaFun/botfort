import telebot
from flask import Flask, request
from telebot import TeleBot
from telebot.types import Update

app = Flask(__name__)


@app.route('/tg/')
def tg():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_update([update])
    return 'ok', 200


bot = telebot.TeleBot('1667764364:AAHfD7JMybA28m_MJwrkWutgd8Y_EzKXS5s', threaded=False)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, как ты себя чувствуешь?')
    elif message.text == 'Плохо':
        bot.send_message(message.from_user.id, 'Надеюсь, тебе станет лучше')
    elif message.text == 'Хорошо':
        bot.send_message(message.from_user.id, 'Это хорошо :)')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю :(')


bot.polling(none_stop=True)