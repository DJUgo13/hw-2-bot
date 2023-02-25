from aiogram import types, Dispatcher
from config import bot, dp


async def echo(massage: types.Message):
    bad_words = ['java', 'html', 'идиот', 'css', 'жопа', 'хуй', 'член', 'пизда']
    username = f'@{massage.from_user.username}' \
        if massage.from_user.username is not None else massage.from_user.first_name
    for word in bad_words:
        if word in massage.text.lower().replace(' ', ''):
            await bot.delete_message(massage.chat.id, massage.message_id)
            await massage.answer(f'не матерись {username}')
    if massage.text.startswith('.'):
        await bot.pin_chat_message(massage.chat.id, massage.message_id)
    if massage.text == 'dice':
        a = await bot.send_dice(massage.chat.id)
        print(a)


def reg_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
