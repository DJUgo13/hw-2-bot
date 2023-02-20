from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, db


async def quiz1(call: types.Message):
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
        open_period=15,
        reply_markup=markup
    )


def reg_client(db: Dispatcher):
    db.register_message_handler(quiz1, commands=['quiz'])
