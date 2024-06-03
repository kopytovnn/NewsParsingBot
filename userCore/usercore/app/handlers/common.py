from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..keyboards.for_user import get_kb_start

from ..handlers.allusers import users


router = Router()


# тестовый функционал для получения id
@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    # для теста сохраним id в множество users
    user_id = message.from_user.id
    users.add(user_id)
    await message.answer("Ваш ID был сохранен.", reply_markup=get_kb_start())
