import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN

from app.handlers import common, edituser, allusers


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(TOKEN)

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(common.router)
    dp.include_router(allusers.router)
    dp.include_router(edituser.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
