import time
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

bot_father_token="6078167339:AAFZGPXLHWjZ7ElMK0q2iR-ZTTR-6OizyWg"
logging.basicConfig(level=logging.INFO)

my_bot=Bot(token=bot_father_token)
my_dispatcher=Dispatcher(bot=my_bot)


@my_dispatcher.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Hello, I'm a bot")

if __name__ == '__main__':
    executor.start_polling(my_dispatcher,skip_updates=True)
