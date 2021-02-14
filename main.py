import config
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

info = ('Приветствую.\n'
        'Данный бот в скором времени будет выполнять следующие функции:\n'
        '1. DDOS атака на номер должника.\n'
        '2. SMS флуд номера телефона.\n'
        '3. WhatsApp рассылка по базе номеров.\n'
        '4. Воспроизведение записи на номер должника.\n'
        '----------------------------\n'
        'В общем, данный проект предназначен для помощи арендодателям отстаивать свои права.\n'
        'Нажмите кнопку: ПОДПИСАТЬСЯ и вы получите уведомление когда проект будет запущен.\n'
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(info)

@dp.message_handler(commands=['admin'])
async def start(message: types.Message):
    await message.answer('Перейдите по ссылке:\nhttps://t.me/aivazanart')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)