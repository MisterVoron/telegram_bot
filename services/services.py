import random
from lexicon.lexicon import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


def _normalize_user_choice(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    user_choice = _normalize_user_choice(user_choice)
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'
