from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON_RU


router = Router()

@router.callback_query(F.data == 'callback_button1_pressed')
async def process_button1_pressed(callback: CallbackQuery):
    if callback.message.text != 'Инлайн кнопка 1 была нажата':
        await callback.message.edit_text(
            text='Инлайн кнопка 1 была нажата',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()

@router.callback_query(F.data == 'callback_button2_pressed')
async def process_button2_pressed(callback: CallbackQuery):
    if callback.message.text != 'Инлайн кнопка 2 была нажата':
        await callback.message.edit_text(
            text='Инлайн кнопка 2 была нажата',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()

@router.message()
async def send_answer(message: Message):
    await message.answer(LEXICON_RU['other_answer'])
