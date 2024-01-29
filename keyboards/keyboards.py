from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
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

button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])
button_lizard = KeyboardButton(text=LEXICON_RU['lizard'])
button_spock = KeyboardButton(text=LEXICON_RU['spock'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_rock, button_scissors, button_paper],
              [button_lizard, button_spock]],
    resize_keyboard=True
)

inlain_button1 = InlineKeyboardButton(text='Инлайн кнопка1', callback_data='callback_button1_pressed')
inlain_button2 = InlineKeyboardButton(text='Инлайн кнопка2', callback_data='callback_button2_pressed')

inlain_kb = InlineKeyboardMarkup(
    inline_keyboard=[[inlain_button1],
                     [inlain_button2]]
)
