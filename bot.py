import asyncio
import logging

from aiogram import Bot, Dispatcher
from bot.clients import tg_client
from bot.handlers import user_handlers, user_handlers_demo

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    bot: Bot = tg_client.bot  # Получает объект бота из tg_client.

    dp: Dispatcher = tg_client.dp

    dp.include_router(user_handlers.router)
#    dp.include_router(user_handlers_demo.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True) # сбрасывает все накопленные обновления
        await dp.start_polling(bot) # поллинг, который непрерывно опрашивает сервер Telegram на предмет новых обновлений.
    finally:
        await bot.session.close()  # Закрывает сессию aiohttp клиента бота


if __name__ == '__main__': # Проверяет, запущен ли скрипт напрямую, а не импортирован как модуль
    asyncio.run(main()) # Запускает основную асинхронную функцию main() с помощью asyncio.run()
