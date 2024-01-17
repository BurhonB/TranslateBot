from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def translate_langs_btn():
    btn = InlineKeyboardMarkup(row_width=2)

    btn.add(

        InlineKeyboardButton(text='ru', callback_data='lang:ru'),
        InlineKeyboardButton(text='uz', callback_data='lang:uz'),
        InlineKeyboardButton(text='en', callback_data='lang:en'),
        InlineKeyboardButton(text='uk', callback_data='lang:uk'),
        InlineKeyboardButton(text='pt', callback_data='lang:pt'),
        InlineKeyboardButton(text='fr', callback_data='lang:fr'),
        InlineKeyboardButton(text='it', callback_data='lang:it'),
        InlineKeyboardButton(text='am', callback_data='lang:am')
    )

    return btn
