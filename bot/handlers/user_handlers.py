from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.keyboard_builder import welcome_keyboard
from bot.services.model_api_requests import generate_response

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Привет, я умный чат-бот', reply_markup=welcome_keyboard())


@router.callback_query(lambda callback: callback.data == 'start') # смотрим если колбэкдата в сообщении равна 'start'
async def start_message(callback_query: CallbackQuery):
    await callback_query.message.answer('Задай свой вопрос')


@router.callback_query(lambda callback: callback.data == 'help')
async def help_message(callback_query: CallbackQuery):
    await callback_query.message.answer('Помощь')


@router.message(Command(commands=['help']))
async def help_command_handler(message: Message):
    await message.answer('/start')


@router.message()
async def echo_handler(message: Message):
    await generate_response(message)
