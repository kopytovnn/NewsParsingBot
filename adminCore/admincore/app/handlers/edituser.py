from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from ..keyboards.for_admin import get_kb_premium

from aiogram.fsm.state import State, StatesGroup


router = Router()


class EditUserStates(StatesGroup):
    action = State()
    user_id = State()


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
        "Введите ID пользователя:"
    )
    await callback_query.answer()


@router.message(EditUserStates.user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    user_id = message.text
    user_data = await state.get_data()
    action = user_data['action']

    if action == 'add_premium':
        await message.answer(f"Премиум статус добавлен для пользователя {user_id}")
    elif action == 'remove_premium':
        await message.answer(f"Премиум статус убран для пользователя {user_id}")

    await state.clear()
