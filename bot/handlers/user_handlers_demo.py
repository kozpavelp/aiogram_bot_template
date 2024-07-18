from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

'''
Message - это тип данных, представляющий сообщение от пользователя
'''

router = Router()
'''
Router из aiogram используется для маршрутизации команд и сообщений. Он позволяет организовать хэндлеры в логические группы.
'''

'''
Ручки обрабатываются сверху вниз, как мы их видим в модуле
'''


@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Привет! Я бот. Напиши мне сообщение и получи его обратно")


@router.message(Command(commands=['help']))
async def help_command_handler(message: Message):
    help_text = (
        "Список доступных команд:\n"
        "/help - Получить справку\n"
        "/start - Начать диалог\n"
        "/my_command - какая-то команда\n"
    )
    await message.answer(help_text)


@router.message(Command(commands=['my_command']))
async def my_command_handler(message: Message):
    await message.answer("Демонстрация кастомной команды")


# Просто эхо на ЛЮБОЕ сообщение для демонстрации работы бота
@router.message()
async def echo_handler(message: Message):
    await message.answer(message.text)


