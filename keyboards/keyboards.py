from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

button1 = KeyboardButton(text=LEXICON_RU['rock'])
button2 = KeyboardButton(text=LEXICON_RU['scissors'])
button3 = KeyboardButton(text=LEXICON_RU['paper'])
button4 = KeyboardButton(text=LEXICON_RU['lizard'])
button5 = KeyboardButton(text=LEXICON_RU['spock'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button1, button2, button3],
              [button4, button5]],
    resize_keyboard=True
)
