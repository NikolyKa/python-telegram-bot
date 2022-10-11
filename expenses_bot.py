from aiogram import Bot, Dispatcher,executor,types
import logging
API_TOKEN='5453208386:AAH3w7qPqHH81BokqvHo60C3BohgLY9UJiA'
logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! \nВыбери что делать дальше!')
@dp.message_handler()
async def echo(message :types.Message):
    await message.answer(message.text)
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)