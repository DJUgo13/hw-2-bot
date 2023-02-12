from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands=['start', 'hello'])
async def start_handler(massege: types.Message):
    await bot.send_message(massege.from_user.id, f'hello {massege.from_user.first_name}')
    await massege.answer('пока что все ')


@db.message_handler()
async def echo(massege: types.Message):
    await bot.send_message(massege.from_user.id, massege.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)