from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import random


ATTEMPTS = 5
user = {
    'in_game': False,
    'total_games': 0,
    'wins': 0,
    'attempts': None,
    'secret_key': None
}


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_random_number() -> int:
    return random.randint(1, 100)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Hello.\nI want to play game with you!\n'
        'Game called <<Guees the number>>\nDo you want to play?'
    )


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        text='This is the game <<Guess the number>>\n'
        'You need to guess hidden number\n'
        f'You have {ATTEMPTS} attempts\n'
        'If you do not guess you lose\n'
        'You may use command /cancel for exit from the game\n'
        'As well command /state for look your statistics\n'
        'Do you want to play?'
    )


@dp.message(Command(commands=['state']))
async def show_statistics(message: Message):
    await message.answer(
        text=f'{user["total_games"]} total amount of games\n'
        f'{user["wins"]} total amount of wins'
    )


@dp.message(Command(commands=['cancel']))
async def exit_from_game(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            text='You exit from the game'
        )
    else:
        await message.answer(
            text='You do not in the game\n'
            'Do you want to play?'
        )


@dp.message(F.text.lower().in_(['yes', "let's go", 'yeah', 'y']))
async def start_game(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['attempts'] = ATTEMPTS
        user['secret_key'] = get_random_number()
        await message.answer(text='Start the game!\nEnter a number')
    else:
        await message.answer('While we are in the game I can react only on digit and command /cancel')


@dp.message(F.text.lower().in_(['no', 'nope', 'not', "don't", 'do not']))
async def refuse_from_game(message: Message):
    if not user['in_game']:
        await message.answer(text="It's a pity\nWrite when be want to play")
    else:
        await message.answer('While we are in the game I can react only on digit and command /cancel')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def game(message: Message):
    if user['in_game']:
        number = int(message.text)
        key = user['secret_key']
        if number == key:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer(text='You are win! Congratulations\nDo you play again?')
        elif number > key:
            user['attempts'] -= 1
            await message.answer(text='Secret number less')
        elif number < key:
            user['attempts'] -= 1
            await message.answer(text='Secret number larger')
        if user['attempts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(text=f"You are lose\nSecret number was {user['secret_key']}\nDo you want to play again?")
    else:
        await message.answer(text="We don't play yet\nDo you want to play?")


@dp.message()
async def process_other_words(message: Message):
    if user['in_game']:
        await message.answer(text='We in the game!\nHere you can enter digits and command /cancel\n Have you understand?!')
    else:
        await message.answer(text="I'm constraint bot.\nEnter the commands that is in the /help")


if __name__ == '__main__':
    dp.run_polling(bot)
