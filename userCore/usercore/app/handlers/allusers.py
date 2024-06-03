from aiogram import Router
from aiogram.types import CallbackQuery


router = Router()

users = set()   # временное хранилище пользователей


@router.callback_query(lambda c: c.data == 'all_users')
async def all_users_callback(callback_query: CallbackQuery):
    # здесь будет функционал вывода пользователей из бд, но пока так
    if users:
        users_list = "\n".join(str(user_id) for user_id in users)
        await callback_query.message.answer(f"Список всех пользователей:\n{users_list}")
    else:
        await callback_query.message.answer("Список пользователей пуст.")
    await callback_query.answer()