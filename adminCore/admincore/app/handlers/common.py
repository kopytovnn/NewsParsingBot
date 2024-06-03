from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..keyboards.for_admin import get_kb_start

from ..handlers.edituser import users

router = Router()


# Регистрация хендлера на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    # оставлю для теста
    users.add(message.from_user.id)
    await message.answer("Выберете следующее действие:", reply_markup=get_kb_start())
