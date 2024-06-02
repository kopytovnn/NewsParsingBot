import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN

from aiogram.filters.command import Command

from app.handlers import common, edituser
from app.handlers.common import users

from app.keyboards.for_admin import get_kb_start


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация хендлера на команду /start
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        users.add(message.from_user.id)
        await message.answer("Что вы хотите сделать?", reply_markup=get_kb_start())

    dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
