import math
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import backend
bot = Bot(token='5052571361:AAEqq9WtciFV0V82ruIo8iib2_UqWW1oP-Q')
dp = Dispatcher(bot)

help_cmd = ['!help', '!h', '/help', '/h']

@dp.message_handler()
async def take_message(message: types.Message):
    if message.text == '/start':
        await bot.send_message(message.from_user.id, 'Бот для решения "Нелинейный управлений"')
        await bot.send_message(message.from_user.id, '?a₀,b₀,ε,ƒ(x)')
        await bot.send_message(message.from_user.id, '''
        Отправь мне сообщение таким шаблоном, где:
        ‣a₀ - начало отрезка;
        ‣b₀ - конец отрезка;
        ‣ε - погрешность;
        ‣ƒ(x) - уравнение функции
        ''')
    elif message.text in help_cmd:
        await bot.send_message(message.from_user.id, 
        '''
        Подсказка:\n
        π - math.pi\n
        e - math.exp(x)\n
        logᵧ(x) - math.log(x, y)\n
        xⁿ - math.pow(x, n)\n
        sin(x) - math.sin(x)\n
        cos(x) - math.cos(x)\n
        tg(x) - math.tan(x)\n
        ctg(x) - math.atan(x)\n
        rad => ° - math.degress(x)\n
        ° => rad - math.radians(x)
        ''')
    elif '?' in message.text:
        list = (message.text[1:]).split(',')
        print(list)

executor.start_polling(dp, skip_updates=True)