from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db


async def all_companies_default_keyboard():
    companies = await db.select_all_companies()

    markup = ReplyKeyboardMarkup()
    markup.resize_keyboard = True
    markup.row_width = 2

    markup.insert(KeyboardButton(text="🔙 Bosh Menyu"))

    for company in companies:
        text_button = company['name']
        markup.insert(KeyboardButton(text_button))

    markup.insert(KeyboardButton(text="🔙 Bosh Menyu"))

    return markup
