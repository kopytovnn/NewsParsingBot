from aiogram import types


def get_kb_start():
    buttons = [
        [
            types.InlineKeyboardButton(text="Все пользователи", callback_data="all_users"),
            types.InlineKeyboardButton(text="Изменить для данного пользователя", callback_data="edit_user")
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_premium():
    buttons = [
        [
            types.InlineKeyboardButton(text="Добавить премиум статус", callback_data="add_premium"),
            types.InlineKeyboardButton(text="Убрать премиум статус", callback_data="remove_premium")
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
