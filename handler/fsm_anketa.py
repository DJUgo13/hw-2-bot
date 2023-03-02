from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboard.client_kb import *
from keyboard import client_kb


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(massage: types.Message):
    if massage.chat.type == 'private':
        await FSMAdmin.name.set()
        await massage.answer('как тебя зовут', reply_markup=start_markup)
        await massage.answer('?', reply_markup=client_kb.cancel_markup)
    else:
        await massage.answer('че ссыш пошли раз на раз', reply_markup=client_kb.cancel_markup)


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('возраст свой скажи свой на?')


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer('пиши числа')
    elif not 16 <= int(massage.text) <= 19:
        await massage.answer('не подходишь')
    else:
        async with state.proxy() as date:
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('кто по жизни мужик или баба?',
                             reply_markup=client_kb.gender_markup)


async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('Где живешь брат эже?',
                         reply_markup=client_kb.cancel_markup)


async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('скинешь фото ?',
                         reply_markup=client_kb.cancel_markup)


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)
    async with state.proxy() as date:
        date['photo'] = massage.photo[0].file_id

        await massage.answer_photo(date["photo"],
                                   caption=f'{date["name"]} {date["age"]} '
                                           f'{date["gender"]}\n @{date["username"]}')
    await FSMAdmin.next()
    await massage.answer('norm?',
                         reply_markup=client_kb.submit_markup)


async def submit(massage: types.Message, state: FSMContext):
    if massage.text.lower() == "да":
        await massage.answer('все заебись', reply_markup=start_markup)
        await state.finish()
    elif massage.text == "хуево, переделывай":
        await massage.answer("как тебя зовут?", reply_markup=start_markup, )
        await FSMAdmin.name.set()
    else:
        await massage.answer("и что?")


async def cancel_reg(massage: types.Message, state: FSMContext):
    currents_state = await state.get_state()
    if currents_state is not None:
        await state.finish()
        await massage.answer("canceled")


def reg_hand_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=["cancel"])
    dp.register_message_handler(cancel_reg, Text(equals="cancel", ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)
