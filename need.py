import time
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import json

bot_father_token="6078167339:AAFZGPXLHWjZ7ElMK0q2iR-ZTTR-6OizyWg"
logging.basicConfig(level=logging.INFO)

my_bot=Bot(token=bot_father_token)
my_dispatcher=Dispatcher(bot=my_bot)




def my_func(code):
    standart_url=f"https://v6.exchangerate-api.com/v6/df0bb553472e34095631927e/latest/{code}"
    
    response=requests.get(standart_url)
    
    main_dict=json.loads(response.text)
    conversion_dict=main_dict['conversion_rates']
    
    search_currensy=str(code)
    to_rouble=conversion_dict['RUB']
    return {'my_currensy':search_currensy,
            'to_rouble':to_rouble}



@my_dispatcher.message_handler(commands=['start'])
async def start_handler(message: types.Message):

    usd=my_func('USD')
    #await message.reply(f"Current rates are:")
    await message.reply(f"Мазафакер,сейчас курс {usd['my_currensy']} к рублю равен {usd['to_rouble']}")
    
   

if __name__ == '__main__':
    executor.start_polling(my_dispatcher,skip_updates=True)
