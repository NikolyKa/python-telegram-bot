import telebot
from telebot import types
import requests, bs4

TOKEN = '5313055857:AAFMrBIdJQvZD4h9YKkzqdG65BL3TOGt9rs'
BOT = telebot.TeleBot(TOKEN)


@BOT.message_handler(commands=['start', 'help'])
def hello(message):
    BOT.send_message(message.chat.id, 'Здравствуйте! Введите \'погода\', \'новости\' или \'курс валют\'.')


@BOT.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Погода')
    item2 = types.KeyboardButton('Новости')
    item3 = types.KeyboardButton('Курс Валют')
    markup.add(item1, item2, item3)
    BOT.send_message(message.chat.id, 'Выберите что вам нужно', reply_markup=markup)


def get_news(quantity_news=5):
    s = requests.get('https://lenta.ru/rubrics/russia/moscow/')
    filtered_news = []
    soup = bs4.BeautifulSoup(s.text, 'html.parser')
    all_news = soup.findAll('h3', class_='card-full-news__title')
    for data in all_news:
        if len(filtered_news) <= quantity_news:
            filtered_news.append(data.text)
    return filtered_news


def get_exchange_rates():
    s = requests.get('http://www.finmarket.ru/currency/rates/')
    soup = bs4.BeautifulSoup(s.text, 'html.parser')
    all_courses = soup.findAll('div', class_='value')
    filtered_rates = [data.text for data in all_courses if data is not None]
    return filtered_rates


def get_weather():
    weather_list = []
    s = requests.get('https://sinoptik.ua/погода-москва')
    b = bs4.BeautifulSoup(s.text, 'html.parser')
    p3 = b.select('.temperature .p3')
    weather1 = p3[0].getText()
    weather_list.append(weather1)
    p4 = b.select('.temperature .p4')
    weather2 = p4[0].getText()
    weather_list.append(weather2)
    p5 = b.select('.temperature .p5')
    weather3 = p5[0].getText()
    weather_list.append(weather3)
    p6 = b.select('.temperature .p6')
    weather4 = p6[0].getText()
    weather_list.append(weather4)
    p7 = b.select('.temperature .p7')
    weather5 = p7[0].getText()
    weather_list.append(weather5)
    p8 = b.select('.temperature .p8')
    weather6 = p8[0].getText()
    weather_list.append(weather6)
    p = b.select('.rSide .description')
    description = p[0].getText()
    weather_list.append(description)
    return weather_list


@BOT.message_handler(content_types=['text'])
def message_reply(message):
    if message.text.lower() == 'погода' or message.text.lower() == 'weather':
        BOT.send_message(message.chat.id, 'Погода в Москве:')
        BOT.send_message(message.chat.id, f'Погода утром : {get_weather()[0]}  {get_weather()[1]}')
        BOT.send_message(message.chat.id, f'Погода днём : {get_weather()[2]}  {get_weather()[3]}')
        BOT.send_message(message.chat.id, f'Погода вечером : {get_weather()[4]}  {get_weather()[5]}')
        BOT.send_message(message.chat.id, get_weather()[6].strip())

    elif message.text.lower() == 'новости' or message.text.lower() == 'news':
        BOT.send_message(message.chat.id, 'Новости Москвы: ')
        for data in get_news():
            BOT.send_message(message.chat.id, data)
    elif message.text.lower() == 'курс валют' or message.text.lower() == 'exchange rates':
        BOT.message_handler(message.chat.id, 'Курс валют: ')
        BOT.send_message(message.chat.id, f'USD: {get_exchange_rates()[0]} rub')
        BOT.send_message(message.chat.id, f'EUR: {get_exchange_rates()[1]} rub')
        BOT.send_message(message.chat.id, f'GBP: {get_exchange_rates()[2]} rub')
        BOT.send_message(message.chat.id, f'CHF: {get_exchange_rates()[3]} rub')
    else:
        BOT.send_message(message.chat.id, 'Введите другую команду')


BOT.infinity_polling()
