import asyncio
from aiogram import executor

from loader import dp, db, bot
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await db.create()
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)