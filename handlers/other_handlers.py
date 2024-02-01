from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon.lexicon import LEXICON
from copy import deepcopy
from database.database import users_db, user_dict_template


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


@router.message()
async def process_any_other_message(message: Message):
    if users_db.get(message.from_user.id):
        await message.answer('Я не знаю, что ответить на это.')
    else:
        await message.answer('Нажмите команду /start чтобы начать работу с ботом.')
