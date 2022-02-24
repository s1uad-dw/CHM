from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

import no_line_equation
import general_functions

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
        π - math.pi
        e - math.exp(x)
        logᵧ(x) - math.log(x, y)
        xⁿ - (x**n)
        sin(x) - math.sin(x)
        cos(x) - math.cos(x)
        tg(x) - math.tan(x)
        ctg(x) - math.atan(x)
        rad => ° - math.degress(x)
        ° => rad - math.radians(x)
        ''')
        
    elif '?' in message.text:
        list = (message.text[1:]).split('#')

        if type(no_line_equation.half_division(float(list[0]), float(list[1]), float(list[2]), list[3]))==type(list):
            doc = open(general_functions.create_excel(list[3], no_line_equation.half_division(float(list[0]), float(list[1]), float(list[2]), list[3]), ['k', 'aₖ', 'f(aₖ)','bₖ', 'f(bₖ)', 'cₖ', 'f(cₖ)', 'εₖ']) + '.xlsx', 'rb')
            await bot.send_document(message.from_user.id, doc)
            os.remove(doc.name)
        else: 
            await bot.send_message(message.from_user.id, 'Не решается методом половинного деления')

        if type(no_line_equation.chord(float(list[0]), float(list[1]), float(list[2]), list[3]))==type(list):
            doc = open(general_functions.create_excel(list[3], no_line_equation.chord(float(list[0]), float(list[1]), float(list[2]), list[3]), ['n', 'xₙ', 'f(xₙ)','b - xₙ', 'εₙ']) + '.xlsx', 'rb')
            await bot.send_document(message.from_user.id, doc)
            os.remove(doc.name)
        else:
            await bot.send_message(message.from_user.id, 'Не решается методом хорд')
        
        if type(no_line_equation.tangent(float(list[0]), float(list[1]), float(list[2]), list[3]))==type(list):
            doc = open(general_functions.create_excel(list[3], no_line_equation.tangent(float(list[0]), float(list[1]), float(list[2]), list[3]), ['n', 'xₙ', 'f(xₙ)',"f'(xₙ)", 'εₙ']) + '.xlsx', 'rb')
            await bot.send_document(message.from_user.id, doc)
            os.remove(doc.name)
        else:
            await bot.send_message(message.from_user.id, 'Не решается методом касательных')
        
        if type(no_line_equation.komb(float(list[0]), float(list[1]), float(list[2]), list[3]))==type(list):
            doc = open(general_functions.create_excel(list[3], no_line_equation.komb(float(list[0]), float(list[1]), float(list[2]), list[3]), ['n', 'xₙ', '!xₙ', 'f(!xₙ)',"f'(!xₙ)", '-ε(!xₙ)' , 'f(xₙ)', '-ε(a)']) + '.xlsx', 'rb')
            await bot.send_document(message.from_user.id, doc)
            os.remove(doc.name)
        else:
            await bot.send_message(message.from_user.id, 'Не решается комбинированным методом хорд и касательных')

executor.start_polling(dp, skip_updates=True)