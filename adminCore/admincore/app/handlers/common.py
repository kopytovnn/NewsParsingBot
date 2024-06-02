from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from ..keyboards.for_admin import get_kb_premium


router = Router()

users = set()


@router.callback_query(lambda c: c.data == 'all_users')
async def all_users_callback(callback_query: CallbackQuery):
    if users:
        users_list = "\n".join(str(user_id) for user_id in users)
        await callback_query.message.answer(f"Список всех пользователей:\n{users_list}")
    else:
        await callback_query.message.answer("Список пользователей пуст.")
    await callback_query.answer()

@router.message()
async def track_user(message: types.Message):
    users.add(message.from_user.id)


@router.callback_query(lambda c: c.data == 'edit_user')
async def edit_user_callback(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Что вы хотите сделать?",
        reply_markup=get_kb_premium()
    )
    await callback_query.answer()

@router.callback_query(lambda c: c.data == 'add_premium')
async def add_premium_callback(callback_query: CallbackQuery):
    await callback_query.message.answer("Премиум статус добавлен")
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'remove_premium')
async def remove_premium_callback(callback_query: CallbackQuery):
    await callback_query.message.answer("Премиум статус убран")
    await callback_query.answer()
