from aiogram import types


def get_kb_start():
    buttons = [
        [
            types.InlineKeyboardButton(text="Все пользователи", callback_data="all_users"),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
