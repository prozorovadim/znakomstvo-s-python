import random
import config
from create_bot import dp
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    kb = [
        [
            KeyboardButton(text="/играть"),
            KeyboardButton(text="/new"),
            KeyboardButton(text="/about")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Привет!\nЯ бот Вадима Викторовича!\nЯ очень крут, как и мой создатель. Нажми на кнопки внизу.", reply_markup=keyboard)
@dp.message_handler(commands=['играть'])
async def mes_start(message: Message):
    await message.answer(text=f'привет! {message.from_user.first_name} \n Сегодня мы с тобой поиграем в интересную игру')


@dp.message_handler(commands='new')
async def mes_new_dame(message: Message):

    await message.answer(text=f'И так, на столе {config.total} конфет. Кидаем жребий, кто берет первым')
    coin = random.randint(0, 1)
    config.games[message.from_user.id] = 150
    if coin == 1:
        await message.answer(text= f' {message.from_user.first_name}, поздравляю! Выпал орёл. Ты ходишь первым. Бери от 1 до 28 конфет')


    else:
        await message.answer(text=f' {message.from_user.first_name}, не расстраивайся первый ход делает бот')
        await bot_turn(message)


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Перейти на сайт, где я работаю', url='https://utnkr.ru')
urlButton2 = InlineKeyboardButton(text='Перейти к нашему боту', url='https://t.me/rks_nt_bot')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands='about')
async def url_command(message: Message):
    await message.answer('Немного обо мне:', reply_markup=urlkb)




@dp.message_handler()
async def all_catch(message: Message):
    if message.text.isdigit()==True:
        if (0 < int(message.text)) and (int(message.text) < 29):
            await player_turn(message)
        else:
            await message.answer(text=f'Ах ты, хитрый {message.from_user.first_name}! Конфет надо взять хотя бы одну, но не больше 28. Попробуй еще раз')
    else:
        await message.answer(text='Введи цифрами количество конфет')



async def player_turn(message: Message):
    take_amount = int(message.text)
    print(config.games.get(message.from_user.id))
    (config.games[message.from_user.id]) = int(config.games.get(message.from_user.id)) - take_amount

    name = message.from_user.first_name
    await message.answer(text=f'{name} взял {take_amount} конфет и на столе осталось {config.games.get(message.from_user.id)}\n')

    if await check_victory(message, name):
        return
    await message.answer(text=f'Торжественно передаем ход боту!')
    await bot_turn(message)


async def bot_turn(message: Message):

    take_amount = 0
    current_total = (config.games.get(message.from_user.id))
    if current_total <= 28:
        take_amount = current_total
    else:
        take_amount = current_total % 29 if current_total % 29 != 0 else 1
    config.games[message.from_user.id] = (config.games.get(message.from_user.id) - take_amount)
    name = message.from_user.first_name
    await message.answer(text=f'Бот взял {take_amount} конфет и на столе осталось {config.games.get(message.from_user.id)} \n')
    if await check_victory(message, 'Бот'):
        return

    await message.answer(text=f' {name} теперь твой черед! Бери конфеты')



async def check_victory(message: Message, name: str):
    if config.games.get(message.from_user.id) <= 0:
        await message.answer(text=f'Победил {name}! Это была славная игра')
        config.games.pop(message.from_user.id)
        return True
    return False

async def player_goroskop(message: Message):
    await message.answer(text=f'Введи дату своего рожедния и получишь предсказание на этот месяц')
