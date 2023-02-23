from aiogram import types, Dispatcher
from config import bot, dp


async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')


def reg_hand_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
