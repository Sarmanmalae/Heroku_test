import logging
from random import randint

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import Bot, Dispatcher, executor, types
from requests import get, put, post

API_TOKEN = '5296851474:AAHC3L5vJ_IF7kRNWqTpp5_qwyRoZdV-0xE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup(one_time_keyboard=True)
keyboard.add(InlineKeyboardButton(text="Заказ готов!", callback_data="ready"))

keyboard2 = InlineKeyboardMarkup(one_time_keyboard=True)
keyboard2.add(InlineKeyboardButton(text="Готово!✅", callback_data="finished"))

keyboard1 = InlineKeyboardMarkup()
keyboard1.add(InlineKeyboardButton(text="To order", callback_data="order"))


@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Начнем работу!", reply_markup=keyboard1)


@dp.callback_query_handler(text="order")
async def send_random_value(call: types.CallbackQuery):
    await bot.send_message(-1001506674517,
                           f'Номер заказа: 23\nИмя клиента: Кирилл\nСодержание заказа:\nЭспрессо(1шт.)\nКруассаны(3шт.)',
                           reply_markup=keyboard)


@dp.callback_query_handler(text="ready")
async def send_random_value(call: types.CallbackQuery):
    await bot.delete_message(chat_id=-1001506674517, message_id=call.message.message_id)
    await bot.send_message(-1001506674517,
                           f'Номер заказа: 23\nИмя клиента: Кирилл\nСодержание заказа:\nЭспрессо(1шт.)\nКруассаны(3шт.)',
                           reply_markup=keyboard2)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
