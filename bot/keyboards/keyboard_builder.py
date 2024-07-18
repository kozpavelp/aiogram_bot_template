from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

buttons = {
    'yes': 'Да',
    'no': 'Нет',
}

welcome = {
    'start': 'Начать',
    'help': 'Помощь',
}


def create_keyboard(buttons_dict: dict) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=text,
        callback_data=callback_data) for callback_data, text in buttons_dict.items()])

    return kb_builder.as_markup()


def yes_no_keyboard() -> InlineKeyboardMarkup:
    return create_keyboard(buttons)


def welcome_keyboard() -> InlineKeyboardMarkup:
    return create_keyboard(welcome)