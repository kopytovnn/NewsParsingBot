from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from ..keyboards.for_admin import get_kb_premium, get_kb_users

from aiogram.fsm.state import State, StatesGroup

router = Router()

users = set()


class EditUserStates(StatesGroup):
    action = State()
    user_id = State()


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
async def edit_user_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(EditUserStates.action)
    await callback_query.message.answer(
        "Что вы хотите сделать?",
        reply_markup=get_kb_premium()
    )
    await callback_query.answer()


@router.callback_query(lambda c: c.data in ['add_premium', 'remove_premium'])
async def process_action(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(action=callback_query.data)
    await state.set_state(EditUserStates.user_id)
    await callback_query.message.answer(
        "Выберите пользователя:",
        reply_markup=get_kb_users(users)
    )
    await callback_query.answer()


@router.callback_query(lambda c: c.data.startswith('user_'))
async def process_user_id(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.data.split('_')[1]
    user_data = await state.get_data()
    action = user_data['action']

    if action == 'add_premium':
        await callback_query.message.answer(f"Премиум статус добавлен для пользователя {user_id}")
    elif action == 'remove_premium':
        await callback_query.message.answer(f"Премиум статус убран для пользователя {user_id}")

    await state.clear()
    await callback_query.answer()
