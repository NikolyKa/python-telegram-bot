import telebot
import requests,bs4
token='5313055857:AAFMrBIdJQvZD4h9YKkzqdG65BL3TOGt9rs'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,'Здравствуйте! Введите "погода", чтобы узнать погоду в Калининграде.')
@bot.message_handler(content_types=['text'])
def weathers(message):
    s = requests.get('https://sinoptik.ua/погода-калининград')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.select('.temperature .p3')
    pogoda1 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    pogoda2 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    pogoda3 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    pogoda4 = p6[0].getText()
    p7=b.select('.temperature .p7')
    pogoda5=p7[0].getText()
    p8=b.select('.temperature .p8')
    pogoda6=p8[0].getText()
    p = b.select('.rSide .description')
    pogoda = p[0].getText()
    if message.text.lower()=='погода':
        bot.send_message(message.chat.id, 'Погода утром :' + pogoda1 + ' ' + pogoda2)
        bot.send_message(message.chat.id,'Погода днём :' + pogoda3 + ' ' + pogoda4)
        bot.send_message(message.chat.id,'Погода вечером :'+pogoda5+' '+pogoda6)
        bot.send_message(message.chat.id,pogoda.strip())
    else:
        bot.send_message(message.chat.id,'Введите другую команду')
bot.polling()