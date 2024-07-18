import aiohttp
from aiogram.types import Message
from bot.config import config

api = config.api #/generate


async def generate_response(message: Message):
    async with aiohttp.ClientSession() as session:
        payload = {'text': message.text}
        async with session.post(api.API_URL, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                generated_text = data.get('generated_text', 'Ошибка в ответе от модели')
                await message.answer(generated_text)
            else:
                await message.answer('Ошибка при обращении к API модели')