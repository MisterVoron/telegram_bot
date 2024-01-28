import random
from lexicon.lexicon import LEXICON_RU
from services.statistic import users
from aiogram.types import Message


def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


def _normalize_user_choice(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


def get_winner(user_choice: Message, bot_choice: str) -> str:
    rules = {'rock': ('scissors', 'lizard'),
             'scissors': ('paper', 'lizard'),
             'paper': ('rock', 'spock'),
             'lizard': ('spock', 'paper'),
             'spock': ('scissors', 'rock')}
    id_user = user_choice.from_user.id
    user_choice = _normalize_user_choice(user_choice.text)
    if user_choice == bot_choice:
        users[id_user]['draw'] += 1
        return 'nobody_won'
    elif bot_choice in rules[user_choice]:
        users[id_user]['win'] += 1
        return 'user_won'
    users[id_user]['lose'] += 1
    return 'bot_won'
