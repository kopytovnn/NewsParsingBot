from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy.orm import Session


from databaseCore.databasecore.models.user import User


router = Router()


# хендлер для получения тг id пользователя
@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    with Session() as session:
        await state.clear()
        user_id = message.from_user.id

        # Проверяем, существует ли пользователь в базе данных
        existing_user = session.query(User).filter(User.id == user_id).first()

        if not existing_user:
            # Добавление пользователя в базу данных
            user = User(id=user_id)
            session.add(user)
            session.commit()

    await message.answer("Ваш ID был сохранен.")