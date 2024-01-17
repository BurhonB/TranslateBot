import logging
from aiogram import Dispatcher, Bot, executor, types
from inline_btn import *
from database import *
from utils import translate_text


BOT_TOKEN = "6757980026:AAFqYBr3hRzQzGrn68hK5R_c7EmzDVycPlI"
ADMINS = [1636898306]

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


async def set_commands(dp: Dispatcher):
    await create_tables()
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Ishga tushirish")
        ]
    )

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer('Salom. Men Engu Tarjimon bot')


@dp.message_handler(commands=["stat"])
async def get_user_stat_handler(message: types.Message):
    if message.from_user.id in ADMINS:
     counts = await get_all_users()
     await message.answer(f"Bot azolari soni: {counts} ta")


@dp.message_handler(content_types=['text'])
async def get_user_text_handler(message: types.Message):
    btn = await translate_langs_btn()
    await message.answer(text=message.text, reply_markup=btn)


@dp.callback_query_handler(text_contains='lang')
async def selected_lang_callback(call: types.CallbackQuery):
    lang = call.data.split(':')[-1]
    text = call.message.text

    result_text = await translate_text(text=text, lang=lang)

    btn = await translate_langs_btn()
    await call.message.edit_text(text=result_text, reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands)
