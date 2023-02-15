from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = config('TOKEN')


bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('это ансфер')
    await massage.reply(massage.from_user.first_name)


@db.message_handler(commands=['quiz'])
async def quiz1(massage: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'кто ты воин?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='ты ахилесс',
        open_period=15,
        reply_markup=markup
    )


@db.callback_query_handler(text='button')
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'из кокого фильма это мем?'
    answer = [
        'бетмен',
        'криминально чтиво',
        'железный человек',
        'каратель',
        'первый мститель'
    ]
    photo = open('media/c55b9821089e04e5860f5354bb5d9929.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='это криминальное чтиво ты угадал',
        open_period=15
    )


@db.callback_query_handler(text='button')
async def quiz3(call: types.CallbackQuery):

    ques = 'из кокого аниме это фото?'
    answer = [
        'HOTD',
        'ангильские ритмы',
        'человек бензопила',
        'DxD',
        'необъятный океан'
    ]
    photo = open('media/d7c76398514577cd29fbf79636fdd59c.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='это DxD ты угадал',
        open_period=15
    )


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
