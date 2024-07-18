from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from bot.config import config, Config


class TelegramCli:
    def __init__(self):
        self.config: Config = config
        self.bot: Bot = Bot(token=self.config.tg.TOKEN,
                            default=DefaultBotProperties(parse_mode='HTML'))
        self.dp: Dispatcher = Dispatcher(token=self.config.tg.TOKEN, bot=self.bot)
        self.bot_info = None

    async def setup(self):
        self.bot_info = await self.bot.get_me()
        print(f"Bot info: {self.bot_info}")

    async def close(self):
        await self.bot.close()

    async def send_message(self, chat_id: str, message: str):
        return await self.bot.send_message(chat_id=chat_id, text=message)

