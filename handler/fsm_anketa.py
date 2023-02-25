from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboard.client_kb import start_markup


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    photo = State()
    gender = State()
    region = State()


async def fsm_start(massage: types.Message):
    if massage.chat.type == 'private':
        await FSMAdmin.name.set()
        await massage.answer('как тебя зовут')
    else:
        await massage.answer('пиши в лс')


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer('пиши числа')
    elif not 18 < int(massage.text) < 19:
        await massage.answer('не подходишь')
    else:
        async with state.proxy() as date:
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('пол?')


async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('где живешь?')


async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('скинешь фото ?')


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)


def reg_hand_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
