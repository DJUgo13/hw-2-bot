from aiogram import types, Dispatcher
from config import bot, db


async def quiz2(call: types.CallbackQuery):
    ques = 'в какого аниме это фото?'
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


def reg_call_back(db: Dispatcher):
    db.register_message_handler(quiz2, text='button')
