import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

loop = asyncio.new_event_loop()

bot = Bot(BOT_TOKEN, parse_mode='HTML')

storage = MemoryStorage()

dp = Dispatcher(bot, loop, storage=storage)

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, skip_updates=True)
