import logging

from aiogram import Bot, Dispatcher, executor, types
import asyncio

from aiogram import Bot, types

API_TOKEN = '5296851474:AAHC3L5vJ_IF7kRNWqTpp5_qwyRoZdV-0xE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

a = 0


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global a
    a = message.chat.id
    await message.answer('Начали работать)')


async def send_message():
    global a
    await bot.send_message(a, '1')


async def main():
    await send_message()


if __name__ == '__main__':
    asyncio.run(main())
