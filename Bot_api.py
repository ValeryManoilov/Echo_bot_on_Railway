from Config import Config
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler()
async def cmd_start(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
