from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb, inlain_kb
from services.services import get_bot_choice, get_winner
from services.statistic import user, users
from lexicon.lexicon import LEXICON_RU


router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    id_user = message.from_user.id
    if id_user not in users:
        users[id_user] = user
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка Меню удалена!')


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


@router.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    id_user = message.from_user.id
    await message.answer(text=f'{LEXICON_RU["win"]} {users[id_user]["win"]}\n'
                              f'{LEXICON_RU["lose"]} {users[id_user]["lose"]}\n'
                              f'{LEXICON_RU["draw"]} {users[id_user]["draw"]}',
                              reply_markup=inlain_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text.in_([LEXICON_RU['paper'],
                            LEXICON_RU['rock'],
                            LEXICON_RU['scissors'],
                            LEXICON_RU['lizard'],
                            LEXICON_RU['spock']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
